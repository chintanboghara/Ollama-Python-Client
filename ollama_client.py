import ollama

# Initialize the Ollama client
client = ollama.Client()

# Define the model (updated to the advanced custom assistant) and the input prompt
model = "custom-assistant"  # This should match the model name created with the advanced Modelfile
prompt = "What is Python?"

# Send the query to the model
response = client.generate(model=model, prompt=prompt)

# Print the response from the model
print("Response from Ollama:")
print(response.response)
