# 🔥 LLM Wrapper: Smart API Router for Multi-Model AI Responses

## 🚀 Overview
**LLM Wrapper** is an intelligent routing system that dynamically selects between **Gemini 1.5 Flash** and **Meta Llama 3.3 70B Instruct Turbo Free** models based on prompt classification. It ensures optimal responses by leveraging:
- **Gemini** for **factual/textual** queries.
- **Llama 3.3** for **logical/mathematical** tasks.

## ✨ Features
✅ **Automatic Prompt Classification** – Determines whether a query is factual or logical.  
✅ **Multi-Model Support** – Routes prompts to the best-suited model (**Gemini or Llama 3.3**).  
✅ **Efficient API Calls** – Minimizes unnecessary requests, reducing latency.  
✅ **Retry Mechanism** – Handles failures with automatic retries.  
✅ **Scalable & Modular** – Easy to extend with more models.  

## 🛠️ Tech Stack
- **Python** – Core programming language.
- **Google Generative AI SDK** – For calling Gemini 1.5 Flash.
- **Together API** – For interacting with Meta Llama 3.3 70B Instruct Turbo Free.
- **Environment Variables** – Secure API key storage.

## 📦 Installation
1️⃣ Clone the repository and install dependencies:
   ```sh
   git clone https://github.com/your-username/llm-wrapper.git
   cd llm-wrapper
   pip install -r requirements.txt
```


2️⃣ Set up your API keys as environment variables:
```sh
export GEMINI_API_KEY="your_google_api_key"
export TOGETHER_API_KEY="your_together_api_key"
```

## 🚀 Usage

Import and use the LLM Wrapper in your Python script:

from llm_wrapper import LLMWrapper

wrapper = LLMWrapper()
prompt = "Explain the concept of black holes."
response = wrapper.get_response(prompt)
print(response)

## 🏗️ Project Structure
```
llm-wrapper/
│── llm_wrapper/
│   │── __init__.py       # Package initialization
│   │── classifier.py     # Classifies prompts as factual or logical
│   │── llm_client.py     # Handles API calls to Gemini and Llama 3.3
│── main.py               # Example script for testing the wrapper
│── requirements.txt      # Python dependencies
│── README.md             # Project documentation
```
## 🔥 Future Enhancements

Add support for more LLMs (GPT-4, Claude, Mistral, etc.).

Improve classification accuracy using ML-based techniques.

Implement caching to optimize repeated queries.

## 🤝 Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue.

## 📜 License

This project is licensed under the MIT License. See LICENSE for details.
