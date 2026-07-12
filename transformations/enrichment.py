from pyspark.sql.functions import *

def enrich_clickstream(df):
    """
    Add useful business columns.
    """

    enriched_df = (

        df

        .withColumn(

            "event_timestamp",

            to_timestamp("timestamp")

        )

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

    )

    return enriched_df
