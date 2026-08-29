from sentence_transformers import SentenceTransformer


MODEL_NAME = "all-MiniLM-L6-v2"


def load_embedding_model():
    """
    Load the sentence-transformer embedding model.
    """

    model = SentenceTransformer(MODEL_NAME)

    return model


def create_embeddings(model, texts):
    """
    Convert a list of texts into embedding vectors.
    """

    embeddings = model.encode(
        texts,
        show_progress_bar=True
    )

    return embeddings


if __name__ == "__main__":

    model = load_embedding_model()

    texts = [
        "A Telugu fantasy movie about magic.",
        "A science fiction movie about artificial intelligence.",
        "A romantic drama about two people falling in love."
    ]

    embeddings = create_embeddings(
        model,
        texts
    )

    print()
    print("Embedding shape:")
    print(embeddings.shape)

    print()
    print("First embedding:")
    print(embeddings[0])

    print()
    print("Embedding dimensions:")
    print(len(embeddings[0]))