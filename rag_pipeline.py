from retrieval.query_parser import parse_query
from retrieval.hybrid_retriever import hybrid_search
from llm.generator import generate_answer


def answer_question(question: str):

    # 1. Parse the user's question
    filters = parse_query(question)

    print()
    print("Detected filters:")
    print(filters)

    # 2. Retrieve relevant movies
    results = hybrid_search(
        question=question,
        industry=filters["industry"],
        year=filters["year"],
        language=filters["language"],
        genre=filters["genre"],
        top_k=5
    )

    # 3. Build context for the LLM
    context_parts = []

    for result in results:

        document = result["document"]

        context_parts.append(
            document["text"]
        )

    context = "\n\n".join(
        context_parts
    )

    # 4. Generate final answer
    answer = generate_answer(
        question=question,
        context=context
    )

    # 5. Build sources
    sources = []

    for result in results:

        metadata = result["document"]["metadata"]

        sources.append({
            "title": metadata["title"],
            "year": metadata["year"],
            "industry": metadata["industry"],
            "language": metadata["language"],
            "genre": metadata["genre"],
            "director": metadata["director"],
            "distance": result["distance"]
        })

    # 6. Return answer + sources
    return {
        "answer": answer,
        "sources": sources
    }


if __name__ == "__main__":

    question = (
        "Find Telugu fantasy movies "
        "from 2024 involving magic"
    )

    result = answer_question(
        question
    )

    print()
    print("=" * 60)
    print("FINAL ANSWER")
    print("=" * 60)
    print()
    print(result["answer"])

    print()
    print("=" * 60)
    print("SOURCES")
    print("=" * 60)

    for source in result["sources"]:

        print()
        print(source)