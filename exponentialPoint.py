import pandas as pd


def calculate_exponential_point(dataframe, marginal_product):
    """
    Calculate the Diminishing Point of a given DataFrame
    :param dataframe: The CSV Dataframe File to locate with Pandas
    :param marginal_product: The Column of Marginal Reach (smooth or unsmooth)
    :return: The inflection Point / the Point of Diminishing Returns
    """

    try:
        for index, point in enumerate(marginal_product):
            if index == len(marginal_product) - 1:  # If we are at the end of the list, break
                break
            # If the next point is at least twice as high as the first entry in marginal_product
            if marginal_product[index + 1] >= 2 * marginal_product[0]:
                # Return the current point
                return dataframe.iloc[index].Reach_Percent
    except ValueError:
        print("The DataFrame is empty. Please check the CSV File.")
        return 0
