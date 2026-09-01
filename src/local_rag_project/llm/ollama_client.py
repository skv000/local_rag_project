from ollama import chat

MODEL_NAME = "llama3.2:3b"

# First version - for testing. No streaming and full response after complete generataion
def ask_llm(prompt: str) -> str:
    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role":"user",
                "content":prompt,
            }
        ]
    )

    return response

def chat_with_llm(messages: list[dict]) -> str:
    response = chat(
        model=MODEL_NAME,
        messages=messages
    )

    return response.message.content
