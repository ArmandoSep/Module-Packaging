
import pandas as pd


def split_date(X):
  """
  This function will split the date from any format into day, month and year organized in columns.
  
  The function expects a DataFrame with a single column named 'Date'.
  """
  X['Date'] = pd.to_datetime(X['Date'], infer_datetime_format=True)
  X['Day'] = X['Date'].dt.day
  X['Month'] = X['Date'].dt.month
  X['Year'] = X['Date'].dt.year
  return X


if __name__ == "__main__":
    # only run the code below IF this script is invoked from the command-line
    # not if it is imported from another script
    print('Please enter the date')
    X = input()
    df = pd.DataFrame({'Date': [X]})
    split_date(df)


# Second helper function
def list_to_column(a, b):
  a = a.split(', ')
  a = list(a)
  a = pd.Series(a)
  df = pd.DataFrame({b: a})
  return df


if __name__ == "__main__":
    # only run the code below IF this script is invoked from the command-line
    # not if it is imported from another script
    print('Write the values, separated with comma and space (value1, value2, etc')
    data = input()
    print('Write the column name')
    name = input()
    list_to_column(data, name)