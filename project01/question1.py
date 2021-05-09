"""
This module provides the functions and code in support of differentiating
between distribution of corn syrup and high fructose corn syrup
in food products.

The `main()` function provides the pythonic driver, however this can
be run directly using python3 -m project01.question1 after the files
have been fetched from the USDA (see `project01.fetcher`).
"""

import sys
import pandas as pd
import seaborn as sns

import project01.parser as food_parser


def establish_food_object_cornsyrup(csv_file: str) -> food_parser.FoodBrandObject:
    """Creates our food object leveraging our general purpose parser.

    Args:
        csv_file (str): The path to the food brand CSV file.

    Returns:
        food_parser.FoodBrandObject: A general purpose brand object which
            contains the parsed dataframe with corn syrup already added as
            a new index.
    """
    bfood = food_parser.FoodBrandObject(csv_file)
    bfood.cleanup()
    cornsyrup = bfood.run_on_df(food_parser.insert_index, "corn syrup", "ingredients")
    return cornsyrup


def establish_food_object_hfcs(csv_file: str) -> food_parser.FoodBrandObject:
    """Creates our food object leveraging our general purpose parser.

    Args:
        csv_file (str): The path to the food brand CSV file.

    Returns:
        food_parser.FoodBrandObject: A general purpose brand object which
            contains the parsed dataframe with high fructose corn syrup
            already added as
            a new index.
    """
    bfood = food_parser.FoodBrandObject(csv_file)
    bfood.cleanup()
    hfcs = bfood.run_on_df(food_parser.insert_index, "high fructose corn syrup", "ingredients")
    return hfcs


def clamp_cornsyrup(bfood: food_parser.BaseFood,
                    floor: int = 0,
                    ceiling: int = None,
                    col: str = "corn_syrup_idx") -> pd.DataFrame:
    """Clamping function used to filter the allowed indices of a column.

    Args:
        bfood (food_parser.BaseFood): The dataframe to operate on.
        floor (int): The lowest allowed value of the column. Defaults to 0.
        ceiling (int): The highest allowed value in the column.
            Defaults to the maximum value in the column.
        col (str): The column name to operate on.  Defaults to corn_syrup_idx.

    Returns:
        pd.DataFrame: A new dataframe, where only the rows within the values
            of floor and ceiling are included, and all others are dropped.
    """
    return bfood.clamp(floor=floor, ceiling=ceiling, col=col)


def clamp_hfcs(bfood: food_parser.BaseFood,
                    floor: int = 0,
                    ceiling: int = None,
                    col: str = "high_fructose_corn_syrup_idx") -> pd.DataFrame:
    """Clamping function used to filter the allowed indices of a column.

    Args:
        bfood (food_parser.BaseFood): The dataframe to operate on.
        floor (int): The lowest allowed value of the column. Defaults to 0.
        ceiling (int): The highest allowed value in the column.
            Defaults to the maximum value in the column.
        col (str): The column name to operate on.  Defaults to sugar_idx.

    Returns:
        pd.DataFrame: A new dataframe, where only the rows within the values
            of floor and ceiling are included, and all others are dropped.
    """
    return bfood.clamp(floor=floor, ceiling=ceiling, col=col)


def plot_cornsyrup(df: pd.DataFrame, out: str = "plot.png"):
    """Creates a catplot of the data.

    Args:
        df (pd.DataFrame): The dataframe to use when plotting.
        out (str): The path to save the plotting graphic to.

    Returns:
        None: The graphic is saved to `out` as a side effect.
    """
    fig = sns.catplot(x="serving_size_unit",
                      y="corn_syrup_idx",
                      data=df).set(title="Distribution of Corn Syrup in Food Products: Solid (g) vs. Liquid (ml)")
    fig.savefig(out)


def plot_hfcs(df: pd.DataFrame, out: str = "plot.png"):
    """Creates a catplot of the data.

    Args:
        df (pd.DataFrame): The dataframe to use when plotting.
        out (str): The path to save the plotting graphic to.

    Returns:
        None: The graphic is saved to `out` as a side effect.
    """
    fig = sns.catplot(x="serving_size_unit",
                      y="high_fructose_corn_syrup_idx",
                      data=df).set(title="Distribution of High Fructose Corn Syrup in Food Products: Solid (g) vs. Liquid (ml)")
    fig.savefig(out)


def main(csv_file: str):
    """Pythonic driver for our first question / query

    This method:
      1. Establishes our food object of interest
      2. Establishes subset from the dataframe by limiting
         the data to only values that have corn syrup
      3. Produces a catplot to compare solid and liquid food item's data

    Args:
        csv_file (str): The path to the branded_foods.csv file.

    Returns:
        None: catplot is written out to file.
    """
    cornsyrup = establish_food_object_cornsyrup(csv_file)
    plot_cornsyrup(cornsyrup, out="q1-cornsyrup.png")

    hfcs = establish_food_object_hfcs(csv_file)
    plot_hfcs(hfcs, out="q1-hfcs.png")


if __name__ == "__main__":
    brand_csv = sys.argv[1] if len(sys.argv) > 2 else "./dataset/FoodData_Central_csv_2020-10-30/branded_food.csv"
    main(csv_file=brand_csv)
