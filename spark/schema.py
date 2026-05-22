
 #Banking transaction schema

transaction_schema = """
transaction_id INT,
account_id STRING,
customer_name STRING,
city STRING,
transaction_type STRING,
amount DOUBLE,
transaction_status STRING,
transaction_time STRING
"""


#Customer Schema


customer_schema = """
customer_id INT,
account_id STRING,
customer_name STRING,
city STRING,
account_type STRING,
kyc_status STRING,
risk_category STRING,
account_open_date STRING,
mobile_number STRING
"""
