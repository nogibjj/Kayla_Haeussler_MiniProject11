import pytest
from pyspark.sql import SparkSession
from mylib.lib import create_spark_session, end_spark_session, log_output, extract_data, query

@pytest.fixture(scope="module")
def spark_session():
    """Fixture for creating a Spark session for tests."""
    spark = create_spark_session("TestApp")
    yield spark
    end_spark_session(spark)

def test_create_spark_session(spark_session):
    """Test Spark session creation and configuration."""
    assert isinstance(spark_session, SparkSession), "Spark session was not created successfully."
    assert spark_session.conf.get("spark.app.name") == "TestApp", "Spark app name does not match."

def test_extract_data(spark_session, tmp_path):
    """Test data extraction from a CSV URL."""
    # Use a small CSV file for testing
    test_url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
    test_filepath = tmp_path / "airtravel.csv"
    
    filepath = extract_data(spark_session, test_url, str(test_filepath))
    assert filepath == str(test_filepath), "Filepath returned by extract_data does not match."
    assert test_filepath.exists(), "Extracted data file does not exist."

def test_query(spark_session, tmp_path):
    """Test query execution."""
    # Create a small DataFrame for testing
    test_data = [("California", "Democratic", True),
                 ("Texas", "Republican", False),
                 ("New York", "Democratic", True)]
    columns = ["state", "party", "incumbent"]
    test_df = spark_session.createDataFrame(test_data, columns)
    
    # Register the DataFrame as a temporary table
    test_table = "test_housedistricts"
    test_df.createOrReplaceTempView(test_table)

    # Run a query
    query_str = """
        SELECT state, 
               party, 
               SUM(CASE WHEN incumbent = true THEN 1 ELSE 0 END) AS incumbent_count, 
               SUM(CASE WHEN incumbent = false THEN 1 ELSE 0 END) AS challenger_count
        FROM test_housedistricts
        GROUP BY state, party
    """
    result_df = query(query_str, test_table)
    result = result_df.collect()

    # Validate the result
    assert len(result) == 3, "Query result does not have the expected number of rows."
    assert result[0]["incumbent_count"] == 1, "Incumbent count does not match expected value."
    assert result[1]["challenger_count"] == 1, "Challenger count does not match expected value."

def test_log_output(tmp_path):
    """Test logging of output."""
    log_file = tmp_path / "test_log.md"
    global LOG_FILE
    LOG_FILE = str(log_file)  # Override LOG_FILE for the test
    
    log_output("test_operation", "Test output for logging.", query="SELECT * FROM test_table")
    with open(log_file, "r") as f:
        content = f.read()
    
    assert "test_operation" in content, "Log output does not contain the operation name."
    assert "Test output for logging." in content, "Log output does not contain the expected output."
    assert "SELECT * FROM test_table" in content, "Log output does not contain the query."
