from pyspark.sql import SparkSession

from configs.config import *

def create_spark_session():

    spark = (
        SparkSession.builder
        .appName("ClickstreamAnalytics")
        .master("local[*]")
        .config(
            "spark.sql.shuffle.partitions",
            "4"
        )
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("WARN")

    return spark
