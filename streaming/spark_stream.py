from pyspark.sql.functions import *


def apply_silver_transformations(df):
    """
    Silver Layer
    Business-ready cleaned data.
    """

    silver_df = (

        df

        # Remove records without user
        .filter(col("user_id").isNotNull())

        # Remove records without event type
        .filter(col("event_type").isNotNull())

        # Remove invalid prices
        .filter(col("price") >= 0)

        # Remove duplicate events
        .dropDuplicates(["event_id"])

        # Convert timestamp
        .withColumn(
            "event_timestamp",
            to_timestamp("timestamp")
        )

        # Business columns
        .withColumn(
            "event_date",
            to_date("event_timestamp")
        )

        .withColumn(
            "event_hour",
            hour("event_timestamp")
        )

        .withColumn(
            "is_purchase",
            when(
                col("event_type") == "purchase",
                1
            ).otherwise(0)
        )

        .withColumn(
            "purchase_amount",
            when(
                col("event_type") == "purchase",
                col("price")
            ).otherwise(0)
        )

        .withColumn(
            "ingestion_time",
            current_timestamp()
        )

    )

    return silver_df
