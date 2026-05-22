from pyspark.sql.functions import *

# ----------------------------------------
# Fraud Rules Function
# ----------------------------------------

def detect_fraud(df):

    fraud_df = df.withColumn(

        "is_suspicious",

        when(col("amount") > 1000000, 1)

        .when(col("transaction_status") == "FAILED", 1)

        .otherwise(0)

    )

    # ----------------------------------------
    # Risk Level Classification
    # ----------------------------------------

    fraud_df = fraud_df.withColumn(

        "risk_level",

        when(col("amount") > 2000000, "HIGH")

        .when(col("amount") > 500000, "MEDIUM")

        .otherwise("LOW")

    )

    return fraud_df
