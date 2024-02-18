import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.set_xlim(1850, 2075)
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], alpha=0.5) # populate the scatter plot

    # Create first line of best fit
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    df_bestfit = pd.DataFrame({
        "Year": range(1880, 2051),
        "Sea Level": [res.intercept + res.slope * year for year in range(1880, 2051)]
    })
    ax.plot(df_bestfit["Year"], df_bestfit["Sea Level"], "green")

    # Create second line of best fit
    df_recent = df[df["Year"] >= 2000]
    res_recent = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    df_recent_bestfit = pd.DataFrame({
        "Year": range(2000, 2051),
        "Sea Level": [res_recent.intercept + res_recent.slope * year for year in range(2000, 2051)]
    })
    ax.plot(df_recent_bestfit["Year"], df_recent_bestfit["Sea Level"], "magenta")

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.grid(True)

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()