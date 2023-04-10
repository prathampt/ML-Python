import pandas as pd

# DataFrame -----------------
# Used to create dataframe
mydata = {'Fruits':["mango",'banana','melon'], 
        'Veggies': ['onion','capsicum','carrot'],
        'Index': [1,2,3]}
        
df = pd.DataFrame(mydata)
print(df)
# df.loc[0] is used to get first row
# df.loc[[2,1]] will give third and second row

df = pd.DataFrame(mydata,["r1","r2","r3"])
print(df)

# df.loc["r1"] is used to get first row
# df.loc[["r3","r2"]] will give third and second row

# Series -------------------
# Used to add column

ser = ["p","r",'a']
ser1 = pd.Series(ser)
print(ser1)
ser2 = pd.Series(ser,['x','y',"z"])
print(ser2)

# To get data from csv file
# Data is mostly in csv files.
# csv file is like exel file

# df1 = pd.read_csv("data.csv") 
# print(df1)
# print(df1.to_string()) # this will typecast data into string

# pd.options.display.max_rows will return max numbers of rows
# it can display...
# we can change it by
# pd.options.display.max_rows = 1000

# similarly we can use .json files


# How to analize the data?

df.head(10) # will give us first 10 rows (5 is defult)
df.tail(7) # will give us last 7 rows
df.info() # will give some information 
# into helps to analize data efficiently

# How to clean our data?

new_df = df.dropna() # this will drop null data
print(new_df.info())
new_filled_data = df.fillna(100) # this will fill the null data
# with 100
print(new_filled_data.info())

# To fill the data 

# x = df1["Calories"].mean()
# df1["Calories"].fillna(x,inplace=True)
# print(df1.info())
# this will feel null data with mean in original data which is 
# confirmed by inplace

# to change the data format
# df["Date"] = df.to_date(df["Date"])

# to check duplicated data use
print(df.duplicated())

df.drop_duplicates(inplace=True)
# this will drop duplicate data

# we can use matplotlib to plot

import matplotlib.pyplot as plt
df.plot()
plt.show()

df.plot(kind="scatter",x="Fruits",y="Veggies")
plt.show()

# to sort use
df.sort_index(ascending=False ,implace=True)
print(df.head())

# we can also merge data

# we can also create a csv file using create function. 
