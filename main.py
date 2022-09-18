
from typing import Any
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame
from pandas.io.parsers import TextFileReader
from scipy.signal import savgol_filter
from curveData import create_reach_data

# 2. Loop through Budget and find point of exponential Cost Increase

# Read CSV File
dataframe: TextFileReader | DataFrame | Any = pd.read_csv(create_reach_data())


# Cleaning Data and Naming

dataframe.rename(columns={"Budget": "Budget",
                          "Reach": "Reach_Percent",
                          "GRP": "GRP",
                          "CostPerReachPoint": "CPR"}, inplace=True)

# Define Change in Budget and Reach to calculate Marginal Reach
budget_change = dataframe.Budget.diff()
reach_change = dataframe.Reach_Percent.diff()
marginal_reach = reach_change / budget_change
smooth_marginal_reach = savgol_filter(marginal_reach, 51, 3)

# Append marginal reach & smooth marginal reach to Dataframe
dataframe["marginal_reach"] = marginal_reach
dataframe["smooth_marginal_reach"] = smooth_marginal_reach

# Turn Reach_Percent, marginal_reach and smooth_marginal_reach into a float with 2 decimal places and multiply by 100
dataframe["Reach_Percent"] = dataframe["Reach_Percent"].apply(lambda x: round(x, 4) * 100)
dataframe["marginal_reach"] = dataframe["marginal_reach"].apply(lambda x: round(x, 4) * 100)
dataframe["smooth_marginal_reach"] = dataframe["smooth_marginal_reach"].apply(lambda x: round(x, 4) * 10000)


# display the dataframe to check for errors
print(dataframe)

def calculate_diminishing_point(marginal_product):
    try:
        for index, point in enumerate(marginal_product):
            if index == len(marginal_product) - 1:
                break
            print(index, point)
            # If the next point is not achieving 1% increment vs current point, we have found the Diminishing Point
            if index + 1 < len(marginal_product) and point <= (marginal_product[index + 1] * 1.01):
                print("Diminishing Point is at index: ", point)
                # Convert the current Point into corresponding Reach using the index
                inflection_point = dataframe.iloc[index, 1]

                print(inflection_point)
                print(type(inflection_point))
                return inflection_point

    except KeyError:
        pass


def visualize():
    # Create Figure and Axes to plot data and label Axes
    fig, ax = plt.subplots(figsize=(10, 6), constrained_layout=True)

    x = dataframe["Budget"]
    y = dataframe["Reach_Percent"]
    diminish_point = calculate_diminishing_point(smooth_marginal_reach)

    # Set Diagram Labels
    ax.set_xlabel('Budget')
    ax.set_ylabel('Reach %')

    # Set X Ticks to a slight rotation
    plt.xticks(rotation=45)

    # plot the final Plot
    plt.plot(x, y)

    # Build Lines to highlight the Diminishing Point

    # Determine the horizontal length of the line by finding the index of the Diminishing Point
    horizontal_length = dataframe.loc[dataframe['Reach_Percent'] == diminish_point, 'Budget']

    # Determine the vertical length of the line by finding the index of the Diminishing Point
    vertical_length = dataframe.loc[dataframe['Reach_Percent'] == diminish_point, 'Reach_Percent']

    # Plot the horizontal line
    plt.plot([0, horizontal_length], [vertical_length, vertical_length], color='red', linestyle='--')

    # Plot the vertical line
    plt.plot([horizontal_length, horizontal_length], [0, vertical_length], color='red', linestyle='--')

    # Create a second Y Axis to show the CPR
    ax2 = ax.twinx()
    ax2.set_ylabel('Marginal Reach')
    ax2.plot(x, dataframe["smooth_marginal_reach"], color='green')

    plt.show()


# Giving the User Output on the Diminishing Point and visualizing the Reach Curve

# Define the Diminishing Point
diminishing_point = calculate_diminishing_point(smooth_marginal_reach)
print(type(diminishing_point))
# Define the Budget that corresponds to the Diminishing Point
required_budget = dataframe.loc[dataframe['Reach_Percent'] == diminishing_point, 'Budget'].iloc[0]
print(type(required_budget))
# Define the GRP that corresponds to the Diminishing Point
required_grp = dataframe.loc[dataframe['Reach_Percent'] == diminishing_point, 'GRP'].iloc[0]

visualize()

print(f"The diminishing Point is at {diminishing_point}.")
print(f"Required Budget is {required_budget} at {required_grp} GRP.")
