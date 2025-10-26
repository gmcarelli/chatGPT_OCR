import os
from openai import OpenAI
from dotenv import load_dotenv

def get_transcription_from_openai(base64_images: list[str]) -> str:
    """
    Sends a list of base64 encoded images to the OpenAI API for transcription.

    Args:
        base64_images: A list of base64 encoded image strings.

    Returns:
        A single string containing the transcribed text from all images,
        with page separators. Returns an error message if the API key is not found
        or if the API call fails.
    """
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return "Error: OPENAI_API_KEY not found in .env file."

    client = OpenAI(api_key=api_key)
    transcribed_text = []

    prompt = """
You are an OCR transcription assistant specialized in accurately converting handwritten text from PDF documents into digital text.

Your main objective is to transcribe the text exactly as it appears in the original document, without correcting or interpreting any errors.
The document is written in Portuguese (Brazilian). You must preserve the original language — do not translate, correct, or modify the text.

Maintain all original spelling mistakes, grammatical issues, punctuation, capitalization, and line breaks.
If a word or section is unreadable, write [ilegível] in its place (use Portuguese for this placeholder).

Guidelines:
- Keep the same paragraph and line structure as the handwritten document.
- Do not add explanations, comments, or notes.
- Output only the transcribed text, nothing else.
"""

    for i, base64_image in enumerate(base64_images):
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": prompt},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/png;base64,{base64_image}"
                                },
                            },
                        ],
                    }
                ],
                max_tokens=2048,
            )
            page_text = response.choices[0].message.content
            transcribed_text.append(f"--- Página {i+1} ---\n{page_text}")
        except Exception as e:
            return f"Error during OpenAI API call for page {i+1}: {e}"

    return "\n\n".join(transcribed_text)
