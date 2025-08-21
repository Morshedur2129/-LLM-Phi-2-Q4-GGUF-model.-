# -LLM-Phi-2-Q4-GGUF-model.-
A simple local chatbot using the Phi-2 large language model (LLM) in GGUF format, powered by llama-cpp-python. Ask questions and get answers entirely offline on your own computer.


# Local Phi-2 Q4_0 GGUF Chatbot

This project lets you run the [Phi-2](https://huggingface.co/microsoft/phi-2) large language model locally using [llama-cpp-python](https://github.com/abetlen/llama-cpp-python).  
Ask questions and get answers entirely offline on your own computer.

---

## Features

- Runs the Phi-2 Q4_0 GGUF model locally (no internet required after setup)
- Simple Python script for chatting with the model

---

## Setup

1. **Clone this repository:**
    ```sh
    git clone https://github.com/Morshedur2129/-LLM-Phi-2-Q4-GGUF-model.-.git
    cd -LLM-Phi-2-Q4-GGUF-model.-
    ```

2. **Download the Phi-2 GGUF model:**
    - Download `phi-2.Q4_0.gguf` from [TheBloke/phi-2-GGUF on Hugging Face](https://huggingface.co/TheBloke/phi-2-GGUF)
    - Place it in the `models` folder (create the folder if it doesn't exist).

3. **Create a virtual environment and install dependencies:**
    ```sh
    python -m venv .venv
    .venv\Scripts\activate
    pip install -r requirements.txt
    ```

4. **Run the chatbot:**
    ```sh
    python chat_phi2.py
    ```

    ## Example Prompt & Answer

![Prompt and Answer](https://github.com/Morshedur2129/-LLM-Phi-2-Q4-GGUF-model.-/blob/main/prompt%20and%20answer%20.jpg?raw=true)

---

## Usage

- Type your question at the `You:` prompt and press Enter.
- The model will generate an answer.
- Type `exit` to quit.

---

## Notes

- The model file (`phi-2.Q4_0.gguf`) is **not included** in this repo due to its size.  
- Make sure the path in `chat_phi2.py` matches where you put the model file.
- This project uses [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) for efficient local inference.

---

## Example

```
You: Who is Shikh Hasina?
Bot: Shikh Hasina is the Prime Minister of Bangladesh.
```

---

## License

This project is for educational and research purposes.  
Phi-2 is released by Microsoft Research under
