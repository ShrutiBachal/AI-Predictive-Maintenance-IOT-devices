def predict_failure(model, X_test):
    """
    Predict failure and probability
    """
    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)[:, 1]

    results = []

    for pred, prob in zip(predictions, probabilities):
        if prob > 0.7:
            alert = "CRITICAL"
        elif prob > 0.5:
            alert = "WARNING"
        else:
            alert = "NORMAL"

        results.append({
            "prediction": int(pred),
            "probability": float(prob),
            "alert": alert
        })

    return results