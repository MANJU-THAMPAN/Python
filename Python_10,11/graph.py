import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
data = pd.read_csv('pet.csv')

# Create a dataframe from the data
df = pd.DataFrame(data)
df = df.head(50)
print(df)
# Create a line graph
plt.plot(df['sales'], df['country'])
plt.xlabel('Position Title')
plt.ylabel('Base Pay')
plt.title('Line Graph of Position Title vs. Given Name')
plt.show()

# Create a bar graph
plt.bar(df['sales'], df['country'])
plt.xlabel('Position Title')
plt.ylabel('Salary Paid')
plt.title('Bar Graph of Position Title vs. Salary Paid')
plt.show()

# Create a scatter plot
plt.scatter(df['sales'], df['country'])
plt.xlabel('Position Title')
plt.ylabel('Salary Paid')
plt.title('Scatter Plot of Position Title vs. Salary Paid')
plt.show()

