""" 
Library Functions Using PySpark
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import when, cols


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
    df_transformed = df_filtered.groupBy("group_column").agg(avg("numeric_column").alias("average_value"))
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
