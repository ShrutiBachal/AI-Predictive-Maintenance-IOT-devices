import pandas as pd


def load_nasa_dataset(file_path):
    """
    Load and clean NASA turbofan dataset
    """

    # Column names (standard for FD001 dataset)
    columns = ["unit", "cycle", "setting1", "setting2", "setting3"] + [f"sensor_{i}" for i in range(1, 22)]

    # Load data
    df = pd.read_csv(file_path, sep=r"\s+", header=None)

    # Assign column names
    df.columns = columns

    return df

def add_failure_label(df):
    """
    Create failure label based on last cycles
    """

    # Get max cycle per engine
    max_cycle = df.groupby("unit")["cycle"].max().reset_index()
    max_cycle.columns = ["unit", "max_cycle"]

    # Merge
    df = df.merge(max_cycle, on="unit")

    # Remaining useful life
    df["RUL"] = df["max_cycle"] - df["cycle"]

    # Define failure (last 30 cycles = failure)
    df["failure"] = df["RUL"].apply(lambda x: 1 if x <= 30 else 0)

    return df

def save_clean_data(df, output_path):
    df.to_csv(output_path, index=False)