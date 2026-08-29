import pandas as pd


REQUIRED_COLUMNS = [
    "movie_id",
    "title",
    "year",
    "industry",
    "language",
    "country",
    "genre",
    "director",
    "cast",
    "runtime_minutes",
    "rating",
    "overview",
    "keywords",
]


def clean_movies(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and prepare the movie dataset.
    """

    df = df.copy()

    # Remove completely empty rows
    df = df.dropna(how="all")

    # Check required columns
    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    # Remove duplicate movie IDs
    df = df.drop_duplicates(subset=["movie_id"])

    # Clean text columns
    text_columns = [
        "title",
        "industry",
        "language",
        "country",
        "genre",
        "director",
        "cast",
        "overview",
        "keywords",
    ]

    for column in text_columns:
        df[column] = (
            df[column]
            .fillna("")
            .astype(str)
            .str.strip()
        )

    # Convert numeric columns
    df["year"] = pd.to_numeric(
        df["year"],
        errors="coerce"
    )

    df["runtime_minutes"] = pd.to_numeric(
        df["runtime_minutes"],
        errors="coerce"
    )

    df["rating"] = pd.to_numeric(
        df["rating"],
        errors="coerce"
    )

    # Remove rows without a title
    df = df[df["title"] != ""]

    return df.reset_index(drop=True)


if __name__ == "__main__":

    file_path = "data/movies.csv"

    movies = pd.read_csv(file_path)

    print("Before cleaning:")
    print("Rows:", len(movies))

    movies = clean_movies(movies)

    print()
    print("After cleaning:")
    print("Rows:", len(movies))

    print()
    print("Missing values:")
    print(movies.isnull().sum())

    print()
    print("Duplicate movie IDs:")
    print(movies["movie_id"].duplicated().sum())