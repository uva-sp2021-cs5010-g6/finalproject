"""

Investigating the use of corn syrup in food products:

Exploratory Data Analysis (EDA)
&
Data Cleanup

"""
print(">>>>>>>>>>----------<<<<<<<<<<")
print("Import Operating System")
print(">>>>>>>>>>----------<<<<<<<<<<\n")


import os
from typing import Any, List, Optional
    #import operating system
print(">>>>>>>>>>----------<<<<<<<<<<")
print("Import Libraries")
print(">>>>>>>>>>----------<<<<<<<<<<\n")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate
    #import libraries

print(os.getcwd())
    #check working directory
print("\n>>>>>>>>>>----------<<<<<<<<<<")
print("Reading in Data Set")
print(">>>>>>>>>>----------<<<<<<<<<<\n")

import project01.parser as parser
    #import in the parser.py  file from the project01 folder so we can
    #instantiate Classes and call functions created within the parser.py script

branded_food = parser.BaseFood('/Users/swaroopveerabhadrappa/PycharmProjects/finalproject/dataset/FoodData_Central_csv_2020-10-30/branded_food.csv')
    #loading the data set
    #create a object  by instantiating BaseFood class, which is designed to create
    # a Data Frame out of a passed in CSV file, which in this case is "branded_food.csv"

print(">>>>>>>>>>----------<<<<<<<<<<")
print("High-level Exploration of Data Set")
print(">>>>>>>>>>----------<<<<<<<<<<\n")

branded_food.run_on_df(parser.insert_index,find="corn syrup")
    #use the branded_food_df Data Frame to call the nested function, insert_index
    #the insert_index function creates a new column with the index position of the value we're looking for
    #which in this case is 'corn syrup.' The insert_index function passes in another function when called,
    #find_index_from_str, which locates the index position of the value we're looking for

print("View first 3 rows of data\n")

print(tabulate(branded_food.df.head(3), headers='keys', tablefmt='psql'))
    #view first 3 rows of DataFrame
    #based on output, number of columns to display will need to be set

print("\n>>>>>>>>>>----------<<<<<<<<<<")
print(">>>>>>>>>>----------<<<<<<<<<<\n")

pd.set_option('display.max_columns', None)
    #use display.max_columns to print all the columns

print("View first 3 rows of data\n")
print(tabulate(branded_food.df.head(3), headers='keys', tablefmt='psql'))
    #check to see if all columns are displayed --> confirmed

print("\n>>>>>>>>>>----------<<<<<<<<<<")
print(">>>>>>>>>>----------<<<<<<<<<<\n")

print("Shape of DataFrame\n")
print(branded_food.df.shape)
    #shape attribute informs us of number of observations (rows) of data and number of
    #variables (columns) in data set:
        #498,182 rows
        #14 variables
print("/n>>>>>>>>>>----------<<<<<<<<<<")
print(">>>>>>>>>>----------<<<<<<<<<<\n")

pd.set_option('display.max_columns', None)
    #use display.max_columns to print all the columns

print("Information on DataFrame\n")
print(branded_food.df.info)
    #provides information about dataset including data types for each variable
        #date variables (modified_date, available_date, and discontinued_date variables) are
        #listed as 'object', change to datetime
    #we have a few categorical variables that need to be changed in data type

print(">>>>>>>>>>----------<<<<<<<<<<")
print(">>>>>>>>>>----------<<<<<<<<<<\n")

print("Convert date columns to datetime format\n")
branded_food.df['modified_date'] = pd.to_datetime(branded_food.df['modified_date'], infer_datetime_format='yyyy-mm-dd')
branded_food.df['available_date'] = pd.to_datetime(branded_food.df['available_date'], infer_datetime_format='yyyy-mm-dd')
branded_food.df['discontinued_date'] = pd.to_datetime(branded_food.df['discontinued_date'], infer_datetime_format='yyyy-mm-dd')

    #convert the date variables into datetime data type and use infer_datetime_format to automatically
    #have Pandas recognize the format, without having to specify a particular format

print("Data Type for each Column\n")
print(branded_food.df.dtypes)
    #confirm that date variables are now in datetime data type
        #confirmed

print(">>>>>>>>>>----------<<<<<<<<<<")
print(">>>>>>>>>>----------<<<<<<<<<<\n")

print("Summary Statistics\n")

print(branded_food.df.describe)
    #describe method provides count, mean, standard deviation, min, percentile values, and max
        #need to suppress scientific notation and set number of decimal places to 2

print("\n>>>>>>>>>>----------<<<<<<<<<<")
print(">>>>>>>>>>----------<<<<<<<<<<\n")

pd.set_option('display.float_format', lambda x: '%.2f' %x)
    #suppress scientific notation in Pandas
pd.options.display.float_format = "{:,.2f}".format
    #display float variables to two decimal places

print(branded_food.df.describe)
    #confirm that scientific notation is suppressed and number of decimal places = 2

print("\n>>>>>>>>>>----------<<<<<<<<<<")
print("Data Cleanup: Checking for Missing Values, Duplicate Records, and Outliers")
print(">>>>>>>>>>----------<<<<<<<<<<\n")

print("Missing Values in DataFrame\n")
print(branded_food.df.isnull().sum())

# print(branded_food.df.isnull().sum())
    #check DataFrame for null values in any column, and sum up the total null values
        #we observe null values in these columns: brand_owner, ingredients, serving_size
        #serving_size_unit, household_serving_fulltext, branded_food_category, and discontinued_date
    #we have the following options to deal with null values: drop from data se or
    #replace with mean/median/mode, which will be dependent on data type of variable
        #it wouldn't make sense to use mean/median with variables with data type object
        #it also wouldn't make sense to use mode with object values, nonsensical
    #one column is entirely blank, and that is discontinued_date
        #let's drop rows and columns if all values are null, and then
        #let's  drop discontinued_date column from Data Frame and then come back to missing values

del branded_food.df['discontinued_date']
    #drop discontinued_date column

print("\nColumns in DataFrame\n")

print(branded_food.df.columns)
    #check to see if discontinued_date column is dropped
        #confirmed
        #number of variables (columns) is now 13

print("\n>>>>>>>>>>----------<<<<<<<<<<")
print(">>>>>>>>>>----------<<<<<<<<<<\n")

print("Drop Missing Values\n")
print(branded_food.df.isnull().sum())
    #let's get back to missing values cleanup
    #which variables can we drop? That is, which variables will we be using for our analysis
        #these variable cannot be null, and if they are, it could lead to issues later on
    #let's drop missing values from brand_owner, ingredients, serving_size and serving_size_unit, and
    #branded_food_category

branded_food.df.dropna(how = 'all')
    #drop rows where all values are null
branded_food.df.dropna(subset = ['brand_owner', 'ingredients', 'serving_size',
                               'serving_size_unit', 'branded_food_category'], inplace=True)
    #define which columns to look for null values and then drop these values

print("\n>>>>>>>>>>----------<<<<<<<<<<")
print(">>>>>>>>>>----------<<<<<<<<<<\n")

print(branded_food.df.isnull().sum())
    #check to see if null values from specified columns have been dropped
        #confirmed
    #remaining columns with null values are household_serving_fulltext and modified_date
        #can keep these since we are not using groupby on these variables

print("\n>>>>>>>>>>----------<<<<<<<<<<")
print(">>>>>>>>>>----------<<<<<<<<<<\n")

print("Duplicate Record Check\n")
#Duplicate Records
duplicate = branded_food.df.duplicated()
    #check for duplicate recordds and create variable

print("There are " + str(duplicate.sum()) + " duplicate values")
    #zero duplicate values

print("\n>>>>>>>>>>----------<<<<<<<<<<")
print(">>>>>>>>>>----------<<<<<<<<<<\n")

#Filter DataFrame so that we only look at rows where
#ingredients contain corn syrup. Rows where ingredients
#do not contain corn syrup, the corn_syrup_idx = -1

contains_corn_syrup_df = branded_food.df[branded_food.df['corn_syrup_idx'] != -1]
    #Give bolean expression to corn_syrup_idx columnto filter
    #the corn_syrup_idx column and only show rows
    #that contain corn syrup, we want to look at all rows
    #where column is not equal to -1.

print("\nFirst 3 rows of New DataFrame, contains_corn_syrup_df, that has\n"
      "only Food Items with corn syrup\n")
print(tabulate(contains_corn_syrup_df.head(3), headers='keys', tablefmt='psql'))
    #first 3 rows of new DataFrame, contains_corn_syrup_df,

print("\nShape of new DataFrame, contains_corn_syrup_df\n")
print(contains_corn_syrup_df.shape)
    #the number of rows (or Food Items) that contains corn syrup
        #96,002 Food Items (note: this is after removing null values)

print("We have Categorical variables that need to be designated\n"
      "as such for data type\n")

contains_corn_syrup_df['brand_owner'] = contains_corn_syrup_df.brand_owner.astype('category')
contains_corn_syrup_df['serving_size_unit'] = contains_corn_syrup_df.serving_size_unit.astype('category')
contains_corn_syrup_df['branded_food_category'] = contains_corn_syrup_df.branded_food_category.astype('category')
contains_corn_syrup_df['market_country'] = contains_corn_syrup_df.market_country.astype('category')

print(contains_corn_syrup_df.dtypes)

print(">>>>>>>>>>----------<<<<<<<<<<\n")
print("Data Cleanup Completed\n"
      "DataFrame has been filtered to only\n"
      "show food items (rows) that contain "
      "corn syrup\n")
print(">>>>>>>>>>----------<<<<<<<<<<\n")

print("There are " + str(len(contains_corn_syrup_df.index)) +
      " Food items that contain corn syrup in our data set.\n"
      "DataFrame is now ready for analysis ")

print(contains_corn_syrup_df.shape)
















