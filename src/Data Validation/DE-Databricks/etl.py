from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Python Spark SQL").getOrCreate()

bronze_df = spark.read.option('header', True).csv("tmp/sample_data.csv")
bronze_df.show()

silver_df = bronze_df.filter(bronze_df['name'].isNotNull())
silver_df.show()
#silver_df.write.format("delta").saveAsTable("silver_table")
#silver_df.to_delta('DE-Databricks/', index=False)

