import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import curveData
from diminishPoint import calculate_diminishing_point


def visualize(dataframe, marginal_reach):
    """
    Visualize the Reach Curve and the Marginal Reach Curve
    :param dataframe: The Dataframe containing the Reach Curve, that was created with curveData.py
    :param marginal_reach: The marginal product/reach curve that is neccessary for the  diminish_point variable and
    used as secondary Curve
    :return: Matplotlib Plot
    """
    # Create Figure and Axes to plot data and label Axes
    fig, ax = plt.subplots(figsize=(10, 6), constrained_layout=True)

    x = dataframe["Budget"]
    y = dataframe["Reach_Percent"]
    diminish_point = calculate_diminishing_point(dataframe, marginal_reach)

    # Set Diagram Labels
    ax.set_xlabel('Budget M EUR')
    ax.set_ylabel('Reach %')

    # Aesthetics:

    # Set X Ticks to a slight rotation
    plt.xticks(rotation=45)
    # Set Y Ticks to 10% increments
    plt.yticks(np.arange(0, 100, 10))
    # Set Y Axis to start at 0
    plt.ylim(0, 100)

    # Change Font to Arial
    plt.rcParams['font.family'] = 'Helvetica'

    # Display Text Box with Diminishing Point, Target Group, Buying Target Group, Country
    text = f"Target Group: {curveData.core_target_group}\n" + \
           f"Buying Target Group: {curveData.buying_target_group}\n" \
           f"Country: {curveData.country}\n" \
           f"Diminishing Point: {diminish_point}%"
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    ax.text(0.05, 0.95, text,
            transform=ax.transAxes, fontsize=11,
            verticalalignment='top', bbox=props)

    # plot the final Plot
    plt.plot(x, y) # Todo: Add a Legend with Color Coding

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
    ax2.set_ylabel('Marginal Reach Cost LOG')
    ax2.plot(x, dataframe["marginal_reach_cost"], color='green')
    # Transform marginal reach cost to an exponential curve
    ax2.set_yscale('log')

    plt.show()
