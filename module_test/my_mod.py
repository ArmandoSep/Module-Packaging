
import pandas as pd


def split_date(X):
  df = pd.DataFrame({'Date': [X]})
  df['Date'] = pd.to_datetime(X, infer_datetime_format=True)
  df['Day'] = df['Date'].dt.day
  df['Month'] = df['Date'].dt.month
  df['Year'] = df['Date'].dt.year
  return df


if __name__ == "__main__":
    # only run the code below IF this script is invoked from the command-line
    # not if it is imported from another script
    print('Please enter the date')
    X = input()
    split_date(X)


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