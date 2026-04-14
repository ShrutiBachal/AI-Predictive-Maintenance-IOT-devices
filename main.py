from src.data_preprocessing import load_data, clean_data, save_processed_data
from src.feature_engineering import create_features
import pandas as pd

def main():
    # 1. Load Data
    df = pd.read_csv("data/processed/nasa_cleaned.csv")
    # Map sensors to meaningful names
    df["temperature"] = df["sensor_2"]
    df["vibration"] = df["sensor_3"]
    df["pressure"] = df["sensor_4"]

    # 2. Clean Data
    df = clean_data(df)

    # 3. Feature Engineering
    df = create_features(df)

    # 4. Save Processed Data
    save_processed_data(df, "data/processed/nasa_processed.csv")

if __name__ == "__main__":
    main()