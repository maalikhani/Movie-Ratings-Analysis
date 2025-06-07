import pandas as pd
import numpy as np

# Define a dictionary specifying the data types for each column
# This helps optimize memory usage and speeds up data processing
dtype_dict = {
    "id": "category", # default dtype detected by pandas was object(in my research i found that category is more optimize than object)
    "title": "string",
    "type": "category",
    "description": "string",
    "release_year": "int16",
    "age_certification": "category",
    "runtime": "int16",
    "imdb_id": "category",
    "imdb_score": "float32",
    "imdb_votes": "Int32" #Int32 because of nun value columns in dataset
}

# Define the path to the CSV file containing the dataset
csv_path = r'C:\users\maryam\Desktop\Netflix TV Shows and Movies.csv'

# Load the dataset into a pandas DataFrame with specified dtypes and indexing
df = pd.read_csv(
    csv_path,
    dtype=dtype_dict,
    index_col=0,
    low_memory=False
)

# Display the first 5 rows of the DataFrame to verify successful loading
print("First 5 rows of the dataset:")
print(df.head())

# Identify columns that contain missing values and display their counts
print("\nColumns with missing values and their counts:")
missing_values = df.isnull().sum().sort_values(ascending=False)
print(missing_values[missing_values > 0])

# Sort the DataFrame by 'imdb_score' in descending order and display top 10 entries
sorted_by_rating = df.sort_values(by='imdb_score', ascending=False)
print("\nTop 10 movies/shows sorted by IMDb score:")
print(sorted_by_rating.head(10))

# Calculate the average IMDb rating grouped by 'type' (e.g., Movie, Show)
average_rating_by_genre = df.groupby('type', observed=False)['imdb_score'].mean()
print("\nAverage IMDb rating by type (genre):")
print(average_rating_by_genre)

# Calculate basic statistics (mean, median, standard deviation) for IMDb ratings
mean_rating = df['imdb_score'].mean()
median_rating = df['imdb_score'].median()
std_rating = df['imdb_score'].std()

print(f"\nMean IMDb Rating: {mean_rating:.3f}")
print(f"Median IMDb Rating: {median_rating:.3f}")
print(f"Standard Deviation of IMDb Rating: {std_rating:.3f}")

# Filter movies/shows with IMDb rating above a threshold (e.g., 4 stars)
ratings_array = df['imdb_score'].to_numpy()
high_rating_filter = ratings_array > 4
high_rating_movies = df[high_rating_filter]
print("\nMovies/shows with IMDb rating above 4:")
print(high_rating_movies.head())

# Filter movies/shows released in the year 2020
year_2020_movies = df[df['release_year'] == 2020]
print("\nMovies/shows released in 2020:")
print(year_2020_movies.head())

# Filter only movies (excluding shows)
movies_only = df[df['type'] == 'MOVIE']
print("\nOnly movies from the dataset:")
print(movies_only.head())

# Combine filters: movies with rating > 7 released in 2022
filtered = df[(df['imdb_score'] > 7) & (df['release_year'] == 2022)]
print("\nMovies with IMDb rating above 7 released in 2022:")
print(filtered.head())
