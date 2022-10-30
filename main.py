
from typing import Any
import pandas as pd
from pandas import DataFrame
from pandas.io.parsers import TextFileReader
from scipy.signal import savgol_filter
from curveData import create_reach_data
import curveData
from exponentialPoint import calculate_exponential_point
from visualChart import visualize


# Read CSV File
dataframe: TextFileReader | DataFrame | Any = pd.read_csv(create_reach_data())

# Rename Columns

dataframe.rename(columns={"Budget": "Budget",
                          "Reach": "Reach_Percent",
                          "GRP": "GRP",
                          "CostPerReachPoint": "CPR"}, inplace=True)

# Define Change in Budget and Reach to calculate Marginal Reach
budget_change = dataframe.Budget.diff()
reach_change = dataframe.Reach_Percent.diff()
marginal_reach = reach_change / budget_change
marginal_reach_cost = budget_change / reach_change
cost_per_reach_point = dataframe.CPR
smooth_marginal_reach = savgol_filter(marginal_reach, 51, 3)

# Append marginal reach & smooth marginal reach to Dataframe
dataframe["marginal_reach"] = marginal_reach
dataframe["smooth_marginal_reach"] = smooth_marginal_reach
dataframe["marginal_reach_cost"] = marginal_reach_cost

# Turn Reach_Percent, marginal_reach and smooth_marginal_reach into a float with 2 decimal places and multiply by 100
dataframe["Reach_Percent"] = dataframe["Reach_Percent"].apply(lambda x: round(x, 4) * 100)
dataframe["marginal_reach"] = dataframe["marginal_reach"].apply(lambda x: round(x, 4) * 100)
dataframe["smooth_marginal_reach"] = dataframe["smooth_marginal_reach"].apply(lambda x: round(x, 4) * 10000)
# Turn Budget into 1000 EUR
dataframe["Budget"] = dataframe["Budget"].apply(lambda x: round(x / 1000, 2))

# display the dataframe to check for errors / nan Values
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(dataframe.head())


# Giving the User Output on the Diminishing Point and visualizing the Reach Curve
# Define the Diminishing Point
exponential_point = calculate_exponential_point(dataframe, cost_per_reach_point)

# Define the Budget that corresponds to the Diminishing Point
required_budget = dataframe.loc[dataframe['Reach_Percent'] == exponential_point, 'Budget'].iloc[0]

# Define the GRP that corresponds to the Diminishing Point
required_grp = dataframe.loc[dataframe['Reach_Percent'] == exponential_point, 'GRP'].iloc[0]

# Visualize the Reach Curve and the Marginal Reach Curve
visualize(dataframe, cost_per_reach_point)

# Print the Diminishing Point and the Budget that corresponds to the Diminishing Point to Console
print(f"The exponential Point is at {exponential_point}.")
print(f"Required Budget is {required_budget}M€ at {required_grp} GRP.")
