import pandas as pd


def create_movie_documents(df: pd.DataFrame) -> list[dict]:
    """
    Convert each movie row into one RAG document.
    """

    documents = []

    for _, row in df.iterrows():

        document = {
            "movie_id": int(row["movie_id"]),

            "text": (
                f"Title: {row['title']}\n"
                f"Year: {row['year']}\n"
                f"Industry: {row['industry']}\n"
                f"Language: {row['language']}\n"
                f"Country: {row['country']}\n"
                f"Genre: {row['genre']}\n"
                f"Director: {row['director']}\n"
                f"Cast: {row['cast']}\n"
                f"Runtime: {row['runtime_minutes']} minutes\n"
                f"Rating: {row['rating']}\n"
                f"Overview: {row['overview']}\n"
                f"Keywords: {row['keywords']}"
            ),

            "metadata": {
                "title": row["title"],
                "year": int(row["year"]),
                "industry": row["industry"],
                "language": row["language"],
                "genre": row["genre"],
                "director": row["director"],
            }
        }

        documents.append(document)

    return documents


if __name__ == "__main__":

    file_path = "data/movies.csv"

    movies = pd.read_csv(file_path)

    documents = create_movie_documents(movies)

    print("Documents created:", len(documents))

    print()
    print("First document:")
    print(documents[0]["text"])

    print()
    print("Metadata:")
    print(documents[0]["metadata"])