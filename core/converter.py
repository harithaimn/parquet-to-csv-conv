from pathlib import Path
#from tqdm import tqdm

from io import BytesIO
from typing import Callable, Optional
import pyarrow.parquet as pq
import pyarrow.csv as pcsv

# input_path = Path("data/raw/meta.parquet")
# output_path = Path("data/raw/meta_convfromparquet.csv")
# output_path.parent.mkdir(parents=True, exist_ok=True)

# parquet_file = pq.ParquetFile(input_path)

def parquet_to_csv_bytes(
    parquet_bytes: bytes,
    progress_cb: Optional[Callable[[float], None]] = None,
) -> BytesIO:
    """
    Convert Parquet (bytes) -> CSV (BytesIO).

    progress_cb: optional callback taking progress float [0, 1]
    """

    parquet_buffer = BytesIO(parquet_bytes)
    parquet_file = pq.ParquetFile(parquet_buffer)

    output_buffer = BytesIO()

    total_groups = parquet_file.num_row_groups

    with pcsv.CSVWriter(output_buffer, parquet_file.schema_arrow) as writer:
        for i in range(total_groups):
            table = parquet_file.read_row_group(i)
            writer.write_table(table)

            if progress_cb:
                progress_cb((i + 1) / total_groups)
            
    output_buffer.seek(0)
    return output_buffer