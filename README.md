# Covid-19 Data Analysis Project

This project analyzes Covid-19 data using Python and various data analysis and visualization techniques. The dataset is sourced from a public URL and contains information such as total cases, deaths, GDP per capita, and human development index for different locations worldwide.

## Project Steps

1. **Data Import**: Import the dataset from a given URL using Pandas.
2. **High-Level Data Understanding**:
   - Check the number of rows and columns.
   - Identify data types of each column.
   - View dataset info and statistical summary.
3. **Low-Level Data Understanding**:
   - Analyze unique values in the `location` column.
   - Identify the continent with the highest frequency.
   - Compute max and mean values for `total_cases`.
   - Calculate quartile values for `total_deaths`.
   - Determine the continent with the highest `human_development_index` and lowest `gdp_per_capita`.
4. **Data Cleaning**:
   - Remove duplicate observations.
   - Handle missing values.
   - Remove rows with missing `continent` values.
   - Fill missing values with 0.
5. **Date-Time Formatting**:
   - Convert `date` to a datetime format.
   - Extract the month from the `date` column.
6. **Data Aggregation**:
   - Aggregate data by continent and find maximum values for each feature.
7. **Feature Engineering**:
   - Create a new feature `total_deaths_to_total_cases`.
8. **Data Visualization**:
   - Plot univariate, scatter, pairplot, and bar charts for analysis.
9. **Save Data**:
   - Save the aggregated data to a CSV file.

## Visualizations

- **Histogram**: Distribution of GDP per capita.
- **Scatter Plot**: Relationship between total cases and GDP per capita.
- **Pairplot**: Pairwise relationships in the aggregated data.
- **Bar Plot**: Total cases by continent.

## Technologies Used

- Python
- Pandas
- NumPy
- Seaborn
- Matplotlib

## How to Run the Project

1. Clone this repository.
2. Install the required Python libraries using:
   ```bash
   pip install pandas numpy seaborn matplotlib
