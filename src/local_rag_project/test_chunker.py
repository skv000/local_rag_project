from local_rag_project.documents.loader import load_text_file
from local_rag_project.documents.chunker import chunk_text


def main():

    print("=" * 50)
    print("Text Chunker Test")
    print("=" * 50)

    document = load_text_file(
        "data/documents/hindu_philosophy.txt"
    )

    chunks = chunk_text(
        document,
        chunk_size=500,
        chunk_overlap=50,
    )

    print(
        f"Original document length: {len(document)}"
    )

    print(
        f"Number of chunks: {len(chunks)}"
    )

    for index, chunk in enumerate(
        chunks,
        start=1,
    ):
        print("\n" + "-" * 50)
        print(f"Chunk index : {index}")
        print("-" * 50)
        print(chunk)


if __name__ == "__main__":
    main()