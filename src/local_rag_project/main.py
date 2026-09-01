from local_rag_project.llm.ollama_client import ask_llm

def main():
    print("="*50)
    print("Local RAG Project")
    print("="*50)

    while True:
        question = input("\nYOU : ")

        if question.lower() in {"exit","quit","q"}:
            print("Goodbye")
            break

        answer = ask_llm(question)

        print("\nAI : ")
        print(answer.message.content)


if  __name__=="__main__":
    main()