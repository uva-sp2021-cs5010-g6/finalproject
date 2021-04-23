
import sys
import pandas as pd
import seaborn as sns

import project01.parser as food_parser


def establish_food_object(csv_file: str) -> food_parser.FoodBrandObject:
    df = food_parser.FoodBrandObject(csv_file)
    df.run_on_df(food_parser.insert_index, find="Corn Syrup")
    return df


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


def main(csv_file):
    bfood = establish_food_object(csv_file)
    df = find_top_five_food_categories(bfood.df)
    sns.violinplot

if __name__ == "__main__":
    brand_csv = sys.argv[1] if len(sys.argv) > 2 else "./dataset/FoodData_Central_csv_2020-10-30/branded_food.csv"
    main(csv_file=brand_csv)
