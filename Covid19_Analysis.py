import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#1. Import the dataset
df = pd.read_csv("covid-data.csv")
print(df)

#2. High-Level Data Understanding
def high_level_data_understanding(df):
    print("Number of rows and columns:", df.shape)
    print("\nData types of columns:\n", df.dtypes)
    print("\nInfo of data:")
    df.info()
    print("\nDescription of data:\n", df.describe())

high_level_data_understanding(df)

# 3. Low-Level Data Understanding
def low_level_data_understanding(df):
    print("\nCount of unique values in 'location' column:", df['location'].nunique())
    print("\nContinent with maximum frequency:", df['continent'].value_counts().idxmax())
    print("\nMaximum and mean value in 'total_cases':", df['total_cases'].max(), df['total_cases'].mean())
    print("\n25%, 50%, and 75% quartile in 'total_deaths':\n", df['total_deaths'].quantile([0.25, 0.5, 0.75]))
    print("\nContinent with maximum 'human_development_index':", df.groupby('continent')['human_development_index'].mean().idxmax())
    print("\nContinent with minimum 'gdp_per_capita':", df.groupby('continent')['gdp_per_capita'].mean().idxmin())

low_level_data_understanding(df)

# 4. Filter the DataFrame
data = df[['continent', 'location', 'date', 'total_cases', 'total_deaths', 'gdp_per_capita', 'human_development_index']]

# 5. Data Cleaning
def data_cleaning(df):
    # Remove duplicates
    df = df.drop_duplicates()

    # Find and remove missing continent values
    df = df.dropna(subset=['continent'])

    # Fill missing values with 0
    df = df.fillna(0)
    return df

data = data_cleaning(data)

# 6. Date Time Format
# Specify the format for date parsing
data['date'] = pd.to_datetime(data['date'], format='%d/%m/%y')


# 7. Data Aggregation
def data_aggregation(df):
    df_groupby = df.groupby('continent').max().reset_index()
    return df_groupby

df_groupby = data_aggregation(data)

# 8. Feature Engineering
data['total_deaths_to_total_cases'] = data['total_deaths'] / data['total_cases']

# 9. Data Visualization
def data_visualization(df, df_groupby):
    sns.set(style="whitegrid")

    # Univariate analysis: histogram for 'gdp_per_capita'
    plt.figure(figsize=(10, 6))
    sns.histplot(df['gdp_per_capita'], kde=True, color='blue')
    plt.title('Distribution of GDP per Capita')
    plt.xlabel('GDP per Capita')
    plt.ylabel('Frequency')
    plt.show()

    # Scatter plot: 'total_cases' vs 'gdp_per_capita'
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='gdp_per_capita', y='total_cases', data=df, color='red')
    plt.title('Total Cases vs GDP per Capita')
    plt.xlabel('GDP per Capita')
    plt.ylabel('Total Cases')
    plt.show()

    # Pairplot on df_groupby
    sns.pairplot(df_groupby)
    plt.show()

    # Bar plot: 'continent' vs 'total_cases'
sns.catplot(
    data=df_groupby, 
    x='continent', 
    y='total_cases', 
    kind='bar', 
    height=6, 
    aspect=1.5, 
    hue='continent',  # Assign the 'x' variable to 'hue'
    palette='viridis', 
    legend=False
)
plt.title("Total Cases by Continent")
plt.xlabel("Continent")
plt.ylabel("Total Cases")
plt.show()



data_visualization(data, df_groupby)

# 10. Save the DataFrame to CSV
df_groupby.to_csv('df_groupby.csv', index=False)
print("df_groupby DataFrame saved as 'df_groupby.csv' in the local directory.")
