"""
https://pandas.pydata.org/docs/index.html

Series.unique()               Return unique values of Series object
Series.nunique(dropna=True)   Return number of unique elements in the object

DataFrame.index               The index (row labels) of the DataFrame
DataFrame.columns             The column labels of the DataFrame
DataFrame.dtypes              Return the dtypes in the DataFrame
DataFrame.values              Return a Numpy representation of the DataFrame
DataFrame.axes                [index, columns]
DataFrame.ndim                Return dimensions, 1 for array, 2 for matrix
DataFrame.size                len(index) * len(columns)
DataFrame.shape               Return a tuple representing the dimensionality of the DataFrame
DataFrame.empty               Indicator whether DataFrame is empty
DataFrame.value_counts()      Return a Series containing counts of unique rows in the DataFrame

----- Data Cleaning -----
DataFrame.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)
  -> Return DataFrame with duplicate rows removed
DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
  -> Remove missing values
DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None)
  -> Fill NA/NaN values using the specified method
DataFrame.drop(labels=None, axis=0, index=None, columns=None, level=None, inplace=False, errors='raise')
  -> Drop specified labels from rows or columns
pandas.to_numeric(arg, errors='raise', downcast=None)
  -> Convert argument to a numeric type
  -> dtypedata type, or dict of column name -> data type
DataFrame.astype(dtype, copy=True, errors='raise')
  -> Cast a pandas object to a specified dtype dtype.

----- Data Manipulation -----
DataFrame.nunique(axis=0, dropna=True)
  -> Count distinct observations over requested axis
DataFrame.merge(right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)
  -> Merge DataFrame or named Series objects with a database-style join
pandas.merge(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)
  -> Merge DataFrame or named Series objects with a database-style join

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

df['description'] = df['description'].str.replace('$', '')

