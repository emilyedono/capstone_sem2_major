from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

from capstone_sem2_major.config import FIGURES_DIR, PROCESSED_DATA_DIR
import pandas as pd
import matplotlib.pyplot as plt

app = typer.Typer()


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    input_path: Path = PROCESSED_DATA_DIR / "dataset.csv",
    output_path: Path = FIGURES_DIR / "arealand_sqmi_by_neighborhood.png",
    # -----------------------------------------
):
    # ---- REPLACE THIS WITH YOUR OWN CODE ----
    logger.info("Generating plot from data...")
    
    # make bar chart of arealand_sqmi by neighborhood
    df = pd.read_csv(input_path)
    plt.figure(figsize=(10, 6))
    plt.bar(df["neighborhood"], df["arealand_sqmi"])
    plt.xlabel("Neighborhood")
    plt.ylabel("Area Land (sq mi)")
    plt.title("Area Land by Neighborhood")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(output_path)
    logger.success("Plot generation complete.")
    # -----------------------------------------


if __name__ == "__main__":
    app()
