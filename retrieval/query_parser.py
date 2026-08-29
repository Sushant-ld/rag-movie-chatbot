import re


GENRES = [
    "Action",
    "Comedy",
    "Drama",
    "Fantasy",
    "Horror",
    "Romance",
    "Science Fiction",
    "Thriller"
]


def parse_query(question: str):

    query_lower = question.lower()

    filters = {
        "industry": None,
        "year": None,
        "language": None,
        "genre": None
    }

    # -------------------------
    # Year
    # -------------------------

    year_match = re.search(
        r"\b(2020|2021|2022|2023|2024|2025|2026)\b",
        query_lower
    )

    if year_match:
        filters["year"] = int(
            year_match.group(1)
        )

    # -------------------------
    # Language
    # -------------------------

    if "telugu" in query_lower:
        filters["language"] = "Telugu"

    elif "hindi" in query_lower:
        filters["language"] = "Hindi"

    elif "english" in query_lower:
        filters["language"] = "English"

    # -------------------------
    # Industry
    # -------------------------

    if "tollywood" in query_lower:
        filters["industry"] = "Tollywood"

    elif "bollywood" in query_lower:
        filters["industry"] = "Bollywood"

    elif "hollywood" in query_lower:
        filters["industry"] = "Hollywood"

    # Infer industry from language
    # for our dataset

    elif filters["language"] == "Telugu":
        filters["industry"] = "Tollywood"

    elif filters["language"] == "Hindi":
        filters["industry"] = "Bollywood"

    elif filters["language"] == "English":
        filters["industry"] = "Hollywood"

    # -------------------------
    # Genre
    # -------------------------

    for genre in GENRES:

        if genre.lower() in query_lower:

            filters["genre"] = genre

            break

    return filters


if __name__ == "__main__":

    questions = [
        "Show me 2024 Telugu fantasy movies",
        "Find 2023 Bollywood action movies",
        "Give me 2025 Hollywood horror movies",
        "Find Telugu movies about magic"
    ]

    for question in questions:

        print()
        print("Question:")
        print(question)

        print("Filters:")
        print(
            parse_query(question)
        )