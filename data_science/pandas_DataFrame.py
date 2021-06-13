"""
https://pandas.pydata.org/docs/reference/frame.html

DataFrame.index         The index (row labels) of the DataFrame
DataFrame.columns       The column labels of the DataFrame
DataFrame.dtypes        Return the dtypes in the DataFrame
DataFrame.values        Return a Numpy representation of the DataFrame
DataFrame.axes          [index, columns]
DataFrame.ndim          Return dimensions, 1 for array, 2 for matrix
DataFrame.size          len(index) * len(columns)
DataFrame.shape         Return a tuple representing the dimensionality of the DataFrame
DataFrame.empty         Indicator whether DataFrame is empty

DataFrame.value_counts()
  -> Return a Series containing counts of unique rows in the DataFrame
DataFrame.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)
  -> Return DataFrame with duplicate rows removed
"""

import pandas as pd

x = {'id': 'x', 'a': 11, 'b': 12, 'c': 13}
y = {'id': 'y', 'a': 21, 'b': 22, 'c': 23}
df = pd.DataFrame([x, y]).set_index('id')
print(df)

# assign value to cell
df.at['x', 'a'] = 41
df.loc['y']['b'] = 42
df.iloc[1][2] = 43
print(df)
