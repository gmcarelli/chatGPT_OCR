# PDF Manuscript Transcriber

This project contains a set of Python scripts to transcribe handwritten text from PDF documents using the OpenAI GPT-4o API.

## Features

-   Processes all PDF files in a specified directory.
-   Converts each PDF page into an image.
-   Sends images to the OpenAI API for transcription.
-   Saves the transcribed text to a `.txt` file in a `temp` directory.

## Project Structure

```
.
├── .env
├── .gitignore
├── main.py
├── README.md
├── requirements.txt
└── src
    ├── __init__.py
    ├── openai_client.py
    └── pdf_processor.py
```

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure your API Key:**
    -   Rename the `.env` file and add your OpenAI API key:
        ```
        OPENAI_API_KEY="your_secret_api_key"
        ```

## Usage

1.  Place all the PDF files you want to transcribe into a directory (e.g., `my_pdfs/`).

2.  Run the main script from the command line, passing the path to your directory:
    ```bash
    python main.py path/to/your/pdfs
    ```

3.  The script will process each PDF file and save the transcriptions in the `temp/` directory. Each output file will have the same name as the corresponding input PDF, but with a `.txt` extension.
