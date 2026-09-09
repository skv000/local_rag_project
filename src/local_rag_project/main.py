from local_rag_project.documents.loader import load_text_file
from local_rag_project.documents.chunker import chunk_text
from local_rag_project.retrieval.retriever import Retriever
from local_rag_project.rag.context_builder  import build_context
from local_rag_project.rag.prompt_builder import build_rag_prompt
from local_rag_project.llm.ollama_client import (
    SYSTEM_PROMPT,
    stream_chat,
)

def main():

    print("=" * 50)
    print("Local RAG Project")
    print("=" * 50)

    # Load Document

    document = load_text_file(
        "data/documents/hindu_philosophy.txt"
    )

    # Create chunks

    chunks = chunk_text(
        text=document,
        chunk_size=200,
        chunk_overlap=30,
    )

    print(f"Loaded document with {len(chunks)} chunks.")

    # Create retriever

    retriever = Retriever(chunks=chunks)

    # Start Conversation

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        }
    ]

    while True:

        question = input("\nYOU : ")

        if question.lower() in {'exit','quit', 'q'}:
            print("\nAI : GoodBye, See you later!")
            break

        # Retrieve relevant chunks

        results = retriever.search(
            query=question,
            top_k=2,
        )

        # Build context

        context = build_context(
            results=results
        )

        # Build RAG prompt

        rag_prompt = build_rag_prompt(
            question=question,
            context=context,
        )

        # Add RAG prompt to conversation

        messages.append(
            {
                "role": "user",
                "content": rag_prompt,
            }
        )

        # Generate Response

        print("\nAI : ")

        answer_parts = []

        for chunk in stream_chat(
            messages=messages
        ):
            print(
                chunk,
                flush=True,
                end=""
            )

            answer_parts.append(chunk)

        print()

        # Save assistant response

        answer = "".join(answer_parts)

        messages.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )


if __name__=="__main__":
    main()