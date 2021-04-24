import pytest

import os
import pandas as pd

import project01.parser as parser


def test_food_object_inheritance():
    fb_object = parser.FoodBrandObject(datadir.join("branded_food.csv"))
    assert issubclass(fb_object, parser.BaseFood)


def test_insert_index_col(datadir):
    bfood = parser.BaseFood(datadir.join("branded_food.csv"))
    bfood.run_on_df(parser.insert_index, "salt", "ingredients")
    assert "salt_idx" in bfood.df


def test_find_index_from_str(datadir):
    bfood = parser.BaseFood(datadir.join("branded_food.csv"))
    bfood.run_on_df(parser.insert_index, "salt", "ingredients")
    assert bfood.df["salt_idx"].equals(pd.DataFrame({"salt_idx": [3, 3, -1, 15]})["salt_idx"])


def test_clamp(datadir):
    bfood = parser.BaseFood(datadir.join("simple.csv"))
    bfood.df["corn_syrup_idx"] = pd.to_numeric(bfood.df["corn_syrup_idx"])
    bfood.clamp()
    assert len(bfood.df) == 2


def test_cornsyrup_clamp_defaults(datadir):
    bfood = parser.BaseFood(datadir.join("simple.csv"))
    bfood.df["corn_syrup_idx"] = pd.to_numeric(bfood.df["corn_syrup_idx"])
    ret = bfood.clamp()
    assert len(bfood.df) == 2
    assert isinstance(ret, pd.DataFrame)
    assert bfood.df.equals(ret)


def test_cornsyrup_clamp_returntype(datadir):
    bfood = parser.BaseFood(datadir.join("simple.csv"))
    bfood.df["corn_syrup_idx"] = pd.to_numeric(bfood.df["corn_syrup_idx"])
    ret = bfood.clamp()
    assert isinstance(ret, pd.DataFrame)


def test_cornsyrup_clamp_mutates_df(datadir):
    bfood = parser.BaseFood(datadir.join("simple.csv"))
    bfood.df["corn_syrup_idx"] = pd.to_numeric(bfood.df["corn_syrup_idx"])
    ret = bfood.clamp()
    assert bfood.df.equals(ret)


def test_cornsyrup_clamp_alt_column(datadir):
    bfood = parser.BaseFood(datadir.join("simple.csv"))
    bfood.df["corn_syrup_idx"] = pd.to_numeric(bfood.df["corn_syrup_idx"])
    ret = bfood.clamp(col="id")
    assert len(bfood.df) == 4


def test_cornsyrup_clamp_alt_floor(datadir):
    bfood = parser.BaseFood(datadir.join("simple.csv"))
    bfood.df["corn_syrup_idx"] = pd.to_numeric(bfood.df["corn_syrup_idx"])
    ret = bfood.clamp(floor=-5)
    assert len(bfood.df) == 4


def test_cornsyrup_clamp_alt_floor2(datadir):
    bfood = parser.BaseFood(datadir.join("simple.csv"))
    bfood.df["corn_syrup_idx"] = pd.to_numeric(bfood.df["corn_syrup_idx"])
    ret = bfood.clamp(floor=-10000)
    assert len(bfood.df) == 6


def test_cornsyrup_clamp_alt_ceil(datadir):
    bfood = parser.BaseFood(datadir.join("simple.csv"))
    bfood.df["corn_syrup_idx"] = pd.to_numeric(bfood.df["corn_syrup_idx"])
    ret = bfood.clamp(ceiling=25)
    assert len(bfood.df) == 1


def test_cornsyrup_clamp_alt_constrained(datadir):
    bfood = parser.BaseFood(datadir.join("simple.csv"))
    bfood.df["corn_syrup_idx"] = pd.to_numeric(bfood.df["corn_syrup_idx"])
    df_result = bfood.clamp(floor=-60, ceiling=25)
    assert len(bfood.df) == 4


def test_find_top_default(datadir):
    bfood = parser.BaseFood(datadir.join("rating.csv"))
    df_result = bfood.find_top()
    assert len(df_result["branded_food_category"].unique()) == 5


def test_find_top_specified_amount(datadir):
    bfood = parser.BaseFood(datadir.join("rating.csv"))
    df_result = bfood.find_top(limit=7)
    assert len(df_result["branded_food_category"].unique()) == 7


def test_find_top_specified_col(datadir):
    bfood = parser.BaseFood(datadir.join("rating.csv"))
    df_result = bfood.find_top(col="alt_category")
    assert len(df_result["alt_category"].unique()) == 5


def test_find_top_specified_limit_and_col(datadir):
    bfood = parser.BaseFood(datadir.join("rating.csv"))
    df_result = bfood.find_top(col="alt_category", limit=3)
    assert len(df_result["alt_category"].unique()) == 3
