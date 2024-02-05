import pandas as pd

# BigMart 2013 sales data 
data = pd.read_csv('data/Train.csv')

# Display the first 5 rows of the dataframe
print(data.head())

# Display the shape of the dataframe
print(data.shape)

# Display the columns of the dataframe
print(data.columns)

print(data.describe())

print(data.info())

print(data.isnull().sum()) # Check for missing values

# Fill missing values with the mean of the column
data['Item_Weight'].fillna(data['Item_Weight'].mean(), inplace=True)

print(data['Outlet_Size'])

# drop the row 'Outlet_Size' with missing values
data.dropna(subset=['Outlet_Size'], inplace=True)

print(data.isnull().sum()) # Check for missing values

# Save the cleaned data to a new csv file
data.to_csv('data/Train_cleaned.csv', index=False)

# check the new csv file
data = pd.read_csv('data/Train_cleaned.csv')
print(data.head())
print(data.shape)
print(data.columns)
print(data.describe())
print(data.info())
print(data.isnull().sum()) # Check for missing values

# visualize the data
import matplotlib.pyplot as plt
import seaborn as sns

# Plot the distribution of the target variable
plt.figure(figsize=(12, 7))
# distplot is deprecated
sns.histplot(data['Item_Outlet_Sales'], kde=True, bins=30, color='red')
plt.title('Item Outlet Sales Distribution')
plt.show()





