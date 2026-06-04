import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    df = pd.read_csv("epa-sea-level.csv")

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_all = np.arange(df["Year"].min(), 2051)
    y_all = res.slope * x_all + res.intercept
    ax.plot(x_all, y_all, "r")

    df_recent = df[df["Year"] >= 2000]
    res_recent = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )
    x_recent = np.arange(2000, 2051)
    y_recent = res_recent.slope * x_recent + res_recent.intercept
    ax.plot(x_recent, y_recent, "g")

    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    fig.savefig("sea_level_plot.png")
    return plt.gca()