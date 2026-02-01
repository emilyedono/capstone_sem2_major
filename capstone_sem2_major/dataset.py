from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer
import pandas as pd

from capstone_sem2_major.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    input_path: Path = RAW_DATA_DIR / "dataset.csv",
    output_path: Path = PROCESSED_DATA_DIR / "dataset.csv",
    # ----------------------------------------------
):
    # ---- REPLACE THIS WITH YOUR OWN CODE ----
    logger.info("Processing dataset...")
    df = pd.read_csv(input_path)

    # rename "name" column to "neighborhood"
    df = df.rename(columns={"name": "neighborhood"})

    df.to_csv(output_path, index=False)
    logger.success("Processing dataset complete.")
    # -----------------------------------------


if __name__ == "__main__":
    app()
