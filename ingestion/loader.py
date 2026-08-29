import pandas as pd

def load_movies(file_path: str) -> pd.DataFrame:
    """
    Load the movie dataset from a csv file.
    """
    df = pd.read_csv(file_path)
    
    return df 


if __name__ == "__main__":

    file_path = "data/movies.csv"

    movies = load_movies(file_path)

    print("Dataset loaded successfully!")
    print()

    print("Number of movies:", len(movies))
    print("Number of columns:", len(movies.columns))
    print()

    print("Columns:")
    print(movies.columns.tolist())
    print()

    print("Industry distribution:")
    print(movies["industry"].value_counts())
    print()

    print("Year distribution:")
    print(movies["year"].value_counts().sort_index())
    print()

    print("First movie:")
    print(movies.iloc[0].to_string())    