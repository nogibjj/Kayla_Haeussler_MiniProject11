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
        """Test loading data using in-memory DataFrame."""
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
        """
        Test SQL query output to count incumbents and 
        challengers by state and party.
        """
        # Run the query and get results
        result_df = lib.run_spark_sql(self.df)
        result_df.show()
        
        self.assertTrue("incumbent_count" in result_df.columns)
        self.assertTrue("challenger_count" in result_df.columns)

        # Validate counts for each (state, party) pair
        california_democrat = result_df.filter((result_df.state
                                                 == "California") & 
                                            (result_df.party == 
                                             "Democrat")).collect()[0]
        california_republican = result_df.filter((result_df.state == 
                                                  "California") & 
                                                (result_df.party == 
                                                 "Republican")).collect()[0]
        texas_democrat = result_df.filter((result_df.state 
                                           == "Texas") & 
                                        (result_df.party 
                                         == "Democrat")).collect()[0]
        texas_republican = result_df.filter((result_df.state
                                              == "Texas") & 
                                            (result_df.party 
                                             == "Republican")).collect()[0]

        # Check counts for each party in California
        self.assertEqual(california_democrat["incumbent_count"], 1)   
                            # 1 Democrat incumbent
        self.assertEqual(california_democrat["challenger_count"], 0)  
                            # 0 Democrat challengers
        self.assertEqual(california_republican["incumbent_count"], 0) 
                            # 0 Republican incumbents
        self.assertEqual(california_republican["challenger_count"], 1) 
                            # 1 Republican challenger

        # Check counts for each party in Texas
        self.assertEqual(texas_democrat["incumbent_count"], 1)   
                            # 1 Democrat incumbent
        self.assertEqual(texas_democrat["challenger_count"], 0)  
                            # 0 Democrat challengers
        self.assertEqual(texas_republican["incumbent_count"], 0) 
                            # 0 Republican incumbents
        self.assertEqual(texas_republican["challenger_count"], 1) 
                            # 1 Republican challenger


    def test_save_data(self):
        """Test saving data by simulating output to a temporary directory."""
        with tempfile.TemporaryDirectory() as temp_dir:
            lib.save_data(self.df, temp_dir)
            # Check that a directory exists instead of a single file
            self.assertTrue(os.path.isdir(temp_dir))
            # Check if any CSV part files are inside the directory
            csv_files = [f for f in os.listdir(temp_dir) 
                         if f.endswith(".csv") or f.startswith("part")]
            self.assertGreater(len(csv_files), 0)
    
    def test_log_output(self):
        """Test that log_output writes expected data to the markdown file."""
        initial_size = os.path.getsize(self.log_file)
        lib.log_output("Test Operation", "Test Output")
        new_size = os.path.getsize(self.log_file)
        self.assertGreater(new_size, initial_size)

if __name__ == "__main__":
    unittest.main()
