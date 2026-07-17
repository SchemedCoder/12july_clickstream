from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("VerifySilver")
    .master("local[*]")
    .config(
        "spark.jars.packages",
        "io.delta:delta-spark_2.12:3.2.0"
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

df = spark.read.format("delta").load("data/silver")

print("\nSchema\n")
df.printSchema()

print("\nSample Data\n")

df.show(10, truncate=False)

spark.stop()
