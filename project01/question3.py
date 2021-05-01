"""
This module provides the functions and code in support of answering the
question "How do popular food categories fare with corn syrup?"

The `main()` function provides the pythonic driver, however this can
be run directly using python3 -m project01.question3 after the files
have been fetched from the USDA (see `project01.fetcher`).
"""

import sys
import numpy as np
import pandas as pd
import seaborn as sns

from matplotlib import pyplot as plt
from typing import List

import project01.parser as food_parser


def establish_food_object(csv_file: str) -> food_parser.FoodBrandObject:
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
    bfood.run_on_df(food_parser.insert_index, find="corn syrup")
    bfood.run_on_df(food_parser.insert_index, find="sugar")
    return bfood


def clamp(bfood: food_parser.BaseFood,
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


def find_top_five_food_categories(bfood: food_parser.BaseFood,
                                  col: str = "branded_food_category") -> pd.DataFrame:
    """Establishes the dataset for top5 food categories

    Args:
        bfood (food_parser.BaseFood): The dataframe to seek against.
        col (str): The column to find the top occurrences of.
    Returns:
        pd.DataFrame: A filtered dataframe containing only the foods
        in the top five largest categories.
    """
    return bfood.find_top(col=col, limit=5)


def metrics_on_food_categories(df: pd.DataFrame,
                               col: str = "branded_food_category") -> List[pd.Series]:
    """Produces simple analysis on a specific column in a dataframe

    Args:
        df (pd.DataFrame): The dataframe to operate on.
        col (str): The column to perform analysis on.  Default: branded_food_category.

    Returns:
        list[pd.Series]: The output of describe() and value_counts() on the dataframe's series.
    """
    return [df[col].describe(), df[col].value_counts()]


def plot_foodcat(df: pd.DataFrame, col="corn_syrup_idx", out: str = "plot.png"):
    """Creates a violin plot of the distribution of data.

    Args:
        df (pd.DataFrame): The dataframe to use when plotting.
        col (str): The column to use for the violinplot magnitude.
        out (str): The path to save the plotting graphic to.

    Returns:
        None: The graphic is saved to `out` as a side effect.
    """
    # Note, we need to establish the figure to ensure sns doesn't
    # try to add to its prior plot.
    fig, ax1 = plt.subplots(figsize=(12, 6))
    sns.violinplot(x=col,
                   y="branded_food_category",
                   orient="h",
                   bw=0.2,
                   cut=0,
                   scale="width",
                   data=df, ax=ax1)
    ax1.set(xlabel="Rank",
            ylabel="Food Category")
    # Calling plt.tight_layout() ensures our labels fit in our
    # plotting space.
    plt.tight_layout()
    fig.savefig(out)


def density(bfood: food_parser.BaseFood, out: str = ""):
    newdf = pd.DataFrame({"brand": bfood.df["branded_food_category"],
                          "sugar": bfood.df["sugar_idx"],
                          "corn_syrup": bfood.df["corn_syrup_idx"]})
    # Insert NaNs for no matches to ensure our counts aren't skewed.
    newdf.loc[newdf["sugar"] == -1, "sugar"] = np.NaN
    newdf.loc[newdf["corn_syrup"] == -1, "corn_syrup"] = np.NaN
    fig, ax1 = plt.subplots(figsize=(12, 6))
    sns.histplot(element="step", bins=30, ax=ax1, data=newdf)
    ax1.set(xlabel="Index",
            ylabel="Count")
    # Calling plt.tight_layout() ensures our labels fit in our
    # plotting space.
    plt.tight_layout()
    fig.savefig(out)


def correlation(bfood: food_parser.BaseFood, out: str = "q3-correlation.png"):
    newdf = pd.DataFrame({"category": bfood.df["branded_food_category"],
                          "sugar": bfood.df["sugar_idx"],
                          "corn_syrup": bfood.df["corn_syrup_idx"]})
    # Insert NaNs for no matches to ensure our counts aren't skewed.
    newdf.loc[newdf["sugar"] == -1, "sugar"] = np.NaN
    newdf.loc[newdf["corn_syrup"] == -1, "corn_syrup"] = np.NaN
    myfig = sns.pairplot(data=newdf, hue="category", markers="|", kind="reg")
    myfig.savefig(out)


def main(csv_file: str):
    """Pythonic driver for our third question / query

    This method:
      1. Establishes our food object of interest
      2. Outputs trivial summary statistics on a column
      3. Establishes a subset to the top five food categories
      4. Outputs metrics on the subset.
      5. Establishes another subset from the dataframe by limiting
         the data to only values that have corn syrup
      6. Produces a violin plot to show our data density across the
         top five groups.  We see a large left tail.
      7. After reviewing the data, the corn_syrup_idx ceiling appears
         to be near ten, so we further clamp the data down to center
         our distribution.

    Args:
        csv_file (str): The path to the branded_foods.csv file.

    Returns:
        None: Output to the terminal statistics and various
        plots are written out to file.
    """
    bfood = establish_food_object(csv_file)
    df = find_top_five_food_categories(bfood)
    metrics_on_food_categories(bfood.df)
    # Very wide range, adjusted to 10 as this seems to match most index returns.
    df_cornsyrup = clamp(bfood)
    plot_foodcat(df_cornsyrup, out="q3-cornsyrup-cat.png")
    df_sugar = clamp(bfood, col="sugar_idx")
    plot_foodcat(df_sugar, out="q3-sugar.png")
    density(bfood, out="q3-density.png")
    correlation(bfood, out="q3-correlation.png")
    

if __name__ == "__main__":
    brand_csv = sys.argv[1] if len(sys.argv) > 2 else "./dataset/FoodData_Central_csv_2020-10-30/branded_food.csv"
    main(csv_file=brand_csv)
