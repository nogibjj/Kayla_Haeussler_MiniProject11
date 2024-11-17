"""
Import and run functions from library for ETL pipeline
"""

from mylib.lib import *


if __name__ == "__main__":
    
    # initialize Spark
    spark = create_spark_session('House_District')

    # extract data
    df = extract_data(spark, "data/house_district_forecast.csv")

    # transform data
    transformed_df = transform_data(df)

    # run SQL query
    sql_result_df = run_spark_sql(df)

    # save results
    load_data(sql_result_df, "output/processed_data.csv")

    # stop Spark session
    spark.stop()