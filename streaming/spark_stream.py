from pyspark.sql import SparkSession

from configs.config import *
from transformations.bronze import apply_bronze_transformations


def create_spark_session():
    """
    Create Spark Session with Kafka + Delta Lake support.
    """

    spark = (
        SparkSession.builder
        .appName("ClickstreamAnalytics")
        .master("local[*]")

        .config(
            "spark.sql.shuffle.partitions",
            "4"
        )

        .config(
            "spark.jars.packages",
            ",".join([
                "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.8",
                "io.delta:delta-spark_2.12:3.2.0"
            ])
        )
        .config(
            "spark.sql.extensions",
            "io.delta.sql.DeltaSparkSessionExtension"
        )

        .config(
            "spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog"
        )

        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("WARN")

    return spark


def read_kafka_stream(spark):
    """
    Read Kafka Stream.
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
            "latest"
        )
        .load()
    )

    return df


if __name__ == "__main__":

    spark = create_spark_session()

    kafka_df = read_kafka_stream(spark)

    bronze_df = apply_bronze_transformations(kafka_df)

    query = (
        bronze_df.writeStream
        .format("delta")
        .outputMode("append")

        .option(
            "path",
            "data/bronze"
        )

        .option(
            "checkpointLocation",
            "checkpoints/bronze"
        )

        .partitionBy("event_date")

        .start()
    )

    query.awaitTermination()
