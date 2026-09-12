import re


def split_sentences(text: str) -> list[str]:
    """
    Split text into sentences while preserving sentence content.
    """

    sentences = re.split(
        r"(?<=[.!?])\s+",
        text.strip(),
    )

    return [
        sentence.strip()
        for sentence in sentences
        if sentence.strip()
    ]


def chunk_text(
    text: str,
    chunk_size: int = 500,
    chunk_overlap: int = 50,
) -> list[str]:

    if chunk_size <= 0:
        raise ValueError(
            "chunk_size must be greater than zero."
        )

    if chunk_overlap < 0:
        raise ValueError(
            "chunk_overlap can not be negative."
        )

    if chunk_overlap >= chunk_size:
        raise ValueError(
            "chunk_overlap must be smaller than chunk_size."
        )

    sentences = split_sentences(text)

    chunks = []
    current_chunk = []

    current_length = 0

    for sentence in sentences:

        sentence_length = len(sentence)

        # If adding this sentence would exceed the chunk size,
        # save the current chunk.
        if (
            current_chunk
            and current_length + sentence_length > chunk_size
        ):
            chunks.append(
                " ".join(current_chunk).strip()
            )

            # Keep sentences from the end of the previous chunk
            # to provide overlap.
            overlap_sentences = []
            overlap_length = 0

            for previous_sentence in reversed(current_chunk):

                if (
                    overlap_length + len(previous_sentence)
                    > chunk_overlap
                ):
                    break

                overlap_sentences.insert(
                    0,
                    previous_sentence,
                )

                overlap_length += len(previous_sentence)

            current_chunk = overlap_sentences
            current_length = sum(
                len(sentence)
                for sentence in current_chunk
            )

        current_chunk.append(sentence)
        current_length += sentence_length

    # Add final chunk.
    if current_chunk:
        chunks.append(
            " ".join(current_chunk).strip()
        )

    return chunks