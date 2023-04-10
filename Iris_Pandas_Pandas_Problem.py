
Problem_Statement = """
1. Print all data fields.
2. Cleaning data:
    Duplicate drop
    Drop null entries (irradicate)
3. Output the no. of species and no. of flowers.
4. Add new rows of species."""


import pandas as pd

df = pd.read_csv("Iris.csv.xls")
print("Information of our data: \n")
df.info()

# 1. Print all data fields.
list_of_data_fileds = list(map(str,df.columns))
print("Data fields are as follows:\n",list_of_data_fileds,sep="")

# 2. Cleaning data:
#    Duplicate drop
#    Drop null entries (irradicate)

df_new = pd.read_csv("Iris.csv.xls")
df_new.drop("Id",axis=1,inplace=True) # As id's all are different then duplicated will always show False
# Thus we are making a copy which don't contain id's
# If any value has duplicated values
for i,j in df_new.duplicated().items():
    if j == True:
        print(f"Data have duplicate values at index {i}.")

df_new.drop_duplicates(inplace=True) # Dropping any duplicate values
print("Now duplicate data is removed.")
df_new.dropna(inplace=True) # Dropping any null values
print("Now any null data is also removed.")
df_new.info()

# 3. Output the no. of species and no. of flowers.

group = df_new.groupby("Species")
print(group["Species"].count())

# 4. Add new rows of species.

df_new_new = pd.DataFrame(df_new, [i for i in range(len(df_new.index))])
df_new_new.loc[len(df_new_new.index)+1] = [5.4,3.9,1.3,0.1,'Iris-prathama']
print("New row sucessfully added.")
df_new_new.info()
print(df_new_new.to_string())

# Updated count
print("Updated count.")
group1 = df_new_new.groupby("Species")
print(group1["Species"].count())