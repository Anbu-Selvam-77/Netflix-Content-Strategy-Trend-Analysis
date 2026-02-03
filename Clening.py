import pandas as pd

df = pd.read_csv("netflix_titles.csv")

# Fill missing values
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')

# Clean and convert date_added
df['date_added'] = pd.to_datetime(
    df['date_added'].str.strip(),
    errors='coerce'
)

# Drop rows where date still couldn't be parsed
df.dropna(subset=['date_added'], inplace=True)

# Extract year
df['year_added'] = df['date_added'].dt.year

# Split multi-value columns
df['listed_in'] = df['listed_in'].str.split(', ')
df['country'] = df['country'].str.split(', ')

# Explode rows
df = df.explode('listed_in')
df = df.explode('country')

# Clean text
df['listed_in'] = df['listed_in'].str.strip()
df['country'] = df['country'].str.strip()
df['type'] = df['type'].str.title()

# Remove duplicates
df.drop_duplicates(inplace=True)

# Save cleaned dataset
df.to_csv("cleaned_netflix_data.csv", index=False)

print("✅ Cleaning completed successfully!")
print(df.shape)
