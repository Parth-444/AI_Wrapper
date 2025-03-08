from llm_wrapper.llm_client import LLMWrapper
from llm_wrapper.classifier import categorize_prompt


def main():
    wrapper = LLMWrapper()

    while True:
        user_prompt = input("\n📝 Enter your prompt (or type 'exit' to quit): ")
        if user_prompt.lower() == "exit":
            print("👋 Exiting...")
            break

        # Classify prompt
        model_type = categorize_prompt(user_prompt).strip()
        print(f"🔍 Classified as: {model_type.upper()}")
        print(model_type)
        # Call the appropriate model
        if "Logical/Programming." in model_type.split() or "Logical/Programming" in model_type.split():
            response = wrapper.call_llama(user_prompt)
        else:
            response = wrapper.call_gemini(user_prompt)

        print("\n💬 Response:\n", response)


if __name__ == "__main__":
    main()



