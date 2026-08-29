import os
import pickle

import faiss
import pandas as pd

from ingestion.chunker import create_movie_documents
from embeddings.embedding_model import (
    load_embedding_model,
    create_embeddings
)


DATA_PATH = "data/movies.csv"

INDEX_DIR = "vectorstore/faiss_index"

INDEX_PATH = os.path.join(
    INDEX_DIR,
    "movies.index"
)

DOCUMENTS_PATH = os.path.join(
    INDEX_DIR,
    "documents.pkl"
)


def create_faiss_index():

    print("Loading dataset...")

    movies = pd.read_csv(DATA_PATH)

    print(f"Movies loaded: {len(movies)}")

    print()
    print("Creating documents...")

    documents = create_movie_documents(
        movies
    )

    print(
        f"Documents created: {len(documents)}"
    )

    print()
    print("Loading embedding model...")

    model = load_embedding_model()

    print()
    print("Creating embeddings...")

    texts = [
        document["text"]
        for document in documents
    ]

    embeddings = create_embeddings(
        model,
        texts
    )

    print()
    print("Embedding shape:")
    print(embeddings.shape)

    # FAISS expects float32
    embeddings = embeddings.astype("float32")

    dimension = embeddings.shape[1]

    print()
    print("Vector dimension:")
    print(dimension)

    # Create FAISS index
    index = faiss.IndexFlatL2(
        dimension
    )

    # Add embeddings
    index.add(embeddings)

    print()
    print("Vectors stored in FAISS:")
    print(index.ntotal)

    # Create directory
    os.makedirs(
        INDEX_DIR,
        exist_ok=True
    )

    # Save FAISS index
    faiss.write_index(
        index,
        INDEX_PATH
    )

    # Save documents
    with open(
        DOCUMENTS_PATH,
        "wb"
    ) as file:

        pickle.dump(
            documents,
            file
        )

    print()
    print("FAISS index saved:")
    print(INDEX_PATH)

    print()
    print("Documents saved:")
    print(DOCUMENTS_PATH)


if __name__ == "__main__":

    create_faiss_index()