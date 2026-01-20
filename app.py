import streamlit as st
import pyarrow.parquet as pq
import pandas as pd
from io import BytesIO

from core.converter import parquet_to_csv_bytes

# ==================================================
# App Config
# ==================================================
st.set_page_config(
    page_title="Parquet -> CSV Converter",
    layout="wide",
    page_icon="🧱",
)

# ==================================================
# Password Protection
# ==================================================
def check_password() -> bool:
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if st.session_state.authenticated:
        return True
    
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if password == st.secrets["APP_PASSWORD"]:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Incorrect password")

    return False

if not check_password():
    st.stop()

# ==================================================
# UI
# ==================================================
st.title("Parquet -> CSV Converter")

uploaded_file = st.file_uploader(
    "Upload a Parquet file",
    type=["parquet"],
)

if uploaded_file is None:
    st.info("Upload a `.parquet` file to begin.")
    st.stop()

# ==================================================
# Preview Section
# ==================================================
st.subheader("Preview (Raw Data)")

parquet_bytes = uploaded_file.getvalue()
parquet_buffer = BytesIO(parquet_bytes)
parquet_file = pq.ParquetFile(parquet_buffer)

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Schema**")
    st.code(str(parquet_file.schema_arrow), language="text")

with col2:
    st.markdown("**Data (head)**")
    table = parquet_file.read_row_group(0)
    df_preview = table.to_pandas().head(20)
    st.dataframe(df_preview, use_container_width=True)

# ===================================================
# Conversion section
# ===================================================
st.divider()
st.subheader("Convert")

progress_bar = st.progress(0.0)

if st.button("Convert to CSV"):
    csv_buffer = parquet_to_csv_bytes(
        parquet_bytes,
        progress_cb=lambda p: progress_bar.progress(p),
    )

    st.success("Conversion complete")

    st.download_button(
        label="Download CSV",
        data=csv_buffer,
        file_name=uploaded_file.name.replace(".parquet", ".csv"),
        mime="text/csv",
    )