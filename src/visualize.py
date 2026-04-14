import matplotlib.pyplot as plt


def plot_temperature(df):
    """
    Plot temperature trend
    """
    plt.figure()
    plt.plot(df['temperature'])
    plt.title("Temperature Trend")
    plt.xlabel("Time")
    plt.ylabel("Temperature")
    plt.savefig("images/plots/temperature.png")
    plt.close()


def plot_failure_distribution(df):
    """
    Plot failure distribution
    """
    plt.figure()
    df['failure'].value_counts().plot(kind='bar')
    plt.title("Failure Distribution")
    plt.savefig("images/plots/failure_distribution.png")
    plt.close()