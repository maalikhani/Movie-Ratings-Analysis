import pandas as pd
import numpy as np

# create a datatype dic , its help us to optimize code and resource usage in compute systems.

dtype_dict = {
    "id": "category",
    "title": "string",
    "type": "category",
    "description": "string",
    "release_year": "int16",
    "age_certification": "category",
    "runtime": "int16",
    "imdb_id": "category",
    "imdb_score": "float32",
    "imdb_votes": "Int32"
}

#describe variable path of dataset in system:
csv_path = r'C:\users\maryam\Desktop\Netflix TV Shows and Movies.csv'

#create a dataframe with read_csv function from pandas lib , in this dataframe creation , i used of 3 keyword argumans
df = pd.read_csv(
    csv_path,
    dtype=dtype_dict,
    index_col=0,
    low_memory=False
)


print(df.head())

#to see a columns without data (non columns)
print("\nColumns with missing values:")
print(df.isnull().sum().sort_values(ascending=False).loc[lambda x: x > 0])

#Sort and filter movies based on ratings or genres.
sorted_by_rating = df.sort_values(by='imdb_score', ascending=False)
print(sorted_by_rating.head(10))

average_rating_by_genre = df.groupby('type', observed=False)['imdb_score'].mean()
print(average_rating_by_genre)
print()

#Calculate basic statistics (mean, median, standard deviation) for ratings.
mean_rating = df['imdb_score'].mean()
median_rating = df['imdb_score'].median()
std_rating = df['imdb_score'].std()

print(f"Mean IMDb Rating: {mean_rating}")
print(f"Median IMDb Rating: {median_rating}")
print(f"Standard Deviation of IMDb Rating: {std_rating}")
print()

#Filter the dataset to find: Movies with ratings above a certain threshold (e.g., 4 stars). - Movies from a specific year or genre
ratings_array = df['imdb_score'].to_numpy()
high_rating_filter = ratings_array > 4
high_rating_movies = df[high_rating_filter]

print(high_rating_movies.head())
print()

year_2020_movies = df[df['release_year'] == 2020]
print(year_2020_movies.head())

print()

movies_only = df[df['type'] == 'MOVIE']
print(movies_only.head())

filtered = df[(df['imdb_score'] > 7) & (df['release_year'] == 2022)]
print(filtered.head())
