# Databricks notebook source
# MAGIC %md
# MAGIC Notebook showing the execution of ETL pipeline (extract, transform, load)

# COMMAND ----------


from mylib.lib import *

# COMMAND ----------

# MAGIC %md
# MAGIC First, extract

# COMMAND ----------

# initialize Spark
spark = create_spark_session('House_District')

# extract data
df = extract_data(spark, "data/house_district_forecast.csv")

# COMMAND ----------

# MAGIC %md
# MAGIC Then, transform

# COMMAND ----------

# transform data
transformed_df = transform_data(df)

# run SQL query
sql_result_df = run_spark_sql(df)

# COMMAND ----------

# MAGIC %md
# MAGIC Now, load

# COMMAND ----------

# save results
load_data(sql_result_df, "ids706_data_engineering.default.keh119_electiondistrict")

# stop Spark session
spark.stop()
