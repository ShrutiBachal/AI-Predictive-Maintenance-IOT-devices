def create_features(df):
    """
    Create new features from sensor data
    """

    # Rolling mean (window size = 5)
    df['temp_mean_5'] = df['temperature'].rolling(window=5).mean()

    # Difference in vibration
    df['vibration_diff'] = df['vibration'].diff()

    # Fill NaN values created by rolling/diff
    df = df.fillna(method='bfill')

    return df