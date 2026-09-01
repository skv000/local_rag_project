# from local_rag_project.llm.ollama_client import ask_llm
from local_rag_project.llm.ollama_client import chat_with_llm

def main():
    print("="*50)
    print("Local RAG Project")
    print("="*50)

    messages = []

    while True:
        question = input("\nYOU : ")

        if question.lower() in {"exit","quit","q"}:
            print("\nGoodbye")
            break

        messages.append(
            {
                "role": "user",
                "content": question,
            }
        )

        answer = chat_with_llm(messages=messages)

        messages.append(
            {
            "role": "assistant",
            "content": answer,
            }
        )

        print("\nAI : ")
        print(answer)


if  __name__=="__main__":
    main()