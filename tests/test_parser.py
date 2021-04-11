import pytest

import os
import project01.parser as parser


def test_insert_index(datadir):
    print(datadir)
    bfood = parser.FoodBrandObject(datadir.join("branded_food.csv"))
    bfood.run_on_df(parser.insert_index, "flour", "ingredients")
    print(bfood.df)


def test_find_index_from_str():
    pass
