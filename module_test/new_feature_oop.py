# module_test/new_feature_opp.py

from pandas import DataFrame

# Refactor this functional approach into an object oriented approach?
# (using classes)

class DataFrameProcessor():
    def __init__(self, df):
        """ 
        Params (my_df) a DataFrame with a column called "abbrev" that has state abbreviations.
        """
        self.df = df


    def add_state_names_column(self):
        """
        Add a column of corresponding state names to dataframe.

        Return a copy of the original dataframe, but with an extra column.
        """
        names_map = {'CA': 'Cali', 'CO': 'Colo', 'CT': 'Conn'}

        # This way will return a transformed copy of the dataframe
        # new_df = self.df.copy()
        # new_df['Name'] = new_df['abbrev'].map(names_map)
        # return new_df

        # This way will muntate the existing df
        self.df['Name'] = self.df['abbrev'].map(names_map)



if __name__ == "__main__":
    df = DataFrame({"abbrev": ['CA', 'CO', 'CT', 'DC', 'TX']})
    # print(df.head())

    # mapped_df = add_state_names_column(df)
    # print(mapped_df.head())

processor = DataFrameProcessor(df=df)
print(processor.df.head())
processor.add_state_names_column()
print(processor.df.head())

# If I want to return the transformed copy
# new_df = processor.add_state_names_column()
# print(new_df.head())