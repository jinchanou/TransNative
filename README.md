# TransNative
A Smarter, More Context-Aware Chinese-to-English Translator.

## Quick Start

Windows users can directly run the `start.bat` script to launch the application, which will automatically start the backend and frontend services.

Alternatively, follow the steps below to start manually:

## Features

  - Translates Chinese into various authentic American English expressions.
  - Provides high-quality translation using the latest Doubao model, with Doubao Pro model as a backup.
  - Clean and easy-to-use Web interface.
  - Supports multiple translation options to suit different contexts.
  - Translation results include usage scenarios and target audience descriptions to avoid misuse.

## Technical Architecture

  - **Backend**: FastAPI (Python)
  - **Frontend**: HTML + JavaScript
  - **Translation Engine**: DeepSeek API (Preferred) + DeepSeek Pro API (Backup)

## Installation and Running

1.  Clone the project code:

    ```bash
    git clone <repository-url>
    cd TransNative
    ```

2.  Create a virtual environment and install dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    # Or venv\Scripts\activate  # Windows
    pip install -r requirements.txt
    ```

3.  Configure environment variables:
    Set your API key in the `.env` file:

    ```bash
    # DeepSeek API Configuration
    DEEPSEEK_API_KEY=your_deepseek_api_key_here
    DEEPSEEK_ENDPOINT=https://api.deepseek.com/chat/completions
    ```

4.  Run the application:

    ```bash
    # Method 1: Use the startup script (Windows)
    start.bat

    # Method 2: Start services separately
    python main.py
    # Run in another terminal:
    # python -m http.server 8001
    ```

5.  Access the application:
    Open your browser and visit `http://localhost:8001` to view the frontend interface.
    API documentation is available at `http://localhost:8000/docs`.

## API Endpoints

### Translation API

  - **URL**: `/translate`
  - **Method**: POST
  - **Request Parameters**:
    ```json
    {
      "text": "Chinese text to be translated"
    }
    ```
  - **Response**:
    ```json
    {
      "translations": [
        "Authentic English translation 1",
        "Authentic English translation 2",
        "Authentic English translation 3"
      ]
    }
    ```

## Deployment

The application can be deployed using the following methods:

1.  Using Docker (Recommended)
2.  Deploying to a cloud server
3.  Using serverless functions (e.g., Vercel, Netlify, etc.)

## Contribution

We welcome Issues and Pull Requests to improve this project.

## License

[MIT License](https://www.google.com/search?q=LICENSE)
