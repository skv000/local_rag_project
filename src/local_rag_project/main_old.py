# from local_rag_project.llm.ollama_client import ask_llm
# from local_rag_project.llm.ollama_client import chat_with_llm
from local_rag_project.llm.ollama_client import (
    stream_chat,
    SYSTEM_PROMPT,
)

def main():
    print("="*50)
    print("Local RAG Project")
    print("="*50)

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        }
    ]

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


        print("\nAI : ")

        answer_parts = []

        # answer = stream_chat(messages=messages)

        
        for chunk in stream_chat(messages=messages):
            print(chunk,flush=True, end="")
            answer_parts.append(chunk)

        print()

        answer = "".join(answer_parts)

        messages.append(
            {
            "role": "assistant",
            "content": answer,
            }
        )




if  __name__=="__main__":
    main()