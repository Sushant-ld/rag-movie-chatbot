def filter_movies(
    documents,
    industry=None,
    year=None,
    language=None,
    genre=None
):
    """
    Filter movie documents using metadata.
    """

    filtered = documents

    if industry:
        filtered = [
            doc for doc in filtered
            if doc["metadata"]["industry"].lower()
            == industry.lower()
        ]

    if year:
        filtered = [
            doc for doc in filtered
            if doc["metadata"]["year"] == int(year)
        ]

    if language:
        filtered = [
            doc for doc in filtered
            if doc["metadata"]["language"].lower()
            == language.lower()
        ]

    if genre:
        filtered = [
            doc for doc in filtered
            if doc["metadata"]["genre"].lower()
            == genre.lower()
        ]

    return filtered