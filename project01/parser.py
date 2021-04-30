"""
This module contains the shared code used to read, parse, and produce
a dataframe object using our USDA dataset.  Reviewing our dataset, we
find that there's several common columns and indices, indicating that
we could adopt an object-oriented approach, where we have a base object
and each of our data tables could expand upon.

"""

import os
import re
from typing import Any, List, Optional

import pandas as pd


class BaseFood:
    """A base object for USDA food elements.
    
    This object creates a common interface for all future USDA food table
    entries.
    """
    def __init__(self, csv_file: str = None, *args, **kwargs) -> None:
        self._df = self._parse_csv(csv_file)
        self._ingredients = None

    @staticmethod
    def _parse_csv(csv_file: str) -> pd.DataFrame:
        """Establishes a pandas dataframe of the passed CSV file

        Args:
            csv_file (str): A string representing the path of the CSV file
               to load
        Returns:
           pd.DataFrame: The CSV file loaded as a dataframe.
        """
        return pd.read_csv(csv_file, header=0, dtype=object)

    def _filter(self, col: str, val: Any) -> pd.DataFrame:
        """Returns the rows of the dataframe which have the passed value in the specified column.

        Args:
            col (str): The name of the column in the current instance's dataframe.
            val (Any): The value to seek on within the dataframe.
        Returns:
            pd.DataFrame: The subset of the dataframe which matches the above condition.
        """
        return self._df[self._df[col] == val]

    def find_by_fdcid(self, idx: int) -> pd.DataFrame:
        """Returns the record whos fdc_id matches teh passed id value.

        Args:
            idx (int): The Index ID used for the food object.
        Returns:
            pd.DataFrame: The subset of the datatframe that matches the passed ID.

        """
        return self._filter("fdc_id", idx)

    @property
    def df(self) -> pd.DataFrame:
        """Provides access to the object's dataframe
        """
        return self._df

    def run_on_df(self, func, *args, **kwargs):
        self._df = func(self._df, *args, **kwargs)
        return self._df

    def cleanup(self) -> pd.DataFrame:
        """Cleans up dataset based upon EDA analysis.

        Returns:
            pd.DataFrame: The cleaned dataframe.
        """
        raise NotImplementedError("Base cleanup method must be implemented in subclasses of object.")

    def clamp(self,
              floor: int = 0,
              ceiling: int = None,
              col: str = "corn_syrup_idx") -> pd.DataFrame:
        """Clamping function used to filter the allowed indices of a column.

        Args:
            df (pd.DataFrame): The dataframe to operate on.
            floor (int): The lowest allowed value of the column. Defaults to 0.
            ceiling (int): The highest allowed value in the column.
                Defaults to the maximum value in the column.
            col (str): The column name to operate on.  Defaults to corn_syrup_idx.

        Returns:
            pd.DataFrame: A new dataframe, where only the rows within the values
                of floor and ceiling are included, and all others are dropped.
        """
        ceil = ceiling if ceiling is not None else self._df[col].max() + 1
        self._df = self._df[(self._df[col] > floor) & (self._df[col] < ceil)]
        return self._df

    def find_top(self,
                 limit: int = 5,
                 col: str = "branded_food_category") -> pd.DataFrame:
        """Establishes the dataset for finding the largest values in the food object.

        Args:
            limit (int): The total number of records to return from the dataset.
            col (str): The column to find the top occurances of.
        Returns:
            pd.DataFrame: A filtered dataframe containing only the foods
            in the top five largest categories.
        """
        top_series = self._df[col].value_counts().nlargest(limit)
        top_names = top_series.index.array
        self._df = self._df[self._df[col].isin(top_names)]
        return self._df

    def __str__(self) -> str:
        return self._df.__str__()


class FoodObject(BaseFood):
    def __init__(self, csv_file: str = None) -> None:
        """An object implementation of the food.csv data table.

        Args:
           csv_file (str): A string that direccts to the food.csv file.
        """
        super().__init__(csv_file)

    def find_by_group(self, grp: str) -> pd.DataFrame:
        """Finds all records that match the passed group.

        Args:
            grp (str): The group name to look up in the dataframe.
        Returns:
            pd.DataFrame: A subset of the dataframe for the specified group.
        """
        return self._filter("food_category_id", grp)

    def cleanup(self):
        raise NotImplementedError("To be implemented.")


class FoodBrandObject(BaseFood):
    def __init__(self, csv_file: str = None) -> None:
        """Establishs a new FoodBrand object based on the food_brand.csv file

        Args:
            csv_file (str): A string that specifies the path of the food_brands.csv file.
        """
        super().__init__(csv_file)

    def find_by_brandowner(self, brand: str = None) -> pd.DataFrame:
        """Finds all records owned by a particular brand.

        Args:
            brand (str): The brand owner's fully named value
        Returns:
            pd.DataFrame: A subset of the data for the specified brand owner.
        """
        return self._filter("brand_owner", brand)

    def cleanup(self) -> pd.DataFrame:
        """Cleans up dataset based upon EDA analysis.

        Returns:
            pd.DataFrame: The cleaned dataframe.
        """
        self._df['modified_date'] = pd.to_datetime(self._df['modified_date'], format="%Y-%m-%d")
        self._df['available_date'] = pd.to_datetime(self._df['available_date'], format='%Y-%m-%d')
        #self._df['discontinued_date'] = pd.to_datetime(self._df['discontinued_date'], format='%Y-%m-%d')
        del self._df['discontinued_date']
        self._df.dropna(how='all')
        self._df.dropna(subset=['brand_owner', 'ingredients', 'serving_size',
                                'serving_size_unit', 'branded_food_category'], inplace=True)
        return self._df

    def get_all_ingredients(self):
        """Parses the entire ingridents series of the dataframe to establish a list of all ingredients.

        Returns:
           set: A set of the ingredients within the dataframe.
        """
        def clean(ing):
            """Performs simple splitting and parsing of an ingredients list.

            Args:
                ing (str): a string representing a product's ingriedents list.

            Returns:
                tuple: A split list of ingredients after being normalized for later processing.
            """
            # Strip paren text
            # Remove paren and bracket text
            cleaned1 = re.sub("[\(\[].*?[\)\]]", "", str(ing))
            # Remove residual punctuation, save our "comma" delimiter
            cleaned2 = re.sub(r'[#\.:\-*?!&}{][()"]', "", cleaned1)
            # Return a tuple split on the comma, removing whitespace
            pt1 = list(i.strip() for i in cleaned2.lower().split(","))
            # Split on nested semicolon list for ingredients
            pt2 = list(i.strip() for lst in pt1 for i in lst.split(";"))
            # Split on subsequent ingredients
            pt3 = list(i.strip() for lst in pt2 for i in lst.split(":"))
            # Split on "statement" ingredients
            pt4 = list(i.strip() for lst in pt3 for i in lst.split("."))
            # Return as an immutable type to make converting to a set easier
            return tuple(pt4) 
        # Unfold the list into a flattened set and then back to a list (for ease of access)
        self._ingredients = tuple(set(x.strip() for lst in self._df["ingredients"].apply(clean).tolist() for x in lst))
        return self._ingredients


def load(csv_dir: Optional[str] = "dataset") -> List[FoodObject]:
    ret = list()

    for base_dir in os.listdir(csv_dir):
        ret.append(FoodObject(os.path.join(csv_dir, base_dir, "food.csv")))
    return ret


def find_index_from_str(delimited_string: str, fnd: str, split: str = ","):
    """Finds the rank of the string fnd in the passed delimited string

    This function takes in a raw string with a known delimiter and locates
    the index position of the fnd value, identifying the rank of the item.

    Args:
        delimited_string (str): The string to operate against.
        fnd (str): The string to search for
        split (str): The delimiter to use to split the source string.
           Default: ","

    Returns:
        int: The integer value representing where the string fnd is
        positioned in an array delimited by split.
    """
    key = fnd.lower()
    lst = [x.strip().lower() for x in str(delimited_string).split(split)]
    rank = -1
    for idx in range(len(lst)):
        try:
            lst[idx].index(key)
            rank = idx+1
            break
        except ValueError:
            idx = -1  # Entry not found
            continue
    return rank



def insert_index(df: pd.DataFrame,
                            find: str,
                            col: str = "ingredients",
                            sep: str = ",") -> pd.DataFrame:
    """Augments dataframe to add a ranked index column.

    This function inspects an existing dataframe's column and
    seeks for a specified string using the logic of `find_index_from_str`

    Args:
        df (pd.DataFrame: The dataframe to operate on.
        find (str): The string to search for
        col (str): The name of the column to operate on in the dataframe.
        sep (str): The delimiter to split the column's values against.

    Returns:
        pd.DataFrame: The mutated dataframe `df` with a new column named `find`_idx
        with the index value specified.  Note that if the value is not found, the
        column's value will be less than 0.
    """
    newcol = "".join([find.replace(" ", "_").lower(), "_idx"])
    df[newcol] = df[col].apply(find_index_from_str, fnd=find, split=sep)
    return df
