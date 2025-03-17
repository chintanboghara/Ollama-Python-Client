import ollama

def main():
    # Initialize the Ollama client
    client = ollama.Client()

    # Define the model (updated to the advanced custom assistant) and the input prompt
    model = "custom-assistant"  # This should match the model name created with your advanced Modelfile
    prompt = "What is Python?"

    try:
        # Send the query to the model
        response = client.generate(model=model, prompt=prompt)

        # Print the response from the model
        print("Response from Ollama:")
        print(response.response)

    except Exception as e:
        # Handle any errors that occur during the request
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
