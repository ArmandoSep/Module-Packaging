
# Write some code using unittest to test our split_date() function works as desired


import unittest
from pandas import DataFrame
from module_test.my_mod import split_date


class TestTest(unittest.TestCase):

    def test_split_date(self):

        df = DataFrame({'Date': ['12/feb/2020']})
        # ensure our test is setup properly
        self.assertEqual(len(df.columns), 1)
        self.assertEqual(list(df.columns), ['Date'])
        self.assertEqual(df.iloc[0]['Date'], '12/feb/2020')


        new_df = split_date(df)
        self.assertEqual(len(new_df.columns), 4)
        self.assertEqual(list(new_df.columns), ['Date', 'Day', 'Month', 'Year'])
        self.assertEqual(new_df.iloc[0]['Day'], 12)
        self.assertEqual(new_df.iloc[0]['Month'], 2)


if __name__ == '__main__':
    unittest.main() # Invoking all of our test class's methods
