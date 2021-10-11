# =================================================================
# Class_Ex1:
# From the data table above, create an index to return all rows for
# which the phylum name ends in "bacteria" and the value is greater than 1000.
# ----------------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame({'value':[632, 1638, 569, 115, 433, 1130, 754, 555],
                     'patient':[1, 1, 1, 1, 2, 2, 2, 2],
                     'phylum':['Firmicutes', 'Proteobacteria', 'Actinobacteria',
    'Bacteroidetes', 'Firmicutes', 'Proteobacteria', 'Actinobacteria', 'Bacteroidetes']})




print('#',50*"-")
# =================================================================
# Class_Ex2:
# Create a treatment column and add it to DataFrame that has 6 entries
# which the first 4 are zero and the 5 and 6 element are 1 the rest are NAN
# ----------------------------------------------------------------



print('#',50*"-")
# =================================================================
# Class_Ex3:
# Create a month column and add it to DataFrame. Just for month Jan.
# ----------------------------------------------------------------



print('#',50*"-")
# =================================================================
# Class_Ex4:
# Drop the month column.
# ----------------------------------------------------------------


print('#',50*"-")
# =================================================================
# Class_Ex5:
# Create a numpy array that has all the values of DataFrame.
# ----------------------------------------------------------------

print('#',50*"-")

# =================================================================
# Class_Ex6:
# Read baseball data into a DataFrame and check the first and last
# 10 rows
# ----------------------------------------------------------------


print('#',50*"-")
# =================================================================
# Class_Ex7:
# Create  a unique index by specifying the id column as the index
# Check the new df and verify it is unique
# ----------------------------------------------------------------


print('#',50*"-")

# =================================================================
# Class_Ex8:
#Notice that the id index is not sequential. Say we wanted to populate
# the table with every id value.
# Hint: We could specify and index that is a sequence from the first
# to the last id numbers in the database, and Pandas would fill in the
#  missing data with NaN values:
# ----------------------------------------------------------------

print('#',50*"-")

# =================================================================
# Class_Ex9:
# Fill the missing values
# ----------------------------------------------------------------


print('#',50*"-")

# =================================================================
# Class_Ex10:
# Find the shape of the new df
# ----------------------------------------------------------------


print('#',50*"-")

# =================================================================
# Class_Ex11:
# Drop row 89525 and 89526
# ----------------------------------------------------------------

print('#',50*"-")


# =================================================================
# Class_Ex12:
# Sor the df ascending and not descending 
# ----------------------------------------------------------------

print('#',50*"-")

