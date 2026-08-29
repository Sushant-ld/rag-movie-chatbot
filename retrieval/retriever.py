import pickle

import faiss

from embeddings.embedding_model import load_embedding_model


INDEX_PATH = "vectorstore/faiss_index/movies.index"
DOCUMENTS_PATH = "vectorstore/faiss_index/documents.pkl"


def load_vectorstore():

    index = faiss.read_index(INDEX_PATH)

    with open(DOCUMENTS_PATH, "rb") as file:
        documents = pickle.load(file)

    return index, documents


def search_movies(
    question: str,
    top_k: int = 5
):

    index, documents = load_vectorstore()

    model = load_embedding_model()

    query_embedding = model.encode(
        [question]
    )

    query_embedding = query_embedding.astype(
        "float32"
    )

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for distance, index_position in zip(
        distances[0],
        indices[0]
    ):

        document = documents[index_position]

        results.append({
            "document": document,
            "distance": float(distance)
        })

    return results