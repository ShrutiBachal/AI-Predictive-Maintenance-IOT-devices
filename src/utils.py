import pandas as pd

def save_predictions(results, path):
    """
    Save predictions to CSV
    """
    df = pd.DataFrame(results)
    df.to_csv(path, index=False)


def save_metrics(metrics, path):
    """
    Save metrics to text file
    """
    with open(path, "w") as f:
        for key, value in metrics.items():
            f.write(f"{key}: {value}\n")