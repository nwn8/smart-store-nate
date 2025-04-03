#Use these for SQLITE

Create_customer_table = "CREATE TABLE IF NOT EXISTS customer (CustomerID INTEGER PRIMARY KEY,Name TEXT,Region TEXT,JoinDate TEXT, LoyaltyPoints INTEGER, ContactMethod TEXT);"

Create_products_table = "CREATE TABLE IF NOT EXISTS product (ProductID INTEGER PRIMARY KEY,ProductName TEXT,Category TEXT, UnitPrice REAL, DiscountPercent INTEGER, Subcategory TEXT);"

Create_sale_table="CREATE TABLE IF NOT EXISTS sale (TransactionID INTEGER PRIMARY KEY,SaleDate TEXT,CustomerID INTEGER,ProductID INTEGER, StoreID INTEGER, CampaignID INTEGER, SaleAmount REAL,BonusPoints INTEGER, PaymentType TEXT, FOREIGN KEY (CustomerID) REFERENCES customer (CustomerID),FOREIGN KEY (ProductID) REFERENCES product (ProductID));"



### Use these for MYSQL

Create_customer_table_mysql = "CREATE TABLE IF NOT EXISTS customer (CustomerID INT PRIMARY KEY,Name VARCHAR(255),Region VARCHAR(255),JoinDate VARCHAR(255), LoyaltyPoints INT, ContactMethod VARCHAR(255));"

Create_products_table_mysql = "CREATE TABLE IF NOT EXISTS product (ProductID INT PRIMARY KEY,ProductName VARCHAR(255),Category VARCHAR(255), UnitPrice DECIMAL, DiscountPercent INT, Subcategory VARCHAR(255));"

Create_sale_table_mysql="CREATE TABLE IF NOT EXISTS sale (TransactionID INT PRIMARY KEY,SaleDate VARCHAR(255), CustomerID INT,ProductID INT, StoreID INT, CampaignID INT, SaleAmount DECIMAL,BonusPoints INT, PaymentType VARCHAR(255), FOREIGN KEY (CustomerID) REFERENCES customer (CustomerID),FOREIGN KEY (ProductID) REFERENCES product (ProductID));"
