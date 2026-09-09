def build_context(
        results: list[tuple[str, float]]
) -> str:
    """
    Combine retrieved chunks into a single context string.
    """

    context_parts = []

    for index, (chunk, score) in enumerate(
        results,
        start=1
    ):
        context_parts.append(
            f"[Chunk {index}]\n{chunk}"
        )

    return "\n\n".join(context_parts)