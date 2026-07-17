from pyspark.sql import SparkSession

from configs.config import *


def create_spark_session():
    """
    Create Spark Session.
    """

    spark = (
        SparkSession.builder
        .appName("ClickstreamAnalytics")
        .master("local[*]")

        .config(
            "spark.sql.shuffle.partitions",
            "4"
        )

        # Kafka Connector (Spark 3.5.8)
        .config(
            "spark.jars.packages",
            "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.8"
        )

        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("WARN")

    return spark


def read_kafka_stream(spark):
    """
    Read Clickstream Events from Kafka.
    """

    df = (
        spark.readStream
        .format("kafka")
        .option(
            "kafka.bootstrap.servers",
            KAFKA_BOOTSTRAP_SERVERS
        )
        .option(
            "subscribe",
            CLICKSTREAM_TOPIC
        )
        .option(
            "startingOffsets",
            "earliest"
        )
        .load()
    )

    return df


if __name__ == "__main__":

    spark = create_spark_session()

    kafka_df = read_kafka_stream(spark)

    query = (
        kafka_df
        .selectExpr("CAST(value AS STRING)")
        .writeStream
        .format("console")
        .outputMode("append")
        .option("truncate", False)
        .start()
    )

    query.awaitTermination()
