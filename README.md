# Ollama Python Client

A simple Python client for interacting with the Ollama API using an advanced custom assistant model.

## Setup

1. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Client

You can run the client using either of the provided scripts:

### Using `ollama_client.py`
This basic script sends a query to your advanced custom assistant model.
```bash
python ollama_client.py
```

### Using `ollama_client_refined.py`
This refined script includes error handling and a more robust structure for sending queries to your advanced custom assistant model.
```bash
python ollama_client_refined.py
```

## Usage

Both scripts query the advanced custom assistant model named `custom-assistant` with the prompt:
```python
prompt = "What is Python?"
```

To modify the model or the prompt, simply edit the respective variables in the scripts:
- In `ollama_client.py`:
  ```python
  model = "custom-assistant"  # Advanced custom model
  prompt = "What is Python?"
  ```
- In `ollama_client_refined.py`:
  ```python
  model = "custom-assistant"  # Advanced custom model
  prompt = "What is Python?"
  ```
