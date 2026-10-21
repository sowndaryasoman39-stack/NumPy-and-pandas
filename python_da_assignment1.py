"""Python DA Assignment 1: Data Analysis using NumPy and Pandas"""
import numpy as np
import pandas as pd

# =====================================================================
# PART 1: NUMPY ARRAY OPERATIONS
# =====================================================================
print("=" * 60)
print("NUMPY ARRAY OPERATIONS")
print("=" * 60)

# 1. Create a 1D array
temperatures_w1 = np.array([22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9])
print("Week 1 temperatures:", temperatures_w1)

# 2. Inspection and properties
print("\nShape:", temperatures_w1.shape)
print("Data type:", temperatures_w1.dtype)
print("Number of elements:", temperatures_w1.size)

# 3. Array operations
temperatures_f = (temperatures_w1 * 9 / 5) + 32
print("\nTemperatures in Fahrenheit:", temperatures_f)
print("Maximum:", temperatures_w1.max())
print("Minimum:", temperatures_w1.min())
print("Mean:", temperatures_w1.mean())

# 4. Slicing and indexing
print("\nFirst three days:", temperatures_w1[:3])
print("Weekend (last two days):", temperatures_w1[-2:])
print("Middle three days:", temperatures_w1[2:5])

# 5. 2D array
temperatures = np.array([
    [22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9],  # Week 1
    [19.2, 22.5, 21.3, 24.0, 23.5, 22.8, 20.1],  # Week 2
])
print("\n2D temperatures array:\n", temperatures)

# 6. Inspect and slice the 2D array
print("\nShape:", temperatures.shape)
print("Data type:", temperatures.dtype)
print("Total number of elements:", temperatures.size)
print("Week 1:", temperatures[0])
print("Week 2:", temperatures[1])
print("Weekends (last two days) of both weeks:\n", temperatures[:, -2:])

# =====================================================================
# PART 2: PANDAS SERIES
# =====================================================================
print("\n" + "=" * 60)
print("PANDAS SERIES")
print("=" * 60)

# 1. Create Series
marks = pd.Series([95, 92, 89, 85, 80],
                  index=['Rank1', 'Rank2', 'Rank3', 'Rank4', 'Rank5'])
print(marks)

# 2. Indexing and slicing
print("\nMark of 1st rank (by label):", marks['Rank1'])
print("Mark of 1st rank (by integer position):", marks.iloc[0])
print("Top 3 ranks using loc:\n", marks.loc['Rank1':'Rank3'])
print("Mark of 3rd rank using iloc:", marks.iloc[2])
print("Ranks with marks > 90:\n", marks[marks > 90])

# 3. Manipulating
marks['Rank1'] = 100
print("\nAfter changing Rank1 to 100:\n", marks)
marks = marks.drop('Rank5')
print("\nAfter removing Rank5:\n", marks)
cgpa = marks / 10
print("\nCGPA (marks / 10):\n", cgpa)

# =====================================================================
# PART 3: PANDAS DATAFRAME
# =====================================================================
print("\n" + "=" * 60)
print("PANDAS DATAFRAME")
print("=" * 60)

# 1. Create DataFrame
transactions = pd.DataFrame({
    'TransactionID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'ProductCategory': ['Electronics', 'Clothing', 'Electronics', 'Furniture',
                        'Clothing', 'Electronics', 'Furniture', 'Clothing',
                        'Furniture', 'Electronics'],
    'Region': ['North', 'South', 'North', 'East', 'West',
               'North', 'East', 'West', 'South', 'North'],
    'Amount': [200, 150, 300, 450, 200, 250, 300, 180, 350, 400],
})

# 2. Data exploration
print("\nDataFrame:\n", transactions)
print("\nHead:\n", transactions.head())
print("\nTail:\n", transactions.tail())
print("\nShape:", transactions.shape)
print("Column names:", list(transactions.columns))
print("\nData types:\n", transactions.dtypes)
print("\nInfo:")
transactions.info()

print("\nProductCategory and Amount:\n", transactions[['ProductCategory', 'Amount']])
print("\nLast 3 columns (iloc):\n", transactions.iloc[:, -3:])
print("\nNorth region and Amount > 200:\n",
      transactions[(transactions['Region'] == 'North') & (transactions['Amount'] > 200)])
print("\nValue counts of ProductCategory:\n", transactions['ProductCategory'].value_counts())
print("\nUnique regions:", transactions['Region'].unique())
print("\nMean amount by region:\n", transactions.groupby('Region')['Amount'].mean())

# 3. Manipulating the DataFrame
transactions.loc[transactions['TransactionID'] == 102, 'Amount'] = 165
print("\nAfter updating TransactionID 102 to 165:\n", transactions)

transactions['Discount'] = transactions['Amount'] * 0.10
print("\nAfter adding Discount column:\n", transactions)

transactions = transactions[transactions['TransactionID'] != 109]
print("\nAfter removing TransactionID 109:\n", transactions)

transactions = transactions.drop(columns='Discount')
print("\nAfter deleting Discount column:\n", transactions)
