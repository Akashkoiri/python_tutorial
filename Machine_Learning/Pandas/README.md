# Panadas Notes

## [1] How to import pandas?

```python
import pandas as pd
```

### [#] How to see pandas & it's dipendencis virsions?

```python
# pandas virsion
pd.__version__

# dipendencis virsion
pd.show_versions()
```

### [2] What is a dataframe in pandas?

A dataframe is a 2 dimensional data structure, or a combination of series objects, like a 2 dimensional array, or a table with rows and columns.

### [3] How to create a datafreame?

```python
# 1. Create a DataFrame using a 2D Array
data = [[1,2],[3,4],[5,6],[7,8]]
column_name = ['Temp', 'Activity']
df = pd.DataFrame(data=data, columns=column_name)


# 2. Create a DataFrame using a Dictionary
data = {'Temp':[1,3,5,7], 'Activity':[2,4,6,8]}
df = pd.DataFrame(data=data)

# 3. Create a dataframe filled with random float values using numpy
pd.DataFrame(data=np.random.rand(5,3), columns=list('ABC'))

# 4. Create a dataframe filled with random int values using numpy
pd.DataFrame(np.random.randint(low=0, high=101, size=(3,4)), columns=column_name)

# Create a quick dataframe using values copied in the clipboard from a excel file
df = pd.read
```

### [4] How to read a saved dataset

```python
# For reading csv files
df =  pd.read_csv('monthly/annual.csv')

# For reading excel files
df = pd.read_excel('monthly/monthly.xlsx')
# set custom index
df = pd.read_excel('monthly/monthly.xlsx').set_index('Name')

# For reading from a link
df = pd.read_table('http://bit.ly/chiporders')
```

### [#] How to save memory when importing csv files?

```py
df = pd.read_csv('annual_price.csv', usecols=['Price'], dtype={'Price':'object'})
```

### [#] How to define datatypes of a column during importing the files?

```py
df = pd.read_csv('monthly.csv', dtype={'column_1':float})
```

### [#] How to get info about a dataframe?

```py
df.info(memory_usage='deep')
```

### [#] How to get the shape of the dataframe?

```py
df.shape
```

### [5] How to write a dataframe to a file?

```python
# For saving as a csv file without the index column
df.to_csv('annual.csv', index=False)

# For saving as an excel file with only this columns
df.to_excel('annual.xlsx', columns=['name','AvgBill'])

# Give custom column name
df.to_excel('annual.xlsx', header=['new_name', 'newBill']
```

## [#] Extract data

---

### [6] What is a series object?

=> One of the column of a dataframe is called series object.

### [#] How to create a series?

```py
sr = pd.Series([1,2,3,4,5])

years = [90,91,92,93,94,95]
f1 = {91:8,90:9,92:13,93:8,94:5} # We can specify each value by the index number
firm1 = pd.Series(f1,index=years)
```

### [7] How to extract a series object or a column from a dataframe?

```python
# 'Activity' is a column name
df['Activity']

df.Activity
```

### [#] How to reverse a dataframe row wise?

```python
df = df.loc[::-1].reset_index(drop=True)
```

### [#] How to reverse a dataframe columns wise?

```python
df = df.loc[:,::-1]
```

### [8] How to extract a row?

```python
# It gives us a series
df.loc[2]
# It gives us a dataframe
df.loc[[2]]


# 1st Method iloc:

# prints only the 6th row
df.iloc[6]
# prints from 0 to 6th
df.iloc[:6]


# 2nd Method loc:

#prints
df.loc[]


df[0:6]
```

### [9] How to extract a cell?

```python
# (Row=3rd index,column='Name')
df['Name'][3]
df.Name[3]

# (Row=3rd index,column=2nd  index)
df.loc[3][2]
```

### [#] How can we get the column's index?

```python
columns = df.columns
columns[0]
```

### [#] How to know all columns datatype?

```py
df.dtypes
```

### [#] How to extract row according to datatypes?

```py
df.select_dtypes(include='float')
df.select_dtypes(exclude=['object','number','datetime'])
```

### [10] How to extract multiple series?

```python
# We would get a dataframe
df[['Temp','Activity']]
```

### [11] How to Filter data?

```python
# First write the shell (df[])
### inside the shell write your conditions (df['Temp']>15)

# Single Condition
df[df['Temp']>10]
df[df['Temp']>=10]

# Filter by 10
df[df['Temp']==10]
# Filter by 10 and 20
df[ df['Temp'].isin([10,20]) ]

#Filter without 8
df[df['Activity']!=8]
#Filter without 7 and 8
df[ ~df['Activity'].isin([10,20]) ]


# Double Conditions
df[ (df['Temp']>10) & (df['Activity']==8) ]
df[ (df['Temp']>5) | (df['Activity']<10) ]


```

### [12] How to sort values?

```python
# Ascending order
df.sort_values('Temp')

# Descending order
df.sort_values('Temp',ascending=False)
```

## [#] Alterate data

---

### [#] How to set custom index?

```python
df = pd.DataFrame(data=data, index=['A','B','C','D'])
```

### [13] How to add a new column?

```python
df['Duration'] = df['Temp'] + df['Activity']
```

### [14] How to add an empty column OR a column filled with same charecters?

```python
# Empty column
df1['Empty'] = ''

# Temporary values
df1['Empty'] = None

# Same charecter
df1['Empty'] = 0
```

### [15] How to change a column's name?

```python
# One or few columns
df = df.rename(columns = {'Temp':'Temp(*C)','Duration':'Duration(Hours)'})

# All the columns
df.columns = ['A','B','C']

# Replace something in all of the columns
df.columns = df.columns.str.replace(' ','_')

# All columns name with a prefix
df = df.add_prefix('x_')

# All columns name with a sufix
df = df.add_suffix('_y')
```

### [#] how to change a columns data type?

```py
# One column at a time
df2.col_three = pd.to_numeric(df2.col_three)
df2.col_three = df2.col_three.astype(int)

# More than one columns at a time
df2 = df2.astype({'col_one':'int', 'col_two':'float'})
```

### [#] How to fix Nan values?

```py
df2.isna()
df2.fillna(0)
df2.dropna(axis='columns')
df2.dropna(axis=1)
# Threshold is used to set a limit of nan values (when we have more than 3 NaN values in a row)
df2.dropna(threshold=3)
```

### [#] How to fix all the bad values of a columns?

```py
df2 = df2.apply(pd.to_numeric, errors='coerce').fillna(0)
```

### [16] How to reset the indexing?

```python
# Use it when you know that the  result will be printing in a bad indexing order

# This will also saves the previous index in a new column
df[df['Temp'].isin([20,30])].reset_index()

# This will not save any previous index in any new column
df[df['Temo'].isin([20,30]),rest_index(drop=True)]
```

## [#] String Functions

---

### [17] How to change a whole string series to lowercase?

```python
# If we want to permanently change the names to lowercase
df['Name'] = df['Name'].str.lower()

# If we want to keep the original series
df['lowerCase_Name'] = df['Name'].str.lower()

# Convert to uppercase
df.Name.str.upper()
```

### [18] How to extract matching strings?

```python
df[ df['Name'].str.contains('.ak.') ]
```

### [#] How to convert boolien valus to 0,1 ?

```py
# True = 1 , False = 0
df.item_name.str.contains('Chicken').astype(int)
```

### [#] How to replace a string series?

```python
df.Date = df.Date.str.replace('-','/')
df.Name.str.replace('[','').str.replace(']','')
# OR
df.Name.str.replace('[\[\]]', '')

# How to replcae all types of bad characters at once.
df = df.replace('[^\d.]', '', regx=True).astype(float)

# Extract dates from a string
df.Description = 
```

### [#] How to use str.title

```py

```

### [#] How to split a series into two columns?

```py
df.Price = df.Date.str.split(',').str.get(1)
df.Date = df.Date.str.split(','),str.get(0)
```

### [#] How to slice a string

```py
df.Name.str.slice(-5, -3)
```

### [19] How to concat two DataFrames?

```python
# Add one on top of another one
# The column's name & number should same
# only the data will be deffrent
df1 = pd.DataFrame(data=data1, columns=columns)
df2 = pd.DataFrame(data=data2, columns=columns)

df3 = pd.concat([df1,df2]).reset_index(drop=True)
```

### [#] How to concat more than one files in a folder with same name like(name1,name2)

```py
from glob import glob

# Row wise
stock_files = sorted(glob('data/stocks*.csv'))  
# It will give a list ['data/stocks1.csv','data/stocks2.csv','data/stocks3.csv']
pd.concat((pd.read_csv(file) for file in stock_files), ignore_index=True) 

# column wise
drinks_file = sorted(glob('data/drinks*.csv'))
pd.concat((pd.read_csv(file) for file in drinks_files), axis='columns')
```

### [20] How to merge two DtaFrames?

```python
# Side by side
df
df1 = pd.DataFrame(data={'Gender':['male','female'],'stream':['science','arts']})

df2 = df.merge(df1,how='left',on='Gender')
```

### [#] How to split a dataframe into two random subsets?

```py
len(movies)
movies1 = movies.sample(frac=0.75, random_state=1234)
movies2 = movies.drop(movies1.index)
```

### [21] How to add a column or series on the left side of the DataFrame?

```python

```

## Aggregatios

---

### [#] How to know that how many rows and columns are there in a dataframe?

```python
df.shape()
```

### [22] How to get the stats of a DataFrame?

```python
# To get all stats
df3.describe()

# To get a specific type of stat
df3.min()

# To get a stat of a specific column
df3['Age'].min()
df3.Age.min()
```

### [23] How to find that how many times a record or a series_data has occured?

```python
# Record or Row
# It helps us to find any duplicate records
df3.value_counts()

# Specific column
df3['Temp'].value_counts()

# Extract largest 5 values
df3.nlargest(3).index
```

### [24] How to extract values of a serries by Grouping them?

```python
# Group by Gender and mean of Age
df3.groupby('Gender')['Age'].mean()

# This will work and get the mean of Age column
# Because there was only one int columns
df.groupby('Gender').mean()
# If there were more than one intiger column then it will do the mean with both of the columns

# How to groupby two columns and then perform two diffrent aggregations.
df.groupby(['Gender','Name'])['Age'].agg('mean','max')
# This will first group according to Gender & then in the gender group it will group according to same names
```
### [#] How to delete the rows,columns?

```py
# temporary remove row
df = df.drop(0) # 0 is index no.
# permanent remove row
df.drop(0, inplace=True)
# multiple remove row
df.drop([1,3,5,7], inplace=True)

# drop column
df.drop('Name', axis=1, inplace=True)
df = df.drop(2, axis=1) # 2 is Column name not index

del df['Price']
```

## Working with date & time

---

### Convert string series to a datetime series

```py
df.Date = df.Date.astype('datetime64')

# format is used to tell pandas that how we are giving dates
pd.to_datetime(df.Date, format='%d/%m/%Y')
# %y = 20  and  %Y = 2020
df.Date = pd.to_datetime('2-9-2022', dayfirst=True)
df.Date = pd.to_datetime(df.Date, errors='coerce')

# After we convert the series into a datetime then we can change the format on our own
df.Date.dt.strftime('%d-%m-%Y')
```

### How to find all the rows & columns according to date & time ?

```py
# Bydefault datetime will take (mm/dd/yy) & Gives us (yyyy/mm/dd)
# 1/1/2000 = month/day/year
ts = pd.to_datetime('1/1/200') # called timestamp
df.loc[df.time >= ts, :]
```

### We can find the earliest date & the most recent date by using min & max aggregations?

```py
df1.Date.min()
df1.Date.max()
```

### Benifits of using .to_datetime

```py
# Source : https://www.pandas.pydata.org/pandas-docs/stable/api.html#datetimelike-proporties
df.Date.dt.date
df.Date.dt.time
df.Date.dt.year
df.Date.dt.month
df.Date.dt.day
df.Date.dt.hour
df.Date.dt.minute
df.Date.dt.second
df.Date.dt.weekday_name
df.Date.dt.weekday
df.Date.dt.dayofyear
```

## Plotting

---

### [25] How to create a plot?

```python
# By default graph takes the index as X-Axis

# Takes all the intiger columns
df2.plot()

# Takes only the specified intiger column
df2['Marks'].plot()
df3.plot(y='Marks')

# Create two graph lines
df3[['Age','Marks']].plot()

# Define X & Y Axis in your own
df3[['Age','Marks']].plot(x='Age',y='Marks')

# Create a scatter plot (doted graph without lines)
df3[['Age','Marks']].plot(x='Age',y='Marks',kind='scatter')

# Adjust the output size of the graph
df3.plot(figsize=(10,6))
```

### [26] How to create histograms?

```python
# Helps us to identify outliers
df3.hist(figsize=(10,6))
```