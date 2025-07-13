# LLM Fundamentals Demos for "Operationalizing LLMs on Azure" Course

This repository contains two Python scripts demonstrating foundational concepts learned in the first two modules of the "Operationalizing LLMs on Azure - Duke University" course.

---

## 1. `hello_azure_openai.py`

This script demonstrates programmatic interaction with a Large Language Model deployed on Microsoft Azure's OpenAI Service.

**Purpose:** To showcase how to connect to and receive responses from an LLM hosted in your Azure environment, illustrating a core component of LLM operationalization.

### Prerequisites

1.  **Azure OpenAI Service Resource:**
    *   An active Azure account is required.
    *   You must have successfully created an [Azure OpenAI Service resource](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=rest-api) in the Azure Portal.
    *   Within that resource, you need to have [deployed a model](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=rest-api#deploy-a-model) (e.g., `gpt-35-turbo` or `gpt-4`). Make note of your **Deployment Name** (e.g., `test-chat`, `my-llm-deployment`).
    *   You will need the **API Key** and the **Endpoint URL** from your Azure OpenAI Service resource (found under the "Keys and Endpoint" section in the Azure portal).

2.  **Python Environment:**
    *   Python (3.7+ recommended) installed on your system.
    *   The `openai` Python library:
        ```bash
        pip install openai
        ```

### How to Run

1.  **Configure Environment Variables (Recommended for Security):**
    It is highly recommended to set your Azure OpenAI credentials as environment variables to keep sensitive information out of your code.
    *   **Linux/macOS:**
        ```bash
        export AZURE_OPENAI_KEY="YOUR_AZURE_OPENAI_KEY"
        export AZURE_OPENAI_ENDPOINT="YOUR_AZURE_OPENAI_ENDPOINT"
        export AZURE_OPENAI_DEPLOYMENT_NAME="YOUR_DEPLOYMENT_NAME"
        ```
    *   **Windows (Command Prompt):**
        ```cmd
        set AZURE_OPENAI_KEY="YOUR_AZURE_OPENAI_KEY"
        set AZURE_OPENAI_ENDPOINT="YOUR_AZURE_OPENAI_ENDPOINT"
        set AZURE_OPENAI_DEPLOYMENT_NAME="YOUR_DEPLOYMENT_NAME"
        ```
    *   **Windows (PowerShell):**
        ```powershell
        $env:AZURE_OPENAI_KEY="YOUR_AZURE_OPENAI_KEY"
        $env:AZURE_OPENAI_ENDPOINT="YOUR_AZURE_OPENAI_ENDPOINT"
        $env:AZURE_OPENAI_DEPLOYMENT_NAME="YOUR_DEPLOYMENT_NAME"
        ```
    *(Alternatively, for quick testing, you can directly replace the placeholder values within the `hello_azure_openai.py` file, but **do not commit keys directly into your repository**).*

2.  **Execute the Script:**
    Navigate to the directory containing `hello_azure_openai.py` in your terminal and run:
    ```bash
    python hello_azure_openai.py
    ```

---

## 2. `simple_tokenizer_demo.py`

This script provides a straightforward demonstration of text tokenization, a fundamental concept in how Large Language Models process language.

**Purpose:** To visually illustrate the initial step an LLM takes when processing text input, breaking it down into discrete "tokens."

### Prerequisites

1.  **Python:**
    *   Python (3.x recommended) installed on your system.
2.  **No External Libraries:**
    *   This script uses only built-in Python modules (`re`).

### How to Run

1.  Navigate to the directory containing `simple_tokenizer_demo.py` in your terminal.
2.  Execute the script using the Python interpreter:
    ```bash
    python simple_tokenizer_demo.py
    ```

---
