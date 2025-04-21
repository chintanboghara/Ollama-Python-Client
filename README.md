# Ollama Python Client

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/) <!-- Optional: Add relevant badges -->

A simple Python client demonstrating interaction with a locally running Ollama API, specifically targeting a custom assistant model.

This project provides two basic scripts to send prompts to an Ollama model and retrieve responses. It's designed as a starting point for building more complex applications using Ollama.

## Features

*   Simple examples for querying the Ollama API.
*   Demonstrates basic API calls (`ollama_client.py`).
*   Includes a refined version with error handling (`ollama_client_refined.py`).
*   Easily configurable model name and prompt.
*   Requires minimal dependencies.

## Prerequisites

Before running the client, ensure you have the following:

1.  **Python:** Version 3.8 or higher recommended.
2.  **Ollama:** Installed and running locally. You can download it from [ollama.com](https://ollama.com/).
3.  **Custom Model:** The specific Ollama model you intend to query (default: `custom-assistant`) must be available in your running Ollama instance. You can pull or create models using the Ollama CLI (e.g., `ollama pull <model_name>` or by defining a `Modelfile`).
4.  **Dependencies:** Python packages listed in `requirements.txt`.

## Installation

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone https://github.com/chintanboghara/Ollama-Python-Client.git
    cd Ollama-Python-Client
    ```

2.  **Install the required Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *This typically includes libraries like `requests` or the official `ollama` Python package, depending on your implementation.*

## Running the Client

Ensure your Ollama service is running in the background. You can then run the example scripts:

### 1. Basic Client (`ollama_client.py`)

This script provides a straightforward example of sending a prompt to the specified Ollama model and printing the response. It lacks robust error handling.

```bash
python ollama_client.py
```

### 2. Refined Client (`ollama_client_refined.py`)

This script builds upon the basic example by incorporating error handling (e.g., for connection issues or model not found errors) and provides a slightly more structured approach.

```bash
python ollama_client_refined.py
```

## Usage and Customization

Both scripts are pre-configured to query the `custom-assistant` model with the prompt "What is Python?".

**To change the model or prompt:**

Edit the relevant variables directly within the Python script files:

*   **In `ollama_client.py`:**
    ```python
    # --- Configuration ---
    MODEL_NAME = "custom-assistant"  # Replace with your target Ollama model
    PROMPT_TEXT = "What is Python?"  # Replace with your desired prompt
    OLLAMA_API_URL = "http://localhost:11434/api/generate" # Default API endpoint
    # -------------------
    ```

*   **In `ollama_client_refined.py`:**
    ```python
    # --- Configuration ---
    MODEL_NAME = "custom-assistant"  # Replace with your target Ollama model
    PROMPT_TEXT = "What is Python?"  # Replace with your desired prompt
    OLLAMA_API_URL = "http://localhost:11434/api/generate" # Default API endpoint
    # -------------------
    ```

**Important:** Ensure the `MODEL_NAME` you specify corresponds to a model that exists in your running Ollama instance.

## Configuration

*   **Ollama API Endpoint:** The scripts assume Ollama is running on the default address (`http://localhost:11434`). If your Ollama service is running on a different host or port, you'll need to update the `OLLAMA_API_URL` variable in the scripts accordingly. The example above shows where this might be defined. *Note: Adapt the variable name and location based on your actual script implementation.*

## Troubleshooting

*   **ConnectionError / Connection Refused:** Ensure the Ollama application or service is running locally. Check if it's accessible on `http://localhost:11434`.
*   **Model Not Found Error (e.g., 404 Not Found):** Verify that the model specified in the `MODEL_NAME` variable (`custom-assistant` by default) has been pulled or created in your Ollama instance. Use `ollama list` in your terminal to see available models.
*   **Dependency Errors:** Ensure you have installed the required packages using `pip install -r requirements.txt`. Consider using a virtual environment.
