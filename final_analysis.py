import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("cleaned_netflix_data.csv")

# -------------------------
# Country-wise Analysis
# -------------------------
top_countries = df['country'].value_counts().head(10)

plt.figure()
plt.bar(top_countries.index, top_countries.values)
plt.title("Top 10 Netflix Content Producing Countries")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# -------------------------
# Movies vs TV Shows Trend
# -------------------------
type_trend = df.groupby(['year_added', 'type']).size().reset_index(name='count')

plt.figure()
for t in type_trend['type'].unique():
    data = type_trend[type_trend['type'] == t]
    plt.plot(data['year_added'], data['count'], label=t)

plt.title("Movies vs TV Shows Trend Over Time")
plt.xlabel("Year")
plt.ylabel("Titles Added")
plt.legend()
plt.tight_layout()
plt.show()
