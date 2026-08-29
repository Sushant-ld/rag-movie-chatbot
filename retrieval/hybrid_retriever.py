import pickle

import faiss

from embeddings.embedding_model import load_embedding_model


INDEX_PATH = "vectorstore/faiss_index/movies.index"
DOCUMENTS_PATH = "vectorstore/faiss_index/documents.pkl"


def load_documents():

    with open(DOCUMENTS_PATH, "rb") as file:
        return pickle.load(file)


def load_index():

    return faiss.read_index(INDEX_PATH)


def hybrid_search(
    question,
    industry=None,
    year=None,
    language=None,
    genre=None,
    top_k=5
):

    documents = load_documents()

    # -----------------------------
    # 1. Metadata filtering
    # -----------------------------

    filtered_documents = documents

    if industry:
        filtered_documents = [
            doc for doc in filtered_documents
            if doc["metadata"]["industry"].lower()
            == industry.lower()
        ]

    if year:
        filtered_documents = [
            doc for doc in filtered_documents
            if doc["metadata"]["year"] == int(year)
        ]

    if language:
        filtered_documents = [
            doc for doc in filtered_documents
            if doc["metadata"]["language"].lower()
            == language.lower()
        ]

    if genre:
        filtered_documents = [
            doc for doc in filtered_documents
            if doc["metadata"]["genre"].lower()
            == genre.lower()
        ]

    # -----------------------------
    # 2. Semantic search
    # -----------------------------

    model = load_embedding_model()

    query_embedding = model.encode(
        [question]
    ).astype("float32")

    # Create temporary mapping from
    # filtered documents to their
    # original document positions.

    filtered_ids = {
        doc["movie_id"]
        for doc in filtered_documents
    }

    index = load_index()

    distances, indices = index.search(
        query_embedding,
        len(documents)
    )

    results = []

    for distance, position in zip(
        distances[0],
        indices[0]
    ):

        document = documents[position]

        if document["movie_id"] in filtered_ids:

            results.append({
                "document": document,
                "distance": float(distance)
            })

        if len(results) >= top_k:
            break

    return results


if __name__ == "__main__":

    question = "movies involving magic"

    results = hybrid_search(
        question=question,
        industry="Tollywood",
        year=2024,
        language="Telugu",
        genre="Fantasy",
        top_k=5
    )

    print()
    print("Question:")
    print(question)

    print()
    print("Filters:")
    print("Industry: Tollywood")
    print("Year: 2024")
    print("Language: Telugu")
    print("Genre: Fantasy")

    print()
    print("Results:")

    for i, result in enumerate(
        results,
        start=1
    ):

        print()
        print(f"Result {i}")
        print("-" * 50)
        print(result["document"]["text"])
        print()
        print("Distance:", result["distance"])