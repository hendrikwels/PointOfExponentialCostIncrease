import pandas as pd


def calculate_diminishing_point(dataframe, marginal_product):
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
            # If the next point is not achieving 1% increment vs current point, we have found the Diminishing Point
            # TODO: check if the first condition is necessary
            if index + 1 < len(marginal_product) and point >= (marginal_product[index + 1] * 1.01):
                # Convert the current Point into corresponding Reach using the index
                inflection_point = dataframe.iloc[index, 1]  # .iloc[0] returns a NoneType
                return inflection_point

    except KeyError:
        pass
