# smart-store-nate

This project covers the ETL process. CSV data was provided in course.


## How to use

Follow instructions in Requirements.txt to activate a virtual environment and install dependencies.

First layer of cleaning from running prepare_xxxx_data.py in scripts. Output of cleaned csv will be sent to "data/prepared" folder

Second layer of cleaning data_prep.py.  Output of cleanded will be sent to "data/scrubbed" folder.

For exploratory analysis of Customers, Products, and Sales data run initial_analysis.py 

##  Write to database

There are two processes available to write to a database.  

create_database_sqlite will write to a sqlite database in the "data" folder.

create_database_mysql will write to a locally installed mysql database with the user as root and password 1234


## PowerBI Dashboard

Dashboard available at until 6/03/2025

https://app.powerbi.com/links/4mJKjHMk8m?ctid=7335011f-1748-4902-8dee-6f4dac036859&pbi_source=linkShare&bookmarkGuid=95b07924-be36-4ae7-ab79-4ce872ec3bc6


## Section 1: Business Goal
    What are the regional and total sales by category, payment type, as well as the Maximum and minimum sale amount by region?
    Purpose: in order to understand better where to invest marketing efforts to increase sales. 

## Section 2: Data Source
    Data is from the tables defined in the "Tables" tab

## Section 3: Tools
    Data source = MySql database, Data Analysis = PowerBI

## Section 4: Workflow and Logic
    Tables were imported into PowerBI in order to extract regional data.

![allregions](images/allregions.png)

## Section 5: Results
North 

![alt text](images/North.png)

South

![alt text](images/South.png)

East

![alt text](images/east.png)

West

![alt text](images/West.png)


Conclusion:

Laptop sales resulted in the highest dollar amount for each region, while The East Region had over 50K in Laptop sales, and sth South Region had over 17K.   Clothing was the second biggest sellar across all regions.  Sports were the least popular item across all regions. East and South produced the most revenue with east at 62K and South at 24K. 

## Section 6: Suggested Business Action

    East is the most active store by far while North has the least amount of sales.  Possible business actions could include marketing to the strengths of each store.  Because the North tends to Sell more Jackets and hats than electronics it may focus on strictly doing that or expand marketing to increase electronics sales


## Section 7: Challenges
    There were no challenges with this module. 
