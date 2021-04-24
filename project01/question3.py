
import sys
import pandas as pd
import seaborn as sns

from matplotlib import pyplot as plt

import project01.parser as food_parser


def establish_food_object(csv_file: str) -> food_parser.FoodBrandObject:
    bfood = food_parser.FoodBrandObject(csv_file)
    bfood.run_on_df(food_parser.insert_index, find="corn syrup")
    return bfood


def clamp_cornsyrup(df, floor=0, ceiling=None):
    ceil = ceiling if ceiling is not None else df["corn_syrup_idx"].max()
    d = df[(df["corn_syrup_idx"] > floor) & (df["corn_syrup_idx"] < ceil)]
    return d


def find_top_five_food_categories(df: pd.DataFrame,
                                  col: str = "branded_food_category") -> pd.DataFrame:
    """Establishes the dataset for top5 food categories

    Args:
        df (pd.DataFrame): The dataframe to seek against.
        col (str): The column to find the top occurances of.
    Returns:
        pd.DataFrame: A filtered dataframe containing only the foods
        in the top five largest categories.
    """
    top5_series = df[col].value_counts().nlargest(5)
    top5_names = top5_series.index.array
    return df[df[col].isin(top5_names)]


def correlate_food_category_by_brand(df: pd.DataFrame) -> pd.DataFrame:
    pass


def plot(df, out="plot.png"):
    fig, ax1 = plt.subplots(figsize=(12,6))
    ax_sns = sns.violinplot(x="corn_syrup_idx",
                            y="branded_food_category",
                            orient="h",
                            data=df, ax=ax1)
    ax1.set(xlabel="Rank",
            ylabel="Food Category")
    plt.tight_layout()
    fig.savefig(out)


def main(csv_file):
    bfood = establish_food_object(csv_file)
    df = find_top_five_food_categories(bfood.df)
    df_cornsyrup_nomax = clamp_cornsyrup(df)
    plot(df_cornsyrup_nomax, out="q3-unbound.png")
    df_cornsyrup_10max = clamp_cornsyrup(df, ceiling=10)
    plot(df_cornsyrup_10max, out="q3-10max.png")


if __name__ == "__main__":
    brand_csv = sys.argv[1] if len(sys.argv) > 2 else "./dataset/FoodData_Central_csv_2020-10-30/branded_food.csv"
    main(csv_file=brand_csv)
