import pytest

import os
import pandas as pd

import project01.parser as parser


def test_insert_index_col(datadir):
    bfood = parser.FoodBrandObject(datadir.join("branded_food.csv"))
    bfood.run_on_df(parser.insert_index, "salt", "ingredients")
    assert "salt_idx" in bfood.df

def test_find_index_from_str(datadir):
    bfood = parser.FoodBrandObject(datadir.join("branded_food.csv"))
    bfood.run_on_df(parser.insert_index, "salt", "ingredients")
    assert bfood.df["salt_idx"].equals(pd.DataFrame({"salt_idx": [3, 3, -1, 15]})["salt_idx"])
