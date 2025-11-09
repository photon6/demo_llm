# Dermatology LLM Demo

This project sets up a minimum viable product (MVP) demo for a dermatology-focused large language model (LLM) using the "brucewayne0459/OpenBioLLm-Derm" model. It includes a Python backend with FastAPI for inference and a Node.js frontend for the web UI. The setup is designed for local development on macOS ARM (Apple Silicon), but can be adapted.

## Prerequisites

- **Python 3.11**: The backend requires Python 3.11 for compatibility with libraries like Transformers. Install via pyenv (recommended for multiple versions) or Conda.
  - With pyenv: `pyenv install 3.11.9` and `pyenv global 3.11.9`.
- **Conda**: Use Miniconda or Anaconda for environment management. Download from [conda.io](https://conda.io). Initialize with `conda init` if not done.
- **Node.js**: Version 18+ for the frontend. Download from [nodejs.org](https://nodejs.org).
- **Hardware**: High-performing MacBook Pro with ARM (e.g., M3/M4) recommended for efficient inference.

## Installation

1. **Create Conda Environment**:

   ```
   conda create -n demo_llm python=3.11
   conda activate demo_llm
   ```

2. **Install Python Dependencies via PIP** (in the activated env):

   ```
   pip install fastapi uvicorn transformers torch protobuf sentencepiece python-multipart accelerate
   ```

   - `fastapi`: For the API server.
   - `uvicorn`: For running FastAPI.
   - `transformers`: For loading the LLM.
   - `torch`: PyTorch backend (use `pip install torch` for ARM compatibility).
   - `protobuf`, `sentencepiece`: For model configs/tokenizers.
   - `python-multipart`: For form data (e.g., prompts).
   - `accelerate`: For device mapping.

3. **Install Node.js Dependencies** (in the frontend directory):
   ```
   npm init -y
   npm install express
   ```

## Configuration

Create a `config.json` file in the project root (for Python backend) with the following content:

```json
{
  "model_id": "brucewayne0459/OpenBioLLm-Derm",
  "host": "0.0.0.0",
  "port": 8000
}
```

For the Node.js frontend, create a `config.json` in its directory:

```json
{
  "port": 3000
}
```

These allow easy changes to model, host, and ports without code edits.

## Running the Application

1. **Start the Backend First** (in the backend directory, with Conda env activated):

   ```
   python app.py
   ```

   - This loads the model and starts the FastAPI server on the configured host/port (default: http://localhost:8000).

2. **Start the Frontend** (in the frontend directory):
   ```
   node server.js
   ```
   - This starts the Express server on the configured port (default: http://localhost:3000).
   - Open the URL in your browser to interact with the UI (submit prompts for dermatology queries).

## Troubleshooting

- **Model Loading Issues**: If crashes occur (e.g., mutex errors on ARM), set `export PYTORCH_ENABLE_MPS_FALLBACK=1` before running.
- **CORS Errors**: Ensure CORSMiddleware is added in `app.py` if UI fetch fails.
- **Dependencies**: If conflicts, use `pip check` or recreate the env.
