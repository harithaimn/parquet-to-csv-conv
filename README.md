# Parquet → CSV Converter (Streamlit)

A simple Streamlit app for converting Parquet files to CSV, fully in-memory, with data preview and download support.

🌐 **Live App:**  
👉 https://parquet-to-csv-conv.streamlit.app/

Designed for:

- Data engineers
- Analysts
- ML practitioners
- Internal tooling / utilities

No files are written to disk. No persistence. Stateless by design.

## Features

🔐 Password-protected access  
📤 Upload .parquet files  
👀 Preview raw data (schema + head)  
🔄 Convert Parquet → CSV (PyArrow)  
📊 Progress indicator during conversion  
📥 Download CSV output  
💾 Fully in-memory (no storage, no temp files)  

## Tech Stack

- Python  
- Streamlit — UI  
- PyArrow — Parquet & CSV handling  
- pandas — lightweight preview only  
- tqdm — reusable progress abstraction (non-UI)  

## Project Structure
```
parquet_to_csv_app/
│
├── app.py                 # Streamlit app (auth, UI, preview)
│
├── core/
│   └── converter.py       # In-memory Parquet → CSV logic
│
├── .streamlit/
│   ├── config.toml        # UI theme (tracked)
│   └── secrets.toml       # App password (NOT tracked)
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup
1️⃣ **Create virtual environment**  
```bash
python -m venv .venv  
source .venv/bin/activate   # Linux / macOS  
.venv\Scripts\activate    # Windows
```

2️⃣ **Install dependencies**
```bash  
pip install -r requirements.txt
```

## Configuration

`.streamlit/secrets.toml`

Create this file locally (do not commit it):

```toml
APP_PASSWORD = "replace-with-a-strong-password"
```

`.streamlit/config.toml`

Controls the dark theme (already versioned).

## Running the App
```bash
streamlit run app.py
```

Open the URL shown in your terminal (usually `http://localhost:8501`).

## Usage Flow

1. Enter password  
2. Upload a .parquet file  
3. Preview schema and sample rows  
4. Click Convert to CSV  
5. Download the generated CSV

## Possible Extensions

- Password hashing (bcrypt)  
- File size limits  
- Multi-file batch conversion  
- CSV delimiter / encoding options  
- Schema diff view  
- Streamlit Cloud deployment

## License

Internal / utility use.  
Copyrighted by Harith Aiman | January 2026.