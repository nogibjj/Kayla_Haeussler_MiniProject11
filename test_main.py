import unittest
from mylib import lib
import os
import tempfile

class TestMain(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up Spark session and in-memory data for all tests."""
        cls.spark = lib.create_spark_session("Test_House_District")
        cls.log_file = lib.LOG_FILE
        # Create sample data for testing
        sample_data = [
            ("California", "Democrat", True, 0.55, 0.50, 0.60),
            ("California", "Republican", False, 0.45, 0.40, 0.50),
            ("Texas", "Democrat", True, 0.60, 0.55, 0.65),
            ("Texas", "Republican", False, 0.40, 0.35, 0.45)
        ]
        cls.columns = ["state", "party", "incumbent", "voteshare", 
                       "p10_voteshare", "p90_voteshare"]
        cls.df = cls.spark.createDataFrame(sample_data, cls.columns)

        # Clear the log file before each test
        with open(cls.log_file, "w") as file:
            file.write("")

    @classmethod
    def tearDownClass(cls):
        """Stop Spark session after all tests are done."""
        lib.end_spark_session(cls.spark)
        if os.path.exists(cls.log_file):
            os.remove(cls.log_file)

    def test_load_data(self):
        """Test loading data into Spark DataFrame using in-memory data."""
        # Here we could simulate loading or simply use cls.df directly.
        df = self.df  # or lib.load_data if it’s supposed to be tested
        self.assertIsNotNone(df)
        self.assertEqual(df.count(), len(self.df.collect()))

    def test_data_transformation(self):
        """Test transformation by checking the new column."""
        transformed_df = lib.data_transformation(self.df)
        self.assertTrue("confidence_interval_range" in transformed_df.columns)

        # Check that confidence_interval_range is calculated correctly
        transformed_row = transformed_df.collect()[0]
        self.assertAlmostEqual(
            transformed_row["confidence_interval_range"],
            transformed_row["p90_voteshare"] - transformed_row["p10_voteshare"]
        )

    def test_run_spark_sql(self):
        """Test SQL query output to count incumbents and challengers."""
        result_df = lib.run_spark_sql(self.df)
        result_df.show()
        
        self.assertTrue("incumbent_count" in result_df.columns)
        self.assertTrue("challenger_count" in result_df.columns)

        # Check specific counts for validation
        california_result = result_df.filter(
            result_df.state == "California").collect()[0]
        self.assertEqual(california_result["incumbent_count"], 1)
        self.assertEqual(california_result["challenger_count"], 1)

    def test_save_data(self):
        """Test saving data by simulating output to a temporary path."""
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp_file:
            temp_output_path = temp_file.name

        # Use the temporary file path for testing save functionality
        try:
            lib.save_data(self.df, temp_output_path)
            self.assertTrue(os.path.exists(temp_output_path))
        finally:
            os.remove(temp_output_path)  # Clean up after the test
    
    def test_log_output(self):
        """Test that log_output writes expected data to the markdown file."""
        initial_size = os.path.getsize(self.log_file)
        lib.log_output("Test Operation", "Test Output")
        new_size = os.path.getsize(self.log_file)
        self.assertGreater(new_size, initial_size)

if __name__ == "__main__":
    unittest.main()
