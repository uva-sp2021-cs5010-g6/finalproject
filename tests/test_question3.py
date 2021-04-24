import pytest

import os
import pandas as pd

import project01.question3 as q3


def test_cornsyrup_clamp_defaults(datadir):
    df = pd.read_csv(os.path.join(datadir, "simple.csv"), header=0)
    df_result = q3.clamp_cornsyrup(df)
    assert len(df_result) == 2
    assert isinstance(df_result, pd.DataFrame)


def test_cornsyrup_clamp_alt_column(datadir):
    df = pd.read_csv(os.path.join(datadir, "simple.csv"), header=0)
    df_result = q3.clamp_cornsyrup(df, col="id")
    assert len(df_result) == 4


def test_cornsyrup_clamp_alt_floor(datadir):
    df = pd.read_csv(os.path.join(datadir, "simple.csv"), header=0)
    df_result = q3.clamp_cornsyrup(df, floor=-5)
    assert len(df_result) == 4


def test_cornsyrup_clamp_alt_floor2(datadir):
    df = pd.read_csv(os.path.join(datadir, "simple.csv"), header=0)
    df_result = q3.clamp_cornsyrup(df, floor=-10000)
    assert len(df_result) == 6


def test_cornsyrup_clamp_alt_ceil(datadir):
    df = pd.read_csv(os.path.join(datadir, "simple.csv"), header=0)
    df_result = q3.clamp_cornsyrup(df, ceiling=25)
    assert len(df_result) == 1


def test_cornsyrup_clamp_alt_constrained(datadir):
    df = pd.read_csv(os.path.join(datadir, "simple.csv"), header=0)
    df_result = q3.clamp_cornsyrup(df, floor=-60, ceiling=25)
    assert len(df_result) == 4


def test_find_top_five_food_categories_default(datadir):
    df = pd.read_csv(os.path.join(datadir, "rating.csv"))
    df_result = q3.find_top_five_food_categories(df)
    assert len(df_result["branded_food_category"].unique()) == 5

