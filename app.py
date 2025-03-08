from flask import Flask, request, jsonify, render_template, session
from llm_wrapper.llm_client import LLMWrapper
from llm_wrapper.classifier import categorize_prompt

app = Flask(__name__)

wrapper = LLMWrapper()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    try:
        prompt = request.form.get('prompt')
        session['prompt'] = prompt
        if not prompt:
            return render_template('index.html', error='No prompt provided')
        classification = categorize_prompt(prompt)
        session['classification'] = classification
        return render_template('index.html', classification=classification, prompt=prompt)
    except Exception as e:
        return render_template('index.html', error=str(e))


@app.route('/call')
def call():
    classification = session.get('classification')
    if "Logical/Programming." in classification.split() or "Logical/Programming" in classification.split():
        llama_out = wrapper.call_llama(session.get('prompt'))
    else:
        gemini_out = wrapper.call_gemini(session.get('prompt'))

if __name__ == '__main__':
    app.run(debug=True, port =5000)