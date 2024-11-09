"""

"""

from mylib import lib


if __name__ == "__main__":
    
    # initialize Spark
    spark = lib.create_spark_session()

    # load data
    df = lib.load_data(spark, "data/house_district_forecast.csv")

    # transform data
    transformed_df = lib.data_transformation(df)

    # run SQL query
    sql_result_df = lib.run_spark_sql(df)

    # save results
    lib.save_data(sql_result_df, "output/processed_data.csv")

    # stop Spark session
    spark.stop()