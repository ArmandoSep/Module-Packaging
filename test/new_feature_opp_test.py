
# Write some code using unittest to test our split_date() function works as desired


import unittest
from pandas import DataFrame
from module_test.new_feature_oop import DataFrameProcessor


class TestNewFeature2(unittest.TestCase):

    def test_add_state_names(self):
        
        df = DataFrame({"abbrev": ['CA', 'CO', 'CT', 'DC', 'TX']})
        processor = DataFrameProcessor(df=df)
        # ensure our test is setup properly
        self.assertEqual(len(processor.df.columns), 1)
        self.assertEqual(list(processor.df.columns), ['abbrev'])
        self.assertEqual(processor.df.iloc[0]['abbrev'], 'CA')


        processor.add_state_names_column()

        self.assertEqual(len(processor.df.columns), 2)
        self.assertEqual(list(processor.df.columns), ['abbrev', 'Name'])
        self.assertEqual(processor.df.iloc[0]['abbrev'], 'CA')
        self.assertEqual(processor.df.iloc[0]['Name'], 'Cali')


if __name__ == '__main__':
    unittest.main() # Invoking all of our test class's methods