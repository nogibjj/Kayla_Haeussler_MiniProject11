""" 
Library Functions Using PySpark
"""
import os
import requests
from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col
from pyspark.sql.types import (
     StructType, 
     StructField, 
     IntegerType, 
     StringType, 
     DateType
)


def create_spark_session(app_name = "MyApp"):
    """ initialize spark session """
    spark = SparkSession.builder \
        .appname(app_name) \
        .getOrCreate()
    return spark

