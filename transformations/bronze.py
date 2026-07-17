from pyspark.sql.functions import *
from pyspark.sql.types import *


def get_clickstream_schema():
    """
    Define the schema for incoming clickstream events.
    """

    return StructType([
        StructField("event_id", StringType(), True),
        StructField("timestamp", StringType(), True),
        StructField("user_id", IntegerType(), True),
        StructField("session_id", StringType(), True),
        StructField("country", StringType(), True),
        StructField("city", StringType(), True),
        StructField("device", StringType(), True),
        StructField("browser", StringType(), True),
        StructField("page", StringType(), True),
        StructField("event_type", StringType(), True),
        StructField("product_id", IntegerType(), True),
        StructField("price", DoubleType(), True)
    ])


def apply_bronze_transformations(df):
    """
    Parse Kafka JSON and perform Bronze layer validation.
    """

    schema = get_clickstream_schema()

    bronze_df = (
        df
        .selectExpr("CAST(value AS STRING) AS json")
        .select(
            from_json(col("json"), schema).alias("data")
        )
        .select("data.*")

        # Data Quality Rules
        .filter(col("event_id").isNotNull())
        .filter(col("user_id").isNotNull())
        .filter(col("event_type").isNotNull())
        .filter(col("price") >= 0)

        # Convert timestamp
        .withColumn(
            "event_timestamp",
            to_timestamp("timestamp")
        )

        # Partition column
        .withColumn(
            "event_date",
            to_date("event_timestamp")
        )

        # Remove duplicate events
        .dropDuplicates(["event_id"])
    )

    return bronze_df
