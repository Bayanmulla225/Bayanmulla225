from ollama import Client

# 1. Initialize the Ollama client
client = Client(host="http://localhost:11434")

# 2. Get the question from the user
question = input("User: ")

#3.generate a response using Qwen3.5
messages = [
    {
        "role": "system",
        "content": (
            "Keep each sentence simple, clear, and informative. "
            "Do not use bullet points or numbering."
        ),
    },
    {
        "role": "user",
        "content": question,
    },
]


completion = client.chat(
    model="qwen3.5:0.8b",
    messages=messages,
    think=True,
    options={
        "temperature": 0,
    }
)

# 4. Extract the AI response
answer = completion.message.content.strip()

# 5. Display the response
print("\nAI:", answer)

