from data_scrubber import DataScrubber
import pathlib
import sys
import pandas as pd

customers_file_name="customers_data_prepared.csv"
products_file_name="products_data_prepared.csv"
sales_file_name="sales_data_prepared.csv"

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))


DATA_DIR: pathlib.Path = PROJECT_ROOT.joinpath("data")
SCRUBBED_DATA_DIR: pathlib.Path = DATA_DIR.joinpath("scrubbed")
PREP_DATA_DIR: pathlib.Path = DATA_DIR.joinpath("prepared")


##### Read and clean customers from prepared folder this is the second level of cleaning

customers_file_path: pathlib.Path = PREP_DATA_DIR.joinpath(customers_file_name)

df_customers=pd.read_csv(customers_file_path)

print("Cleaning customers csv")


scrub_csv=DataScrubber(df_customers)
consistency=scrub_csv.check_data_consistency_before_cleaning()
print(consistency)

df_customers=scrub_csv.handle_missing_data(fill_value="N/A")
df_customers=scrub_csv.parse_dates_to_add_standard_datetime('JoinDate')

results=scrub_csv.check_data_consistency_after_cleaning()
print(results)

customers_write_file_path: pathlib.Path = SCRUBBED_DATA_DIR.joinpath("scrubbed_customers.csv")
df_customers.to_csv(customers_write_file_path)

##### Read and clean Products from prepared folder this is the second level of cleaning

products_file_path: pathlib.Path = PREP_DATA_DIR.joinpath(products_file_name)

df_products=pd.read_csv(products_file_path)

print("Cleaning products csv")


scrub_csv=DataScrubber(df_products)
consistency=scrub_csv.check_data_consistency_before_cleaning()
print(consistency)

df_products=scrub_csv.handle_missing_data(fill_value="N/A")


results=scrub_csv.check_data_consistency_after_cleaning()
print(results)

products_write_file_path: pathlib.Path = SCRUBBED_DATA_DIR.joinpath("scrubbed_products.csv")
df_products.to_csv(products_write_file_path)

