"""
Library Functions Using PySpark
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

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



def create_spark_session(appName):
    """ initialize spark session """
    spark = SparkSession.builder.appName(appName).getOrCreate()
    return spark

def end_spark_session(spark):
    spark.stop()
    return "stopped spark session"


def load_data(spark, file_path):
    """
    Loads a CSV file into a Spark DataFrame.
    """
    df = spark.read.csv(file_path, header=True, inferSchema=True)

    log_output("load data", df.limit(10).toPandas().to_markdown())

    return df

def data_transformation(df):
    """
    Adds a new column 'confidence_interval_range' that represents the range between 
    p90_voteshare and p10_voteshare for each candidate.
    """
    df_transformed = df.withColumn("confidence_interval_range", 
                                   col("p90_voteshare") - col("p10_voteshare"))

    log_output("transform data", df.limit(10).toPandas().to_markdown())


    return df_transformed


def run_spark_sql(df):
    """
    Executes a Spark SQL query on the DataFrame to count 
    the number of incumbents and challengers 
    by state and party.
    """
    # Create or retrieve the SparkSession
    spark = SparkSession.builder.getOrCreate()

    # Register the DataFrame as a SQL temporary view
    df.createOrReplaceTempView("election_data")

    # SQL query to count incumbents and challengers by state and party
    sql_query = """
    SELECT state, 
           party, 
           SUM(CASE WHEN incumbent = true THEN 1 ELSE 0 END) AS incumbent_count, 
           SUM(CASE WHEN incumbent = false THEN 1 ELSE 0 END) AS challenger_count
    FROM election_data
    GROUP BY state, party
    """
    result_df = spark.sql(sql_query)

    log_output("query data", spark.sql(sql_query).toPandas().to_markdown(), sql_query)

    return result_df


def save_data(df, output_path):
    """
    Saves the resulting DataFrame to the specified path.
    """
    df.write.csv(output_path, header=True, mode="overwrite")


