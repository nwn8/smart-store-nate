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