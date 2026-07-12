from pyspark.sql.functions import *

def clean_clickstream(df):
    """
    Clean raw clickstream events.
    """

    cleaned_df = (

        df

        # Remove records without user id
        .filter(col("user_id").isNotNull())

        # Remove records without event type
        .filter(col("event_type").isNotNull())

        # Remove invalid prices
        .filter(col("price") >= 0)

        # Remove duplicate events
        .dropDuplicates(["event_id"])

    )

    return cleaned_df
