
import os
from typing import Any, List, Optional

import pandas as pd

def load(csv_dir: Optional[str] = "dataset") -> List[pd.DataFrame]:
    ret = list()

    for base_dir in os.listdir(csv_dir):
        ret.append(FoodObject(os.path.join(csv_dir, base_dir, "food.csv")))
    return ret


class BaseFood():
    """A base object for USDA food elements.
    
    This object creates a common interface for all future USDA food table
    entries.
    """
    def __init__(self, csv_file: str = None) -> None:
        self._df = self._parse_csv(csv_file)

    def _parse_csv(self, csv_file: str) -> pd.DataFrame:
        """Establishes a pandas dataframe of the passed CSV file

        Args:
            csv_file (str): A string representing the path of the CSV file
               to load
        Returns:
           pd.DataFrame: The CSV file loaded as a dataframe.
        """
        return pd.read_csv(csv_file, header=0)

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
    
    def __str__(self) -> str:
        self._df.__str__()

class FoodObject(BaseFood):
    def __init__(self, csv_file: str=None) -> None:
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

class FoodBrandObject(BaseFood) -> pd.DataFrame:
    def __init__(self, csv_file: str = None) -> None:
        """Establishs a new FoodBrand object based on the food_brand.csv file

        Args:
            csv_file (str): A string that specifies the path of the food_brands.csv file.
        """
        super().__init__(csv_file)

    def find_by_brandowner(self, brand: str=None) -> pd.DataFrame:
        """Finds all records owned by a particular brand.

        Args:
            brand (str): The brand owner's fully named value
        Returns:
            pd.DataFrame: A subset of the data for the specified brand owner.
        """
        return self._filter("brand_owner", brand)

    @staticmethod
    def index_ingredients(ingredient_list: list[str], find: str) -> List[str]:
        ingredients = ingredient_list if isinstance(ingredient_list, list) else [ingredient_list]
        for row, data in ingredients.items():
    ...:     print("{}: {}".format(row, data.lower().split(",")))
        lst = list()
        lst = listing.split(",")
