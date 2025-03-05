import google.generativeai as genai
import os

gen_key = os.getenv('genai-api')
genai.configure(api_key=gen_key)
model = genai.GenerativeModel("gemini-1.5-flash")


def categorize_prompt(prompt):
    """Ask Gemini 2.0 Flash to classify the query into 'Logical/Programming' or 'Factual/Textual'."""
    try:
        """Classify the prompt using Gemini 1.5 Flash."""
        response = model.generate_content([
            {"role": "user", "parts": [{"text": f"Classify the following prompt as either 'Logical/Programming or "
                                                f"'Factual/Textual/Content': {prompt}"}]}
        ])
        return response.text.strip()
    except Exception as e:
        print(f" Error classifying prompt: {e}")
        return "Factual/Textual"
