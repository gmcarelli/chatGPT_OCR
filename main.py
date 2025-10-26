import os
import argparse
from src.pdf_processor import convert_pdf_to_base64_images
from src.openai_client import get_transcription_from_openai

def main():
    """
    Main function to process PDF files in a directory and transcribe them using OpenAI.
    """
    parser = argparse.ArgumentParser(
        description="Transcribe handwritten text from PDF files using OpenAI's GPT-4o."
    )
    parser.add_argument(
        "input_dir",
        type=str,
        help="The path to the directory containing the PDF files.",
    )
    args = parser.parse_args()

    input_dir = args.input_dir
    output_dir = "temp"

    if not os.path.isdir(input_dir):
        print(f"Error: The directory '{input_dir}' does not exist.")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: '{output_dir}'")

    print(f"Scanning for PDF files in '{input_dir}'...")

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(input_dir, filename)
            print(f"Processing file: {filename}")

            # 1. Convert PDF to images
            base64_images = convert_pdf_to_base64_images(pdf_path)
            if not base64_images:
                print(f"  -> Could not extract images from {filename}. Skipping.")
                continue

            print(f"  -> Extracted {len(base64_images)} page(s).")

            # 2. Get transcription from OpenAI
            print("  -> Sending to OpenAI for transcription...")
            transcribed_text = get_transcription_from_openai(base64_images)

            # 3. Save the result
            output_filename = os.path.splitext(filename)[0] + ".txt"
            output_path = os.path.join(output_dir, output_filename)

            try:
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(transcribed_text)
                print(f"  -> Successfully saved transcription to '{output_path}'")
            except IOError as e:
                print(f"  -> Error saving transcription for {filename}: {e}")
        else:
            print(f"Ignoring non-PDF file: {filename}")

    print("\nProcessing complete.")

if __name__ == "__main__":
    main()
