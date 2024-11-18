"""
Import and run functions from library for ETL pipeline
"""

from mylib.lib import *
import os
from pyspark.sql import SparkSession

if __name__ == "__main__":
    
    # initialize Spark
    spark = create_spark_session('House_District')

    # extract data
    df = extract_data(spark, url="https://projects.fivethirtyeight.com/congress-model-2018/house_district_forecast.csv", filepath="data/house_district_forecast.csv")

    outputdf = query("""
    SELECT state, 
           party, 
           SUM(CASE WHEN incumbent = true THEN 1 ELSE 0 END) AS incumbent_count, 
           SUM(CASE WHEN incumbent = false THEN 1 ELSE 0 END) AS challenger_count
    FROM ids706_data_engineering.default.keh119_housedistricts
    GROUP BY state, party
    """, "ids706_data_engineering.default.keh119_housedistricts")


    # stop Spark session
    spark.stop()