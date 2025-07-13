Prerequisites for Running the hello_azure_openai.py:
  
  1. Azure Account and Resource:  
    - You need an active Azure account.
    - You must have successfully created an Azure OpenAI Service resource in the Azure Portal.
    - Within that resource, you need to have deployed a model (e.g., gpt-35-turbo or gpt-4) with a specific deployment name (e.g., test-chat, my-llm-deployment).
    - You will need the API Key and the Endpoint URL from your Azure OpenAI Service resource (under "Keys and Endpoint" in the Azure portal).
  
  2. Python Environment:
    - Install Python (3.7+ recommended).
    - Install the openai Python library:
      Bash: pip install openai
   
  This is a simple Python script that interacts with the Azure OpenAI Chat Completion API.
  Purpose: To demonstrate that you can programmatically connect to and get a response from an LLM deployed on Azure.

Prerequisites for Running the simple_tokenizer_demo.py:
  
  1. Python: You only need Python installed (3.x recommended).
  2. No external libraries other than re which is built-in.
  How to Run:
  
  1. Save the code above as simple_tokenizer_demo.py.
  2. Open your terminal or command prompt.
  3. Navigate to the directory where you saved the file.
  4. Run the command: python simple_tokenizer_demo.py
  
  This Python script will demonstrate how text is broken down into "tokens," a fundamental concept you learned. It uses a very basic word-based tokenizer, which is easy to understand and quick to run.
  
  Purpose: To visually show the concept of tokenization, illustrating the initial step an LLM takes when processing text.
