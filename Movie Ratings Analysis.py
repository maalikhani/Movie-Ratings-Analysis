import numpy as np
import pandas as pd

# File path (change this to your actual path)
csv_path = r'C:\Users\maryam\Desktop\Netflix TV Shows and Movies.csv'

# Load dataset
df = pd.read_csv(csv_path)

# Show first few rows
print("📋 Preview of the dataset:")
print(df.head())

# Show column names
print("\n📊 Columns in the dataset:")
print(df.columns)

# Check if 'imdb_score' exists in the dataset
if 'imdb_score' not in df.columns:
    raise KeyError("❌ Column 'imdb_score' not found in the dataset.")

# Convert 'imdb_score' to numeric (if there are any non-numeric values)
df['imdb_score'] = pd.to_numeric(df['imdb_score'], errors='coerce')

# Calculate statistics
mean_score = df['imdb_score'].mean()
median_score = df['imdb_score'].median()
std_score = df['imdb_score'].std()

# Print results
print(f"\n📈 IMDb Score Statistics:")
print(f"- Mean: {mean_score:.2f}")
print(f"- Median: {median_score:.2f}")
print(f"- Standard Deviation: {std_score:.2f}")

# Filter high-rated movies (IMDb > 4)
high_rated_movies = df[df['imdb_score'] > 4]

print(f"\n🎬 Number of high-rated titles (IMDb > 4): {len(high_rated_movies)}")
print("Top examples:")
print(high_rated_movies[['title', 'imdb_score']].head())
