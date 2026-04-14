from src.data_preprocessing import load_data, clean_data, save_processed_data
from src.feature_engineering import create_features
from src.model_training import train_model, save_model
from src.evaluate import evaluate_model
from src.predict import predict_failure
from src.utils import save_predictions, save_metrics
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

     # 5. Train Model
    model, X_test, y_test = train_model(df)

    # 6. Save model
    save_model(model, "models/model.pkl")

    # 7. Evaluate
    metrics, y_pred = evaluate_model(model, X_test, y_test)

    # 8. Save metrics
    save_metrics(metrics, "outputs/metrics.txt")

    # 9. Predict
    results = predict_failure(model, X_test)

    # 10. Save predictions
    save_predictions(results, "outputs/predictions.csv")

if __name__ == "__main__":
    main()