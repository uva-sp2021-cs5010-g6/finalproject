"""
This module provides the functions and code in support of answering the
question "How do solid food items (grams) and liquid item (ml) fare with corn syrup?"

The `main()` function provides the pythonic driver, however this can
be run directly using python3 -m project01.question4 after the files
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


def establish_food_object_sugar(csv_file: str) -> food_parser.FoodBrandObject:
    """Creates our food object leveraging our general purpose parser.

    Args:
        csv_file (str): The path to the food brand CSV file.

    Returns:
        food_parser.FoodBrandObject: A general purpose brand object which
            contains the parsed dataframe with sugar already added as
            a new index.
    """
    bfood = food_parser.FoodBrandObject(csv_file)
    bfood.cleanup()
    sugar = bfood.run_on_df(food_parser.insert_index, "sugar", "ingredients")
    return sugar


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
                      data=df).set(title="Serving Size: Corn Syrup")
    fig.savefig(out)


def plot_sugar(df: pd.DataFrame, out: str = "plot.png"):
    """Creates a catplot of the data.

    Args:
        df (pd.DataFrame): The dataframe to use when plotting.
        out (str): The path to save the plotting graphic to.

    Returns:
        None: The graphic is saved to `out` as a side effect.
    """
    fig = sns.catplot(x="serving_size_unit",
                      y="sugar_idx",
                      data=df).set(title="Serving Size: Sugar")
    fig.savefig(out)


def main(csv_file: str):
    """Pythonic driver for our fourth question / query

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
    plot_cornsyrup(cornsyrup, out="q4-cornsyrup.png")

    sugar = establish_food_object_sugar(csv_file)
    plot_sugar(sugar, out="q4-sugar.png")


if __name__ == "__main__":
    brand_csv = sys.argv[1] if len(sys.argv) > 2 else "../dataset/FoodData_Central_csv_2020-10-30/branded_food.csv"
    main(csv_file=brand_csv)
