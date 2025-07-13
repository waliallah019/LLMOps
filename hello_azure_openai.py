import os
import openai # Assuming openai library is installed via pip

# --- Configuration ---
# IMPORTANT: Replace these with your actual Azure OpenAI details
# It's best practice to use environment variables for sensitive info
AZURE_OPENAI_KEY = os.environ.get("AZURE_OPENAI_KEY", "YOUR_AZURE_OPENAI_KEY")
AZURE_OPENAI_ENDPOINT = os.environ.get("AZURE_OPENAI_ENDPOINT", "YOUR_AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_VERSION = "2024-02-15-preview" # Or your specific version
# This is the 'Deployment name' you created in Azure OpenAI Studio (e.g., 'test-chat')
AZURE_OPENAI_DEPLOYMENT_NAME = os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME", "YOUR_DEPLOYMENT_NAME") 

# --- Configure OpenAI client for Azure ---
# This setup is for the `openai` Python client library (v1.x.x)
openai.api_type = "azure"
openai.api_base = AZURE_OPENAI_ENDPOINT
openai.api_version = AZURE_OPENAI_API_VERSION
openai.api_key = AZURE_OPENAI_KEY

def get_chat_completion(prompt_text):
    """
    Sends a prompt to the Azure OpenAI Chat Completion API and returns the response.
    """
    try:
        response = openai.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT_NAME,
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt_text}
            ],
            temperature=0.7, # Controls randomness (0.0-1.0)
            max_tokens=150   # Maximum number of tokens to generate
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    print("--- Connecting to Azure OpenAI Service ---")
    user_prompt = "Explain LLMOps in two sentences."
    print(f"Sending prompt: '{user_prompt}'")

    response_content = get_chat_completion(user_prompt)

    print("\n--- LLM Response ---")
    print(response_content)

    print("\n--- Example 2: Another prompt ---")
    user_prompt_2 = "What are the main benefits of using Azure OpenAI Service over public OpenAI API?"
    print(f"Sending prompt: '{user_prompt_2}'")
    response_content_2 = get_chat_completion(user_prompt_2)
    print("\n--- LLM Response ---")
    print(response_content_2)