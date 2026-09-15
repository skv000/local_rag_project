from local_rag_project.documents.loader import load_text_file
from local_rag_project.documents.chunker import (
    chunk_text,
    split_paragraphs,
)


def main():

    print("=" * 50)
    print("Text Chunker Test")
    print("=" * 50)

    document = load_text_file(
        "data/documents/rag_test_document.txt"
    )

    paragraphs = split_paragraphs(document)

    chunks = chunk_text(
        document,
        chunk_size=500,
        chunk_overlap=50,
    )

    print(
        f"Original document length: {len(document)}"
    )

    print(
        f"Number of paragraphs: {len(paragraphs)}"
    )

    print(
        f"Number of chunks: {len(chunks)}"
    )

    for index, chunk in enumerate(
        chunks,
        start=1,
    ):

        print("\n" + "-" * 50)
        print(f"Chunk {index}")
        print("-" * 50)

        print(chunk)

        print(
            f"\nCharacters: {len(chunk)}"
        )


if __name__ == "__main__":
    main()