# Semester Project: How much corn syrup and sugar are brands using in today's products? 

Session 1 Team 6

* Nitika Kataria (NK3RF) - <nk3rf@virginia.edu>
* Robert Knuuti (UQQ5ZZ) - <uqq5zz@virginia.edu>
* Swaroop Veerabhadrappa (SBV5DN) - <sbv5dn@virginia.edu>

School of Data Science, University of Virginia

* CS 5010: Programming and Systems for Data Science - Dr. Judy Fox

* May 9th, 2021

# Main Body

## Introduction

Food and beverage companies have a direct influence on our health with the way they assemble ingredients and compose our food. The sheer number of products, brands, and food categories that are available in today’s grocery stores is astounding. The recipes, or unique combinations of ingredients, within these products have evolved over time to include new ingredients, some that are naturally occurring and others that are either partly or wholly engineered. As recipes have evolved, so has the average consumers’ taste preferences for food  and beverage products . In spite of this evolutionary aspect of food and beverage products and consumer taste preferences, one element has remained the same. There continues to be five unique flavor profiles, according to Le Cordon Bleu. These are “sweetness,” “saltiness,” “bitterness,” “sourness,” and “umami.” 

The creativity and ingenuity by manufacturers in assembling ingredients to target one or more of the five flavor profiles has generated the concern that many of these ingredients are potentially harmful when consumed, even in small quantities. One particular concern that's been in the front of many health-conscious individuals is the prolific usage of corn syrup in big brand companies.  To learn more about the prevalence of corn syrup in food and beverage products, we created this report to identify which companies produce the most products that include corn syrup and perform analysis on the results of brands that use corn syrup, establishing a ranking based on their usage of corn syrup in their ingredients list. In addition to examining  presence of corn syrup in food and beverage products, we will be including  the ingredient ‘sugar’ within the scope of our primary analysis and the ingredient ‘high fructose corn syrup’ as part of a secondary analysis, with potential for expanded analysis in the future. We will investigate the usage of ‘corn syrup’, ‘sugar’ and ‘high fructose corn syrup’ since these ingredients are often associated in trying to trigger the “sweetness” flavor profile. 

## Research

According to the Food and Drug Administration (FDA), the three ingredients we are investigating (corn syrup, sugar, and high fructose corn syrup) are chemically connected to one another. Sugar (or sucrose), perhaps the most prevalent of sweeteners, is made up of two simple sugars: glucose and fructose. Then there’s corn syrup, the byproduct of corn starch broken into individual glucose molecules. Corn starch, which is essentially a chain of glucose molecules, breaks down into individual glucose molecules with an end-product that results in the creation of high fructose corn syrup (HFCS). HFCS is created when enzymes are added to corn syrup to convert glucose to fructose, another simple sugar. Corn syrup, as noted above, is essentially 100% glucose whereas HFCS is high in fructose. The exact split between glucose and fructose in HFCS is either 42 or 55 percent fructose, with the remaining percentage attributable to water content and glucose. 

Regardless of whether we’re focusing on corn syrup, sugar, or HFCS  -- insights gleaned from FDA articles suggest that all sugar, especially added sugars, are detrimental to our health. The evolution of ingredients in the “sweetener” flavor profile has resulted in questions being asked about the safety of these ingredients. This is  a focus of the FDA, as it studies how human beings metabolize fructose vs. other simple sugars (e.g., glucose).


## The Data

The collected data has been curated by the United States Department of Agriculture (USDA) that is sampled yearly (and may have an update issued within the year) of the currently approved food items for sale in the United States stores.  This agency provides an authoritative set of information independent of manufacturers and the sellers, providing unbiased information source to perform this analysis.

This data is represented in two formats (Microsoft Access and CSV).  The CSV is an export of the Access database tables, and will be used in this project.  The USDA has produced a data dictionary demonstrating how the CSV file elements link between each table, allowing for cross-table analysis from the export.  For our analysis, we will be leveraging the CSV formatted files.  These can be obtained directly from [USDA](https://fdc.nal.usda.gov/download-datasets.html) .

Performing this analysis will require the investigation of the branded_food.csv file and its associated references as described in the USDA data dictionary PDF.  This table will require transformation as the listing of ingredients is a single data cell that will need to be split to inventory what ingredients are used in the branded product.  According to the dictionary, the listing of ingredients is exactly the same as they are listed on the product in stores.  The general ruling on ingredient listings is that the earlier an ingredient is in the list, the more significant the ingredient is in the final product (indicating that more is used).



### Exploratory Data Analysis (EDA)

We performed exploratory data analysis, or EDA, on our data set to fully understand the data we would be analyzing and to identify any potential data cleansing requirements. 

1.	The shape of the branded_foods.csv file from October 2020 is 498,182 rows and 13 columns. 
2.	There are multiple date/time columns that needed to be converted to datetime objects, categorical variables that needed to be designated as such, and missing values that needed to be addressed.
3.	96,002 rows (or products) that contain corn syrup

* 6,126 unique brands
* 56,928 unique ingredients
* 185 food categories
* Bimodal distribution of index values at positions 0 and 2
* Mean index value = 9
* Median = 5
5. 246,773 rows (or products) that contain sugar
* 17,782 unique brands
* 156,310 unique ingredients
* 218 food categories
* Bimodal distribution of index values at positions 0 and 2

### Data Cleansing

1.	The three date columns (available, modified, discontinued) were converted into pandas datetime objects. 
2.	Four columns that needed to be declared as categorical type:
* Brand_owner
* Brand_food_category
* Serving_size_unit
* Market_country
3. We checked for missing values, duplicate records, and outliers. 

   1. For missing values, we noted that the entire discontinued_date column contained null values, so we removed this column. Additionally, there were missing values in the ingredients, serving_size, serving_size_unit, household_serving_fulltext, branded_food_category, and modified_date columns. We removed the rows in which the corresponding values in the columns were empty, with the exception of household_serving_fulltext and modified_date columns. We kept the missing values in these two columns since the missing values would have no impact on our analysis (not in scope of this analysis). 
         * Total of 60,268 missing values, pre-cleansing - and 904 missing values post-cleansing
   2. There were no duplicate records
   3. We did not identify outliers in the traditional mindset of a potential      irregularity or inaccuracy with the data. Since the data are procured by the USDA, and are presumably of better than average quality, we kept any potential outliers because while the distribution of data is important and recognition of outliers is crucial, in our analysis the outliers are beneficial in understanding any potential unique products that help support our analysis of corn syrup, sugar, and high fructose corn syrup. 

## Experimental Design

1. Pull the data from the USDA website and extract the data to a working directory (requests)
2. Import the brand data into a table for analysis (pandas)
3. Insert a new column indicating the presence of corn syrup in the ingredients list (pandas)
4. Insert a new column indicating the position of corn syrup in the ingredients list (pandas)
5. Group the branded items based on the position of corn syrup (pandas)
6. Produce a visualization showing how many products a company has listed which includes corn syrup, scaled by the position of corn syrup in the ingredients list. (matplotlib / plotly)
7. If we get to it:
   1. Loop this analysis over multiple years of the dataset
   2. Establish a regression analysis based on the data over the collected years (scipy)

### Code Design and Flow

We established some common coding standards at the beginning of our project including:

1.	Ensuring our code is reproducible as a module and package.
2.	We would separate our analysis and our common functionality, as to create opportunities for code reuse.
3.	We would establish a base object that contained our common functions used in our analysis and expand on them based on the different CSV files.
4.	We would publish our EDA and various analysis questions as independent modules that utilize these common functions.
5.	We would fully document our code using the Google DocString format, making our code easier to understand and easier for others to understand how each of our functions work.
6.	We would test the code where we’ve written custom logic using pytest and sample data.

#### Explanation of Fetch.py

The first module (fetch) acted as our general purpose download engine to obtain the data as published by the USDA.  It operated from the assumption that there would be a reference file that contained the Universal Resource Locator (URL) to the research data from the Food Data Central (FDC), and extract the data on the local machine.  This was implemented using the python requests library to obtain the zip file and save it to a temporary location as determined by python’s tempfile library.  By doing this, we can have confidence the download would be written to a temporary directory and be cleaned up after the program finished execution.  As the research data is compressed, we used zipfile to automate the extraction of the data immediately after the file was downloaded to a specified directory.

<img width="468" alt="image" src="https://user-images.githubusercontent.com/65091393/117586659-83cb3a00-b0e7-11eb-82e1-1927f59f0f6a.png">

This results in a very clean execution flow that’s configured for obtaining future FDC without having to rewrite code, and also supports future analysis where multiple datasets may be needed.  This was detached from the rest of our execution to conserve bandwidth on consecutive runs.

#### Explanation of Parser.py

The second module written established the common objects and functions that would be used for all future analysis.  This module is the most complicated of the entire project as it composes our dataframe, performs cleanup, and also exposes functionality to augment each object’s dataframe.

While our analysis focused on only the branded_foods.csv file from the research data, we noticed that there were several other files that represented a food item.  As such, we actively made the choice to create a base object that would define common methods and structure to give our program’s a common api that is ready to share common functionality and also allow for more specific queries to be written for specific tables.

Our base object established several common functionality methods that breaks down the aforementioned construction of the object, isolating the loading of CSV files, creating a few filter methods that reduces the object’s dataframe by the specified column name and the value (find_top and clamp),  and the run_of_df function that runs the passed function on the data frame, the same way that pandas does for its aggregate functions. While we define a cleanup function in the base object, we force all subclasses to define their own method by raising a NotImplementedError.  This provides a similar implementation to an “abstract” class in other object oriented languages.

From there, a new food brand object extends the base food object, inheriting all the above common methods, implements its own unique cleanup method, and also defines some methods unique to the branded food csv file.  In this case, we define a new method to call the previously defined filter method to return the records that are only with the named brand.  The FoodBrandObject also defines a unique method that identifies all the unique ingredients from the ingredients list.  It uses a series of regular expressions to normalize parenthetical and bracketed values in the ingredients list and also normalizes common delimiters (comma, semicolon and periods) used when labeling ingredients.  As many of these methods return lists of lists, we use a multi layer generator pattern to unnest the lists to a single dimension.

The methods of find_index_from_str and insert_index are utility functions that were designed to support the run_on_df method of our food objects and perform our feature engineering.  These perform simple operations, such as finding the position of an ingredient from a comma separated list that’s a string, and a method designed to augment a dataframe so that the matches are inserted as a new column that matches the ingredient name you wish to search on.

All of the above logic when combined provides the sufficient data cleaning, filtering, parsing, and feature generation that’s needed to perform our analysis.

#### Explanation of Question Files

The python modules that start with the word “question” are where we performed our analysis from the parser module.  Each one runs as standalone assessments and seeks to answer a question in the module’s doc string.  

## Project Management

We have designed a project timeline showcasing the key milestones that we would like to hit incrementally along the way. The timeline takes into consideration the course schedule for the remainder of the semester, the final exam dates of May 1st and May 2nd, and our preference of having enough time to review our work so that we can be sure high-quality deliverables are produced. It should also be noted that we will schedule weekly check-ins so that we can touch base, share any feedback and concerns, and evaluate our progress to ensure alignment with the project timeline. While we have no plans of formally adhering to Agile project management practices, we will ensure that we embrace change and make minor course corrections along the way, if needed. That is to say that the project timeline is something we hope to stick to, but understand that it’s more advantageous to make small changes along the way as opposed to strictly adhering to a project timeline, irrespective of the facts and circumstances we discuss in our check-ins.

To coordinate the programming component of the project among, we will use GitHub and create a new organization for this project. This will allow us to upload files in a clean and organized manner, and also help facilitate the division of coding work. We have decided for the time-being, that given our varied backgrounds and skill-levels in python and in programming in general, that we will not formally assign ‘roles’ but will assign responsibilities for each week. This will allow us to collaborate and leverage one another's strengths to compensate for any potential weaknesses we may have so that we can work as an efficient and collaborative team. As we get closer to the end of the project, we may designate one individual to be responsible for compiling the final report. This will be decided in a weekly check-in towards the end of April. The goal of the timeline is to help facilitate the flow of raw data → information → knowledge → wisdom, in the most student-friendly way possible.

### Project Timeline (weekly check-ins not shown)
* 3/17 - Project begins
* 3/24 - Weekly meeting schedule (day(s) and time(s)) decided and begin conceptualizing and designing data sets and perform any data cleanup to address data quality issues
* 3/31 - Clean datasets generated and EDA begins
* 4/7 - EDA is completed and coding begins
* 4/21 - Coding is completed; testing begins
* 4/28 - Testing completed; findings discussed, and begin write-up. "What did we learn?"
* 4/28 - 5/5 - Use this week to incorporate feedback from professor/classmates/TAs, make any changes to code or write-up, finish write-up, and record the video presentation and compile each segment into one video file (final exam is 5/1-5/2 so we can record after the exam)
* 5/5 - Project Presentation
* 5/8 - Final Project Submission due in Collab
 
## Beyond the Original Specifications

Some interesting features we’ve added to this module include:

1.	Integrating into python’s most recent packaging standards following Python’s PEP 508 and PEP 621 formats.  All of our code is written using Poetry’s packaging and dependency management capabilities, which reads the pyproject.toml file for all python packages and metadata about our project.  As a result, a new analyst can get started quickly by simply installing poetry and running poetry shell and poetry update and all required software dependencies will be downloaded and will match our specification from our toml file.  Similarly, our package can be prepared for uploading into pypi with the command poetry build, automating the creation of the package zip and related python metadata, generating both a tar.gz and whl file.
2.	The “doc” folder contains all the required files to generate a Sphinx website, and is configured to include our python API docs.  While there’s two manual steps to generate this, you can run “make api html” to generate a sphinx website with all of our API documentation.
3.	While described as part of our coding design and flow, we decided to implement a trivial data collection tool that automated the download of the database files and the extraction.
4.	The modules were written using CLI arguments, so that users of our app could reconfigure how the execution worked without having to dive deep into the code.
 
## Results

After the coding and testing phases of the project have concluded, we will begin discussing our findings internally . We hope to have taken raw data, converted it into information, then into knowledge, and finally into actionable wisdom. To discuss and socialize our analysis including code written, the course corrections we made and why, visualizations created, and findings from our analysis along with real-world applicability of our findings - we plan on generating a Word document and an accompanying slide deck in Powerpoint for the video presentation component of the project. Tables and charts/graphs will be created in python and included in both the Word document and slide deck. 

### Question 1

For question one, we focused on the top 10 brands that used the most corn syrup and sugar in their products. With this analysis we are able to see which brands contribute to the most use of corn syrup and sugar. Also, we can compare the brands discovered between the two ingredients. This was first done by establishing our branded food item, one for corn syrup and one for sugar. From there we produced plots based off of the intended analysis. This analysis consisted with the top 10 brands to have a narrowed down approach to this analysis as there are many brands present in the data set. The plots that were generated are q2-cornsyrup-10max.png, q2-cornsyrup-unbound.png, q2-sugar-10max.png, and q2-sugar-unbound.png. These plots are violin plots that are generated by seaborn. The plots show the density and distribution of where corn syrup or sugar was in the index, respectively. The width of the brands indicates the overall density of the data at a particular point of interest, while there is a small box plot contained within the density ridges to show the overall distribution of data for each brand. The plots q2-cornsyrup-10max.png and q2-sugar-10max.png show the rank of the ingredients having a ceiling till the rank value of 10 to show a zoomed in version of the unbounded plots.  

The unbounded plots for corn syrup and sugar, respectively: 

<img width="468" alt="image" src="https://user-images.githubusercontent.com/65091393/117587059-06ed8f80-b0ea-11eb-8858-892e214d9fdf.png">

<img width="468" alt="image" src="https://user-images.githubusercontent.com/65091393/117587067-0e149d80-b0ea-11eb-9226-34c0f88e5e00.png">

The plots with the bounded rank ceiling of 10 for corn syrup and sugar, respectively:

<img width="469" alt="image" src="https://user-images.githubusercontent.com/65091393/117587075-17056f00-b0ea-11eb-86fe-e9e2f148124a.png">

<img width="468" alt="image" src="https://user-images.githubusercontent.com/65091393/117587079-1c62b980-b0ea-11eb-8bb5-b904fb011e2a.png">

With both unbounded and bounded plots, it can be seen that both corn syrup and sugar are present in the same top 10 brands even though the brands are at different placings for both ingredients. The top 10 brands are *The Kroger Co.; Supervalu, Inc; Harris-Teeter Inc.; Target Stores; Wal-Mart Stores, Inc; Hy-Vee, Inc.; Topco Associates, Inc.; Nash Finch Company, Mejier, Inc.*; and  Safeway, Inc. The rankings and their densities between corn syrup and sugar in their respective plots are in the similar range of each other but are not exactly the same. This shows that the corn syrup and sugar are independent of each other and brands use them on their own individual measurements in their products. 

### Question 2

For question two, it inverted our logic from brands to food categories.  By doing this we are confirming where the product was used across all food items and if there were any surprising factors that become apparent in the analysis.  This was first done by establishing our branded food item and then producing a number of plots based off of our objectives.  The analysis was limited to top five as increasing the number of categories didn’t appear to have any significant results.  In this question we also reviewed for interactions.  This was done via a pairplot from seaborn and by using scikit learn, using corn syrup as a predictor for the index position of sugar.  When we ran this, we did get a linear model of sugar = 2.13423854 + 0.11217854(corn_syrup), but the outputted regression had a very low R^2 value of 0.08530698.  Reviewing the pairwise plot also demonstrated that there appeared to be very little correlation between the two ingredients.

<img width="468" alt="image" src="https://user-images.githubusercontent.com/65091393/117587138-7fece700-b0ea-11eb-9571-885393995f48.png">

As additional output from this generation, there are four plots to support our claims.

The two plots are q3-cornsyrup-cat.png and q3-sugar.png, which is a violin plot generated by seaborn showing the density and distribution of where corn syrup or sugar was in the index, respectively.  The width of the categories indicates the overall density of the data at a particular point of interest, while there is a small box plot contained within the density ridges to show the overall distribution of data.

For Corn Syrup:

<img width="440" alt="image" src="https://user-images.githubusercontent.com/65091393/117587152-92ffb700-b0ea-11eb-91a9-6550a202d43a.png">

For Sugar:

<img width="439" alt="image" src="https://user-images.githubusercontent.com/65091393/117587161-9c891f00-b0ea-11eb-99d6-dc2cdc371cc6.png">

An interesting inferential statement can be made between these two graphics is that the usage of sugar and corn syrup in the top five food categories appears to be the same, as the two plots are nearly identical in terms of density.

To support this assumption, we did a ridge chart with the values of corn syrup and sugar against each other with this same data, to see if this assumption appears sound.

<img width="468" alt="image" src="https://user-images.githubusercontent.com/65091393/117587173-ab6fd180-b0ea-11eb-86ac-43580ff42191.png">

From this output, we were able to conclude that both sugar and corn syrup, when used, are frequently early on in the ingredients list.  Sugar appears to be used about 25% more than corn syrup and is more likely to be at the front of the ingredients list.

The last plot was used to determine if there were any interactions to see if sugar and corn syrup were frequently used together.  Using a pairplot, we can see that the relationships do not appear to follow our linear assumptions and the data points appear unrelated.

<img width="468" alt="image" src="https://user-images.githubusercontent.com/65091393/117587189-bcb8de00-b0ea-11eb-8d5a-6d14687abb07.png">

### Question 3

For question three, we focused on solid food items and liquid food items that contain the ingredients corn syrup and sugar. With this analysis we are able to see how much corn syrup and sugar are used in solid and liquid food items. This was first done by establishing our branded food item, one for corn syrup and one for sugar. From there we produced plots based off of the intended analysis. The plots produced are q4-cornsyrup.png and q4-sugar.png. These plots are catplots generated by seaborn. The catplots allow us to visually see the columns for the solid food items and liquid food items while also plotting the data points corresponding to the ingredient’s index. The plots show the serving size unit on the x-axis, which consist of the grams (g) and milliliters (ml). The measurement of grams corresponds to the solid food items and the measurement of milliliters corresponds to the liquid food items. The data points represent where the serving size corresponds to the corn syrup and sugar index in their respective plots. 

The plots for corn syrup and sugar, respectively: 

<img width="382" alt="image" src="https://user-images.githubusercontent.com/65091393/117587204-d3f7cb80-b0ea-11eb-93ca-a677696a0d6b.png">

<img width="382" alt="image" src="https://user-images.githubusercontent.com/65091393/117587208-d823e900-b0ea-11eb-9250-788ee25eb53d.png">

From these plots, it can be concluded that there is a greater number of solid food items than liquid food items for both ingredients, corn syrup and sugar. Taking account of the different scale indexes for corn syrup and sugar, it can also be seen that corn syrup is more present in solid food items than sugar. On the other hand, sugar is more present in liquid food items than corn syrup. This analysis also supports the fact that corn syrup and sugar are independent of each other and are used on their own individual measurements in both solid and liquid food items.

### Question 4

For question four, we focused on comparing the distribution of corn syrup and high fructose corn syrup (HFCS) among solid foods and liquid foods. Our motivation for investigating corn syrup vs. HFCS is centered around insights gleaned from the FDA’s website, which focuses on high fructose corn syrup. As mentioned earlier, the most prevalent forms of HFCS are either 42% or 55% fructose, or HFCS 42 and HFCS 55, respectively. HFCS 42 is most commonly used in solid foods and some beverages whereas HFCS 55 is used mostly in soft drinks. Accordingly, we thought it would be interesting to see if what we learned on the FDA’s website was reflected within our dataset. 

In taking a look at the two visuals below, we can see that taking into consideration the differences in y-axis values, the distribution of corn syrup and high fructose corn syrup among solid and liquid foods looks even, for the most part. We also learned that there are more products that contain corn syrup than those that contain high fructose corn syrup. This is most likely attributable to the fact that high fructose corn syrup has generated significant controversy in the general public. The idea that high fructose corn syrup is unhealthier than other sweeteners, including corn syrup, has stuck. The exact science of this is unclear but preliminary research suggests that this due to the difference in metabolic reaction to fructose vs. glucose. While interesting, no major conclusions can be drawn from this splice of the data, but certainly warrants additional research.

<img width="297" alt="image" src="https://user-images.githubusercontent.com/65091393/117587262-f984d500-b0ea-11eb-9ef5-9b238646898e.png">

<img width="298" alt="image" src="https://user-images.githubusercontent.com/65091393/117587271-00134c80-b0eb-11eb-8044-f8b486538321.png">

## Testing

Any testing that we will conduct will be based on the code we write to import, data pre-processing, and data visualization. The unit tests will be written to ensure that the written code’s behavior is consistent with how we would like the outcome to be. For each method written, a unit test will be written as well. 

### Testing Fetcher

The fetcher class is primarily implemented by third party libraries, so there wasn’t much to test other than the logic of establishing a temporary directory to store the transient zip file and to validate the way how the fetcher’s configuration file is read.  In these scenarios, we test the fetcher class to make sure that our object sets the correct internal variables from its constructor, that the config file only processes each line as its own download to be processed, that lines in the config file that start with a octothorpe are ignored, and that when calling add_uri explicitly that the passed string to the download class.

### Testing Parser

The parser tests evaluate a fairly extensive suite of functionality as this is where most of our coding logic resides.  In these tests, we use a sample set of five records that were taken from the branded_foods.csv file that were augmented for the various input scenarios.  This allowed our tests to run quickly, and the test data made it so that we did not need to inject dummy data into our test cases directly.  The logic behind this injection was using pytest’s autoload of conftest.py when running the test suite and establishing the datadir as a pytest fixture.  While the code used to insert the test CSV files were taken from stackoverflow, they were slightly modified for our scenario.

After adding this additional test scaffolding, tests were written for default conditions, parameterized calls, expected values, simple type checking, and the mutation logic we’ve built as part of these food objects.

## Conclusions

We learned that nearly 25% of all food products we examined contain corn syrup and 50% contain sugar. The amount of each ingredient, that is, the index position of the ingredient in question, is highly dependent on brand, food category, and product. We learned that there is no correlation between corn syrup and sugar. Additionally, ingredients can be misleading. For example, we learned that there are over 200 different names for sugar, with maltodextrin as one of them. 

Given the importance of consuming quality, healthy products with safe ingredients - we recommend additional analysis be performed to take a look at disguised ingredients. Also, a time series analysis would be interesting to take a look at. We could see how the recipes for the same product have changed over time, and then even break this down into food categories, brands, serving size, serving size unit, and other attributes. It was suggested in class that we could find data on product sales to research whether there is a relationship between sales in dollars and amount of a particular ingredient. This would require piecing together additional data sets but is certainly an interesting topic of focus.

## References

Center for Food Safety and Applied Nutrition. (n.d.). High Fructose Corn Syrup Questions and Answers. U.S. Food and Drug Administration. Retrieved May 8, 2021, from https://www.fda.gov/food/food-additives-petitions/high-fructose-corn-syrup-questions-and-answers 

Git [Computer Software]. (2021, March 26). Retrieved from https://git-scm.com/

Le Cordon Bleu Culinary Arts Institute. (2019, February 4). How to balance the five flavour elements. Home. Retrieved May 8, 2021, from https://www.cordonbleu.edu/news/how-to-balance-the-five-flavours/en.  

Matplotlib [Computer Software]. (2021, March 26). Retrieved from https://matplotlib.org/ 

National Center for Biotechnology Information (2021). PubChem Compound Summary for CID 5282499, Corn syrup. Retrieved April 24, 2021 from https://pubchem.ncbi.nlm.nih.gov/compound/Corn-syrup 

Numpy [Computer Software]. (2021, January 31). Retrieved from https://numpy.org/ 

Pandas [Computer Software]. (2021, March 02).  Retrieved from https://pandas.pydata.org/

Poetry [Computer Software]. (2021, April 14). Retrieved from https://python-poetry.org/ 

Python [Computer Software]. (2020, October 05).  Retrieved from https://www.python.org/ 

Pytest [Computer Software]. (2021, April 03). Retrieved from https://docs.pytest.org/en/6.2.x/. 

Requests [Computer Software]. (2020, December 16). Retrieved from https://docs.python-requests.org/en/master/index.html. 

Scikit-Learn [Computer Software]. (2021, April). Retrieved from https://scikit-learn.org/stable/index.html. 

Seaborn [Computer Software]. (2020, December). Retrieved from https://seaborn.pydata.org/. 

US Department of Agriculture. (2020, October). FoodData Central Download Data. FoodData Central. https://fdc.nal.usda.gov/download-datasets.html. 

## Annex A: Project Resources
Git Repository: https://github.com/uva-sp2021-cs5010-g6/finalproject 
