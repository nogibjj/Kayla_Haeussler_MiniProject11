# Databricks notebook source
# initialize Spark
spark = create_spark_session('House_District')

# extract data
df = extract_data(spark, "data/house_district_forecast.csv")
