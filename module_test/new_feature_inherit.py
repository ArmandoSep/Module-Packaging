# module_test/new_feature_inherit.py

from pandas import DataFrame

# How can we use an inheritance approach?

class CustomFrame(DataFrame):
    """
    A DataFrame with a column called "abbrev" that has state abbreviations.
    """

    # Don't need this if we wont do any modifications
    # def __init__(self, data, additional_atrribute):
    #     super().__init__(data)
    #     self.additional_atrribute = additional_atrribute

    def add_state_names_column(self):
        """
        Add a column of corresponding state names to dataframe.
        """
        names_map = {'CA': 'Cali', 'CO': 'Colo', 'CT': 'Conn'}
        self['Name'] = self['abbrev'].map(names_map)


if __name__ == "__main__":
    # df = DataFrame({"abbrev": ['CA', 'CO', 'CT', 'DC', 'TX']})
    # print(df.head())

    # mapped_df = add_state_names_column(df)
    # print(mapped_df.head())

    custom_frame = CustomFrame({"abbrev": ['CA', 'CO', 'CT', 'DC', 'TX']})
    print(custom_frame.head())
    custom_frame.add_state_names_column()
    print(custom_frame.head())