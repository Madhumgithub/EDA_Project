import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("AIML.csv")  # Replace with your actual file name

# Display the structure of the DataFrame
print(data.info())

# Display basic statistics
print(data.describe())

# Check for missing values
missing_values = data.isnull().sum()
print("Missing values in numeric columns:\n", missing_values[missing_values > 0])

# Define the crime-related columns
crime_columns = data.columns[3:18]  # Adjust based on your dataset

# Define plotting functions
def plot_distribution():
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Total Violent Crimes (Cols.3 to 17)'], bins=20, kde=True)
    plt.title('Distribution of Total Violent Crimes', fontsize=16)
    plt.xlabel('Total Violent Crimes', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.grid(True)
    plt.show()

def plot_boxplot():
    plt.figure(figsize=(14, 10))
    sns.boxplot(data=data[crime_columns], orient='h', palette='Set2')
    plt.title('Boxplot of Violent Crimes', fontsize=16)
    plt.xlabel('Number of Crimes', fontsize=14)
    plt.ylabel('Type of Crime', fontsize=14)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_correlation_heatmap():
    plt.figure(figsize=(12, 10))
    correlation = data[crime_columns].corr()
    sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm', square=True)
    plt.title('Correlation Heatmap of Violent Crimes', fontsize=16)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.show()

def plot_average_crimes_by_state():
    average_crimes_per_state = data.groupby('State/UT')[crime_columns].mean().reset_index()
    plt.figure(figsize=(14, 8))
    melted_data = average_crimes_per_state.melt(id_vars='State/UT', value_vars=crime_columns)
    sns.barplot(data=melted_data, x='State/UT', y='value', hue='variable', palette='viridis')
    plt.title('Average Violent Crimes by State/UT', fontsize=16)
    plt.xlabel('State/UT', fontsize=14)
    plt.ylabel('Average Number of Crimes', fontsize=14)
    plt.xticks(rotation=90, fontsize=10)
    plt.legend(title='Type of Crime', fontsize=12)
    plt.grid(True)
    plt.show()

# List of plotting functions and corresponding instructions
plot_functions = [
    (plot_distribution, "You will see the distribution of total violent crimes."),
    (plot_boxplot, "You will see a boxplot of various violent crimes."),
    (plot_correlation_heatmap, "You will see a correlation heatmap of violent crimes."),
    (plot_average_crimes_by_state, "You will see average violent crimes by State/UT.")
]

# Instructions for the first graph
print("Instructions:")
print("You will see a series of visualizations regarding violent crimes data.")
print("Please close each graph window to proceed to the next visualization.")

# Loop through the plotting functions
for plot_func, instruction in plot_functions:
    print(instruction)
    plot_func()  # Call the plotting function

# End statement
print("Thank you for reviewing the visualizations. This concludes the exploratory data analysis.")
