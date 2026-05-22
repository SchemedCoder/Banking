from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder \
    .appName("BankingAuditPipeline") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# ---------------------------------
# Read Kafka Stream
# ---------------------------------
raw_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "bank_transactions") \
    .load()

json_df = raw_df.selectExpr("CAST(value AS STRING)")

# ---------------------------------
# Schema
# ---------------------------------
schema = """
transaction_id INT,
account_id STRING,
customer_name STRING,
city STRING,
transaction_type STRING,
amount DOUBLE,
transaction_status STRING,
transaction_time STRING
"""

# ---------------------------------
# Parse JSON
# ---------------------------------
parsed_df = json_df \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# ---------------------------------
# Data Quality
# ---------------------------------
clean_df = parsed_df.dropna()

# ---------------------------------
# Timestamp Conversion
# ---------------------------------
clean_df = clean_df.withColumn(
    "transaction_time",
    to_timestamp("transaction_time")
)

# ---------------------------------
# Watermarking
# ---------------------------------
clean_df = clean_df.withWatermark(
    "transaction_time",
    "10 minutes"
)

# ---------------------------------
# Fraud Detection Rules
# ---------------------------------
fraud_df = clean_df.withColumn(
    "is_suspicious",
    when(col("amount") > 1000000, 1).otherwise(0)
)

# ---------------------------------
# Aggregations
# ---------------------------------
agg_df = fraud_df.groupBy(
    "city",
    "transaction_type"
).agg(
    count("*").alias("total_transactions"),
    sum("amount").alias("total_amount"),
    sum("is_suspicious").alias("suspicious_transactions")
)

# ---------------------------------
# Write to ADLS Gen2
# ---------------------------------
query = agg_df.writeStream \
    .outputMode("complete") \
    .format("parquet") \
    .option(
        "path",
        "abfss://gold@bankauditlake.dfs.core.windows.net/audit/"
    ) \
    .option(
        "checkpointLocation",
        "abfss://gold@bankauditlake.dfs.core.windows.net/checkpoints/"
    ) \
    .start()

query.awaitTermination()
