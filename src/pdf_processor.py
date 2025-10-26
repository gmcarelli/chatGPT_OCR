import fitz  # PyMuPDF
import base64

def convert_pdf_to_base64_images(pdf_path: str) -> list[str]:
    """
    Converts each page of a PDF file into a list of base64 encoded image strings.

    Args:
        pdf_path: The file path to the PDF document.

    Returns:
        A list of strings, where each string is a base64 encoded PNG image
        of a page from the PDF. Returns an empty list if the file cannot be opened.
    """
    base64_images = []
    try:
        pdf_document = fitz.open(pdf_path)
    except Exception as e:
        print(f"Error opening PDF {pdf_path}: {e}")
        return base64_images

    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap()
        img_bytes = pix.tobytes("png")
        base64_encoded_image = base64.b64encode(img_bytes).decode('utf-8')
        base64_images.append(base64_encoded_image)

    pdf_document.close()
    return base64_images
