import tiktoken

# Get the encoding used by a specific model (e.g. gpt-4, gpt-3.5-turbo)
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

# Encode a string into tokens
text = "Hello, my name is ChatGPT!"
tokens = encoding.encode(text)

print(f"Tokens: {tokens}")
print(f"Token count: {len(tokens)}")

# Decode tokens back into string
decoded = encoding.decode(tokens)
print(f"Decoded: {decoded}")
