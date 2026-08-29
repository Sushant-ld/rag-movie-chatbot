import pickle

from retrieval.metadata_filter import filter_movies


DOCUMENTS_PATH = "vectorstore/faiss_index/documents.pkl"


with open(DOCUMENTS_PATH, "rb") as file:
    documents = pickle.load(file)


results = filter_movies(
    documents,
    industry="Tollywood",
    year=2024,
    genre="Fantasy"
)


print("Filtered movies:", len(results))

print()

for movie in results[:5]:

    print(
        movie["metadata"]
    )