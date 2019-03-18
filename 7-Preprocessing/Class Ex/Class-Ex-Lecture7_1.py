# =================================================================
# Class_Ex1:  Convert text to lowercase
# ----------------------------------------------------------------
input_str = 'The 5 biggest countries by population in 2017 are China, India, United States, Indonesia, and Brazil.'



# =================================================================
# Class_Ex2:  Numbers removing

# ----------------------------------------------------------------
input_str = 'Box A contains 3 red and 5 white balls, while Box B contains 4 red and 2 blue balls.'



# =================================================================
# Class_Ex3: White spaces removal

# ----------------------------------------------------------------
input_str = "\t a string example\t "


# =================================================================
# Class_Ex4: Use Pandas and explore the given dataset.

# ----------------------------------------------------------------

import pandas as pd
import numpy as np

df = pd.io.parsers.read_csv('https://raw.githubusercontent.com/rasbt/pattern_classification/master/data/wine_data.csv',
     header=None, usecols=[0,1,2] )

df.columns=['Class label', 'Alcohol', 'Malic acid']
df.head()




# =================================================================
# Class_Ex5: Normalize the input of the IRIS dataset.

# ----------------------------------------------------------------






# =================================================================
# Class_Ex6: Demonstrate data standardization of the Iris flowers dataset.

# ----------------------------------------------------------------





# =================================================================
# Class_Ex7:

# ----------------------------------------------------------------
