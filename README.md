# Group 6 Semester Project

* Nitika Kataria (NK3RF) - <nk3rf@virginia.edu>
* Robert Knuuti (UQQ5ZZ) - <uqq5zz@virginia.edu>
* Swaroop Veerabhadrappa (SBV5DN) - <sbv5dn@virginia.edu>

## Problem Statement

How much corn syrup are companies using in today’s products?

## Proposal

### Introduction

Companies today have direct influences on our health with the way they have composed our food.
One particular concern that's been in the front of many health conscious individuals is the prolific usage of corn syrup in big brand companies.

With this report, we seek to identify which companies produce the most products that include corn syrup and perform analysis on the results of brands that use corn syrup, establishing a ranking based on their usage of corn syrup in their ingredients list.
Additionally, we seek to identify how frequently corn syrup is used in products of similar categories of food.
Furthermore, we will attempt to draw conclusions of these metrics over time.

By the end of this analysis, our data will show what brands are limiting the usage of corn syrup across the industry.

### The Data
The collected data has been curated by the United States Department of Agriculture (USDA) that is sampled yearly (and may have an update issued within the year) of the currently approved food items for sale in the United States stores.
This agency provides an authoritative set of information independent of manufacturers and the sellers, providing unbiased information source to perform this analysis.

This data is represented in two formats (Microsoft Access and CSV).
The CSV is an export of the Access database tables, and will be used in this project.
The USDA has produced a data dictionary demonstrating how the CSV file elements link between each table, allowing for cross-table analysis from the export.
For our analysis, we will be leveraging the CSV formatted files.
These can be obtained directly from USDA at https://fdc.nal.usda.gov/download-datasets.html .

Performing this analysis will require the investigation of the `food_brands.csv` file and its associated references as described in the USDA data dictionary PDF.
This table will require transformation as the listing of ingredients is a single data cell that will need to be split to inventory what ingredients are used in the branded product.
According to the dictionary, the listing of ingredients is exactly the same as they are listed on the product in stores.
The general ruling on ingredient listings is that the earlier an ingredient is in the list, the more significant the ingredient is in the final product (indicating that more is used).

### Experimental Design

1. Pull the data from the USDA website and extract the data to a working directory (requests)
2. Import the brand data into a table for analysis (pandas)
3. Insert a new column indicating the presence of corn syrup in the ingredients list (pandas)
4. Insert a new column indicating the position of corn syrup in the ingredients list (pandas)
5. Group the branded items based on the position of corn syrup (pandas)
6. Produce a visualization showing how many products a company has listed which includes corn syrup, scaled by the position of corn syrup in the ingredients list. (matplotlib / plotly)
7. If we get to it:
   1. Loop this analysis over multiple years of the dataset
   2. Establish a regression analysis based on the data over the collected years (scipy)

### Project Management

We have designed a project timeline showcasing the key milestones that we would like to hit incrementally along the way.
The timeline takes into consideration the course schedule for the remainder of the semester, the final exam dates of May 1st and May 2nd, and our preference of having enough time to review our work so that we can be sure high-quality deliverables are produced.
It should also be noted that we will schedule weekly check-ins so that we can touch base, share any feedback and concerns, and evaluate our progress to ensure alignment with the project timeline.
While we have no plans of formally adhering to Agile project management practices, we will ensure that we embrace change and make minor course corrections along the way, if needed.
That is to say that the project timeline is something we hope to stick to, but understand that it’s more advantageous to make small changes along the way as opposed to strictly adhering to a project timeline, irrespective of the facts and circumstances we discuss in our check-ins.

To coordinate the programming component of the project among, we will use GitHub and create a new organization for this project.
This will allow us to upload files in a clean and organized manner, and also help facilitate the division of coding work.
We have decided for the time-being, that given our varied backgrounds and skill-levels in python and in programming in general, that we will not formally assign "roles" but will assign responsibilities for each week.
This will allow us to collaborate and leverage one another's strengths to compensate for any potential weaknesses we may have so that we can work as an efficient and collaborative team.
As we get closer to the end of the project, we may designate one individual to be responsible for compiling the final report.
This will be decided in a weekly check-in towards the end of April.
The goal of the timeline is to help facilitate the flow of raw data to information to knowledge to wisdom, in the most student-friendly way possible.

#### Project Timeline (weekly check-ins not shown)
* 3/17 - Project begins
* 3/24 - Weekly meeting schedule (day(s) and time(s)) decided and begin conceptualizing and designing data sets and perform any data cleanup to address data quality issues
* 3/31 - Clean datasets generated and EDA begins
* 4/7 - EDA is completed and coding begins
* 4/21 - Coding is completed; testing begins
* 4/28 - Testing completed; findings discussed, and begin write-up. "What did we learn?"
* 4/28 - 5/5 - Use this week to incorporate feedback from professor/classmates/TAs, make any changes to code or write-up, finish write-up, and record the video presentation and compile each segment into one video file (final exam is 5/1-5/2 so we can record after the exam)
* 5/5 - Project Presentation
* 5/8 - Final Project Submission due in Collab
 
### Results

After the coding and testing phases of the project have concluded, we will begin discussing our findings internally.
We hope to have taken raw data, converted it into information, then into knowledge, and finally into actionable wisdom.
To discuss and socialize our analysis including code written, the course corrections we made and why, visualizations created, and findings from our analysis along with real-world applicability of our findings - we plan on generating a Word document and an accompanying slide deck in Powerpoint for the video presentation component of the project.
Tables and charts/graphs will be created in python and included in both the Word document and slide deck. 

### Testing

Any testing that we will conduct will be based on the code we write to import, data pre-processing, and data visualization.
The unit tests will be written to ensure that the written code’s behavior is consistent with how we would like the outcome to be.
For each method written, a unit test will be written as well. 

### Conclusions
The plan for this project is to collect the data from the USDA website and pre-process the data so that proper visualizations and analysis can be conducted.
With the visualizations and analysis, we will be able to showcase our findings on corn syrup related to the different brands and products.
These findings can be used by others as a way to visually see how corn syrup is used in the products they might be consuming.
This will allow others to visually see a concise way of how corn syrup is used and will help others gain a better understanding about how much is being consumed by them. 

# References

Git [Computer Software]. (2021, March 26). Retrieved from https://git-scm.com/

Matplotlib [Computer Software]. (2021, March 26). Retrieved from https://matplotlib.org/ 

Numpy [Computer Software]. (2021, January 31). Retrieved from https://numpy.org/ 

Pandas [Computer Software]. (2021, March 02).  Retrieved from https://pandas.pydata.org/

Python [Computer Software]. (2020, October 05).  Retrieved from https://www.python.org/ 

US Department of Agriculture. (2020, October). FoodData Central Download Data. FoodData Central. https://fdc.nal.usda.gov/download-datasets.html. 

# Annex A: Project Resources
Git Repository: https://github.com/uva-sp2021-cs5010-g6/finalproject 

