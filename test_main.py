"""
Test goes here

"""

import pytest
from pyspark.sql import SparkSession
from mylib import lib

# Initialize a Spark session for testing
@pytest.fixture(scope="module")
def spark():
    spark_session = SparkSession.builder \
        .appName("TestSession") \
        .master("local[1]") \
        .getOrCreate()
    yield spark_session
    spark_session.stop()

def test_create_spark_session(spark):
    assert spark is not None
    assert isinstance(spark, SparkSession)

def test_load_data(spark):
    # Assuming test data file path
    test_file_path = "data/house_district_forecast.csv"
    df = lib.load_data(spark, test_file_path)
    assert df is not None
    assert df.count() > 0  # Check that there are rows in the DataFrame
    assert len(df.columns) > 0  # Check that there are columns in the DataFrame

def test_data_transformation(spark):
    # Create a sample DataFrame for testing
    data = [("A", 10), ("B", 20), ("A", 30), ("B", 40)]
    df = spark.createDataFrame(data, ["group_column", "numeric_column"])

    # Run transformation
    transformed_df = lib.data_transformation(df)

    # Check that the transformation worked as expected
    assert transformed_df is not None
    assert "average_value" in transformed_df.columns
    assert transformed_df.count() == 2  # Check that there are 2 groups (A and B)

def test_run_spark_sql(spark):
    # Create a sample DataFrame for testing
    data = [("A", 10), ("B", 20), ("A", 30), ("B", 40)]
    df = spark.createDataFrame(data, ["group_column", "numeric_column"])

    # Run SQL query
    result_df = lib.run_spark_sql(df)

    # Check that the SQL query returned expected results
    assert result_df is not None
    assert "total_value" in result_df.columns
    assert "average_value" in result_df.columns
    assert result_df.count() == 2  # Check that there are 2 groups (A and B)

def test_save_data(spark, tmp_path):
    # Create a sample DataFrame for testing
    data = [("A", 10), ("B", 20)]
    df = spark.createDataFrame(data, ["group_column", "numeric_column"])

    # Save to a temporary directory
    output_path = tmp_path / "output.csv"
    lib.save_data(df, str(output_path))

    # Check that the file was created
    assert output_path.exists()
    assert output_path.is_file()
