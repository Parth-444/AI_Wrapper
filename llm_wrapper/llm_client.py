import os
import time
import together
import google.generativeai as genai

GEMINI_API_KEY = os.getenv("genai-api")
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

if not GEMINI_API_KEY or not TOGETHER_API_KEY:
    raise ValueError("❌ Missing API keys. Ensure GEMINI_API_KEY and TOGETHER_API_KEY are set.")

genai.configure(api_key=GEMINI_API_KEY)
client = together.Together(api_key=TOGETHER_API_KEY)


class LLMWrapper:
    """Wrapper for calling Gemini 1.5 Flash and Llama models."""

    def __init__(self):
        self.gemini_model = genai.GenerativeModel("gemini-1.5-flash")
        self.llama_model = "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"

    def call_gemini(self, prompt, retries=3, delay=2):
        """Calls Gemini 1.5 Flash API with retries on failure."""
        print("Using Gemini")
        for attempt in range(retries):
            try:
                response = self.gemini_model.generate_content(prompt)
                return response.text
            except Exception as e:
                print(f"⚠️ Gemini API Error (Attempt {attempt + 1}): {e}")
                time.sleep(delay)
        return "⚠️ Gemini API failed after multiple attempts."

    def call_llama(self, prompt, retries=3, delay=2):
        print("Using Llama")
        """Call Llama-3.3-70B-Instruct-Turbo-Free" API via Together AI with retries on failure."""
        for attempt in range(retries):
            try:
                response = client.chat.completions.create(
                    model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=512,
                    temperature=0.6,
                    top_p=0.95
                )
                return response.choices[0].message.content
            except Exception as e:
                print(f"⚠️ Together API Error (Attempt {attempt + 1}): {e}")
                time.sleep(delay)

        return "⚠️ Together API failed after multiple attempts."