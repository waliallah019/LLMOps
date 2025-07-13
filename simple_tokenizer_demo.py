import re

def simple_word_tokenizer(text):
    """
    A basic tokenizer that splits text into words, treating punctuation as separate tokens.
    It simulates how an LLM might break down input.
    """
    # Convert to lowercase to normalize (optional, but common in NLP)
    text = text.lower()
    
    # Use regex to split by whitespace and capture punctuation as separate tokens
    # This regex means: split by whitespace, but keep alphanumeric sequences and punctuation.
    # It's a very simplified tokenizer, not as complex as actual LLM tokenizers (e.g., BPE)
    tokens = re.findall(r'\b\w+\b|[.,!?;\"\':()]', text)
    
    # Filter out empty strings that might result from multiple spaces or complex regex
    tokens = [token for token in tokens if token]
    
    return tokens

if __name__ == "__main__":
    print("--- Simple Tokenizer Demonstration ---")
    
    example_texts = [
        "What is a tokenizer?",
        "Today is a sunny day.",
        "LLMOps is cool, isn't it?",
        "The quick brown fox jumps over the lazy dog.",
        "It's 24/7 support!" # Demonstrates basic handling of special chars
    ]
    
    for i, text in enumerate(example_texts):
        print(f"\n--- Example {i+1} ---")
        print(f"Original Text: '{text}'")
        tokens = simple_word_tokenizer(text)
        print(f"Tokens: {tokens}")
        print(f"Number of Tokens: {len(tokens)}")

    print("\n--- Why is this important? ---")
    print("LLMs convert text into these numerical 'tokens' before any processing.")
    print("Understanding tokenization is the first step to understanding how LLMs 'read' and 'write'.")
    print("It also explains why some words or punctuation might be treated as separate units,")
    print("and why LLM costs are often based on 'tokens' rather than just 'words'.")