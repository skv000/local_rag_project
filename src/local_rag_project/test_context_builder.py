from local_rag_project.documents.loader import load_text_file
from local_rag_project.documents.chunker import chunk_text
from local_rag_project.retrieval.retriever import Retriever
from local_rag_project.rag.context_builder import build_context

def main():

    print("=" * 50)
    print("Context Builder Test")
    print("=" * 50)

    document = load_text_file(
        "data/documents/hindu_philosophy.txt"
    )

    chunks = chunk_text(
        document,
        chunk_size=200,
        chunk_overlap=30,
    )

    retriever = Retriever(chunks=chunks)

    query = "What does advaita vedanta teach?"

    results = retriever.search(
        query=query,
        top_k=2,
    )

    context = build_context(results=results)

    print("\n" + "=" * 50)
    print("QUERY")
    print("=" * 50)
    print(query)

    print("\n" + "=" * 50)
    print("RETRIEVED CONTEXT")
    print("=" * 50)
    print(context)

if __name__=="__main__":
    main()