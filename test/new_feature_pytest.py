
# Write some code using pytest to test our add_state_names_column() function works as desired


from pandas import DataFrame
from module_test.new_feature import add_state_names_column


def test_add_state_names():

    df = DataFrame({"abbrev": ['CA', 'CO', 'CT', 'DC', 'TX']})
    # ensure our test is setup properly //
    # self.assertEqual(len(df.columns), 1)
    # self.assertEqual(list(df.columns), ['abbrev'])
    # self.assertEqual(df.iloc[0]['abbrev'], 'CA')
    assert len(df.columns) == 1
    assert list(df.columns) == ['abbrev']
    assert df.iloc[0]['abbrev'] == "CA"


    mapped_df = add_state_names_column(df)
    # self.assertEqual(len(mapped_df.columns), 2)
    # self.assertEqual(list(mapped_df.columns), ['abbrev', 'Name'])
    # self.assertEqual(mapped_df.iloc[0]['abbrev'], 'CA')
    # self.assertEqual(mapped_df.iloc[0]['Name'], 'Cali')
    assert len(mapped_df.columns) == 2
    assert list(mapped_df.columns) == ['abbrev', 'Name']
    assert mapped_df.iloc[0]['abbrev'] == 'CA'
    assert mapped_df.iloc[0]['Name'] == 'Cali'

