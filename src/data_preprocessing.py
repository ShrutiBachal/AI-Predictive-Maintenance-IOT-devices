import pandas as pd

def load_data(file_path):
    """
    Load dataset from CSV file
    """
    df = pd.read_csv(file_path)
    return df


def clean_data(df):
    """
    Clean dataset:
    - Remove null values
    - Remove duplicates
    """
    df = df.drop_duplicates()
    df = df.dropna()
    return df


def save_processed_data(df, output_path):
    """
    Save cleaned data
    """
    df.to_csv(output_path, index=False)