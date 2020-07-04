
# Write some code using unittest to test our add_state_names_column() function works as desired


import unittest
from pandas import DataFrame
from module_test.new_feature import add_state_names_column


class TestNewFeature(unittest.TestCase):

    def test_add_state_names(self):

        df = DataFrame({"abbrev": ['CA', 'CO', 'CT', 'DC', 'TX']})
        # ensure our test is setup properly
        self.assertEqual(len(df.columns), 1)
        self.assertEqual(list(df.columns), ['abbrev'])
        self.assertEqual(df.iloc[0]['abbrev'], 'CA')

        mapped_df = add_state_names_column(df)
        self.assertEqual(len(mapped_df.columns), 2)
        self.assertEqual(list(mapped_df.columns), ['abbrev', 'Name'])
        self.assertEqual(mapped_df.iloc[0]['abbrev'], 'CA')
        self.assertEqual(mapped_df.iloc[0]['Name'], 'Cali')


if __name__ == '__main__':
    unittest.main() # Invoking all of our test class's methods