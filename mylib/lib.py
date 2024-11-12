"""
Library Functions Using PySpark
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg


def create_spark_session(app_name = "MyApp"):
    """ initialize spark session """
    spark = SparkSession.builder \
        .appname(app_name) \
        .getOrCreate()
    return spark

def load_data(spark, file_path):
    """
    Loads a CSV file into a Spark DataFrame.
    """
    df = spark.read.csv(file_path, header=True, inferSchema=True)
    return df

def data_transformation(df):
    """
    Performs a transformation on the DataFrame, such as calculating averages
    or filtering rows.
    """
    # Example: Filter out rows with missing values in a specific column
    df_filtered = df.filter(col("some_column").isNotNull())

    # Example: Group by and calculate average for another column
    df_transformed = df_filtered.groupBy("group_column").agg(
        avg("numeric_column").alias("average_value")
        )
    return df_transformed

def run_spark_sql(df):
    """
    Executes a Spark SQL query on the DataFrame after creating a temporary view.
    """
    # Register the DataFrame as a SQL temporary view
    df.createOrReplaceTempView("data_view")

    # Example SQL query to calculate sum and average of a column grouped by another
    sql_query = """
    SELECT group_column, 
           SUM(numeric_column) AS total_value, 
           AVG(numeric_column) AS average_value
    FROM data_view
    GROUP BY group_column
    """
    result_df = df.sql(sql_query)
    return result_df

def save_data(df, output_path):
    """
    Saves the resulting DataFrame to the specified path.
    """
    df.write.csv(output_path, header=True, mode="overwrite")



#------------------------------------------------------------
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

LOG_FILE = "pyspark_output.md"


def log_output(operation, output, query=None):
    """adds to a markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"The operation is {operation}\n\n")
        if query: 
            file.write(f"The query is {query}\n\n")
        file.write("The truncated output is: \n\n")
        file.write(output)
        file.write("\n\n")




def start_spark(appName):
    spark = SparkSession.builder.appName(appName).getOrCreate()
    return spark

def end_spark(spark):
    spark.stop()
    return "stopped spark session"

def extract(
    url="""
   https://github.com/fivethirtyeight/data/blob/master/daily-show-guests/daily_show_guests.csv?raw=true 
    """,
    file_path="data/serve_times.csv",
    directory="data",
):
    """Extract a url to a file path"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
 

    return file_path

def load_data(spark, data="data/serve_times.csv", name="DailyShowGuests"):
    """load data"""
    # data preprocessing by setting schema
    schema = StructType([
        StructField("YEAR", IntegerType(), True),
        StructField("GoogleKnowlege_Occupation", StringType(), True),
        StructField("Show", DateType(), True),
        StructField("Group", StringType(), True),
        StructField("Raw_Guest_List", StringType(), True)
    ])

    df = spark.read.option("header", "true").schema(schema).csv(data)

    log_output("load data", df.limit(10).toPandas().to_markdown())

    return df


def query(spark, df, query, name): 
    """queries using spark sql"""
    df = df.createOrReplaceTempView(name)

    log_output("query data", spark.sql(query).toPandas().to_markdown(), query)

    return spark.sql(query).show()

def describe(df):
    summary_stats_str = df.describe().toPandas().to_markdown()
    log_output("describe data", summary_stats_str)

    return df.describe().show()

def example_transform(df):
    """does an example transformation on a predefiend dataset"""
    conditions = [
        (col("GoogleKnowlege_Occupation") == "actor")
          | (col("GoogleKnowlege_Occupation") == "actress"),
        (col("GoogleKnowlege_Occupation") == "comedian") 
        | (col("GoogleKnowlege_Occupation") == "comic"),
    ]

    categories = ["Acting", "Comedy"]

    df = df.withColumn("Occupation_Category", when(
        conditions[0], categories[0]
        ).when(conditions[1], categories[1]).otherwise("Other"))

    log_output("transform data", df.limit(10).toPandas().to_markdown())

    return df.show()