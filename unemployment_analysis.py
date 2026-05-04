import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Style for better visuals
plt.style.use('ggplot')

# Load dataset
df = pd.read_csv("Unemployment in India.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Rename column for easy use
df.rename(columns={
    'Estimated Unemployment Rate (%)': 'Unemployment_Rate'
}, inplace=True)

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Remove missing values
df = df.dropna()

# -------------------------------
# 1. Unemployment Trend Over Time
# -------------------------------
plt.figure(figsize=(12,5))
df.groupby('Date')['Unemployment_Rate'].mean().plot()
plt.title("Overall Unemployment Trend in India")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.savefig("trend.png")
plt.show()

# -------------------------------
# 2. Top 10 States with Highest Unemployment
# -------------------------------
top_states = df.groupby('Region')['Unemployment_Rate'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
top_states.plot(kind='bar')
plt.title("Top 10 States by Unemployment Rate")
plt.xlabel("States")
plt.ylabel("Unemployment Rate")
plt.savefig("top_states.png")
plt.show()

# -------------------------------
# 3. Heatmap Visualization
# -------------------------------
pivot = df.pivot_table(values='Unemployment_Rate', index='Region', columns='Date')

plt.figure(figsize=(12,8))
sns.heatmap(pivot, cmap='coolwarm')
plt.title("Unemployment Heatmap Across States")
plt.savefig("heatmap.png")
plt.show()

# -------------------------------
# 4. COVID-19 Impact Analysis
# -------------------------------
covid = df[df['Date'] >= '2020-03-01']

plt.figure(figsize=(12,5))
covid.groupby('Date')['Unemployment_Rate'].mean().plot(color='red')
plt.title("Impact of COVID-19 on Unemployment")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate")
plt.savefig("covid.png")
plt.show()