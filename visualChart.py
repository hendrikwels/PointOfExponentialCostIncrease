import matplotlib.pyplot as plt
import numpy as np
import curveData
from exponentialPoint import calculate_exponential_point


def visualize(dataframe, marginal_reach):
    """
    Visualize the Reach Curve and the Marginal Reach Curve
    :param dataframe: The Dataframe containing the Reach Curve, that was created with curveData.py
    :param marginal_reach: The marginal product/reach curve that is necessary for the  exponential_point variable and
    used as secondary Curve
    :return: Matplotlib Plot
    """
    # Create Figure and Axes to plot data and label Axes
    fig, ax = plt.subplots(figsize=(10, 6), constrained_layout=True)

    x = dataframe["Budget"]
    y = dataframe["Reach_Percent"]

    # marginal_parameter is marginal_reach_cost from the Dataframe in main.py
    exponential_point = calculate_exponential_point(dataframe, marginal_reach)
    target_grp = dataframe.loc[dataframe['Reach_Percent'] == exponential_point, 'GRP'].iloc[0]
    budget = dataframe["Budget"] # Declare Budget Variable so we don't need to import

    # Set Diagram Labels
    ax.set_xlabel('Budget M EUR')
    ax.set_ylabel('Reach Percent')


    # Set X Ticks to a slight rotation
    plt.xticks(rotation=45)

    # Change Font to Arial
    plt.rcParams['font.family'] = 'Helvetica'

    # Display Text Box with Diminishing Point, Target Group, Buying Target Group, Country
    text = f"Target Group: {curveData.core_target_group}\n" + \
           f"Buying Target Group: {curveData.buying_target_group}\n" \
           f"Country: {curveData.country}\n" \
           f"Exponential Point: {round(exponential_point, 2)}%\n" \
           f"Target GRP: {target_grp}\n"
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    ax.text(0.05, 0.95, text,
            transform=ax.transAxes, fontsize=9,
            verticalalignment='top', bbox=props)

    # plot the final Plot
    plt.plot(x, y)

    # Second Axis for Reach
    ax2 = ax.twinx()
    ax2.set_ylabel('Marginal Reach Cost EUR')
    ax2.plot(x, dataframe["marginal_reach_cost"], color="red", label="Marginal Reach Cost EUR")


    # Build Lines to highlight the Exponential Point

    # Determine the horizontal length of the line by finding the index of the Exponential Point
    horizontal_length = dataframe.loc[dataframe['Reach_Percent'] == exponential_point, 'Budget']

    # Determine the vertical length of the line by finding the index of the Exponential Point
    vertical_length = dataframe.loc[dataframe['Reach_Percent'] == exponential_point, 'Reach_Percent']

    # Plot the line
    ax.plot([horizontal_length, horizontal_length], [0, vertical_length], color="red", linestyle="--", label="Exponential Point")

    # Plot the line
    ax.plot([0, horizontal_length], [vertical_length, vertical_length], color="red", linestyle="--", label="Exponential Point")



    # Add a Legend for Reach Curve, Marginal Reach Cost and Diminishing Point
    ax.legend(['Marginal Reach Cost', 'Exponential Point'], loc='right')

    # New comment for Git

    plt.show()
