"""
https://pandas.pydata.org/docs/index.html

Series.unique()               Return unique values of Series object
Series.nunique(dropna=True)   Return number of unique elements in the object
Series.apply(func, convert_dtype=True, args=(), **kwds)
    -> Invoke function on values of Series

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
DataFrame.astype(dtype, copy=True, errors='raise')
    -> Cast a pandas object to a specified dtype dtype.
pandas.to_numeric(arg, errors='raise', downcast=None)
    -> Convert argument to a numeric type
    -> dtypedata type, or dict of column name -> data type
    
----- Data Manipulation -----
DataFrame.nunique(axis=0, dropna=True)
    -> Count distinct observations over requested axis
DataFrame.merge(right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)
    -> Merge DataFrame or named Series objects with a database-style join
pandas.merge(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)
    -> Merge DataFrame or named Series objects with a database-style join
pandas.pivot_table(data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All', observed=False)
    -> Create a spreadsheet-style pivot table as a DataFrame
    -> aggfuncfunction, list of functions, dict, default numpy.mean

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

'----- grouby & aggregate -----'
df = pd.DataFrame(
    {
        "A": [1, 1, 2, 2, 2],
        "B": [1, 2, 3, 5, 10],
        "C": [0.362838, 0.227877, 1.267767, -0.562860, 0],
    }
)
df.groupby('A').agg({'B': ['min', 'max'], 'C': 'sum'})
grouped = df.groupby('A')
grouped["B"].agg([lambda x: x.max() - x.min(), lambda x: x.median() - x.mean()])
df.groupby('A').agg(get_min=pd.NamedAgg(column="B", aggfunc="min"), median_mean=pd.NamedAgg(column="B", aggfunc=lambda x: x.median() - x.mean()))
