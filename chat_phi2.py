from llama_cpp import Llama

model_path = r"F:\phi2_local\models\phi-2.Q4_0.gguf"

llm = Llama(
    model_path=model_path,
    n_ctx=2048,
    n_threads=4,
    n_gpu_layers=0
)

print("Chatbot ready! Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    try:
        # Use a more instructive prompt
        prompt = f"Question: {user_input}\nAnswer:"
        output = llm(
            prompt,
            max_tokens=100,
            stop=["\n", "</s>"],
            temperature=0.2,
            top_p=0.8
        )
        print("Bot:", output["choices"][0]["text"].strip())
    except Exception as e:    del [index.lock](http://_vscodecontentref_/0)
        print("Error:", e)