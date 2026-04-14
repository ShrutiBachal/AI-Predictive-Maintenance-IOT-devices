from src.load_nasa_data import load_nasa_dataset, add_failure_label, save_clean_data

# Load raw NASA file
df = load_nasa_dataset("data/raw/train_FD001.txt")

# Add failure label
df = add_failure_label(df)

# Save cleaned dataset
save_clean_data(df, "data/processed/nasa_cleaned.csv")

print(df.head())
print("Dataset cleaned and saved!")