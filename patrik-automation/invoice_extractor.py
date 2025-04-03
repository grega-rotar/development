import os
import fitz
import json
import requests
from google import genai
from dotenv import load_dotenv
import re
import tempfile


def extract_invoice_data(pdf_path_or_url):
    """
    Extracts invoice amount, VAT percentage, and shipping amount from a PDF,
    whether it's a local file path or a URL.

    Args:
        pdf_path_or_url (str): Path to the PDF file or a URL pointing to a PDF.

    Returns:
        dict: A dictionary containing the extracted data, or None if an error occurs.
    """
    load_dotenv()

    API_KEY = os.getenv("GENAI_API_KEY")
    if not API_KEY:
        print("Error: GENAI_API_KEY not found in environment variables.")
        return None

    client = genai.Client(api_key=API_KEY)

    try:
        if pdf_path_or_url.startswith("http://") or pdf_path_or_url.startswith(
            "https://"
        ):
            # Download the PDF from the URL
            response = requests.get(pdf_path_or_url)
            response.raise_for_status()  # Raise an exception for bad status codes

            # Create a temporary file to save the PDF within ./temp
            temp_dir = "./temp"
            os.makedirs(temp_dir, exist_ok=True) # Ensure temp directory exists

            with tempfile.NamedTemporaryFile(delete=False, dir=temp_dir) as temp_pdf:
                temp_pdf.write(response.content)
                temp_pdf_path = temp_pdf.name

            doc = fitz.open(temp_pdf_path)

        else:
            # Open the PDF from the local file path
            doc = fitz.open(pdf_path_or_url)

        all_pages_text = ""
        for page in doc:
            all_pages_text += page.get_text()
        prompt = f"""
            Extract the invoice amount, VAT percentage, and shipping amount from the following text and return them in JSON format. If a value cannot be found, use "x" as the placeholder. If vat value cannot be found than it should be set to 0.
            Amount and shipping should be in xxxxx.xx format.
            Text:
            {all_pages_text}

            JSON format:
            {{
            "amount": "value" or "x",
            "vat": "value" or "x",
            "shipping": "value" or "x"
            }}
            """

        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=prompt
        )
        extracted_json_str = response.text

        # Replace non-standard whitespace with standard spaces
        extracted_json_str = re.sub(r"\s", " ", extracted_json_str)

        # Remove the ```json and ``` if present
        extracted_json_str = extracted_json_str.replace("```json", "")
        extracted_json_str = extracted_json_str.replace("```", "")
        extracted_json_str = extracted_json_str.strip()

        extracted_json = json.loads(extracted_json_str)

        if pdf_path_or_url.startswith("http://") or pdf_path_or_url.startswith("https://"):
            os.unlink(temp_pdf_path) #delete temp file

        return extracted_json

    except json.JSONDecodeError:
        print("Error: Could not decode the response as JSON.")
        print(
            "Raw response text:",
            response.text if "response" in locals() else "No response",
        )
        if pdf_path_or_url.startswith("http://") or pdf_path_or_url.startswith("https://"):
            os.unlink(temp_pdf_path)
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error downloading PDF from URL: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        if pdf_path_or_url.startswith("http://") or pdf_path_or_url.startswith("https://"):
            os.unlink(temp_pdf_path)
        return None


if __name__ == "__main__":
    # Example Usage:
    pdf_file_path = "temp/example.pdf"  # Replace with your PDF file path
    pdf_url = "https://mypromode.eu/41/out/xrechk/pdf/00045000/Creaglobe-Invoice_KAONY_Sarl___LOC_Surf_3606974.pdf" # Replace with your PDF URL
    extracted_data_path = extract_invoice_data(pdf_file_path)
    extracted_data_url = extract_invoice_data(pdf_url)

    if extracted_data_path:
        print("Path result:")
        print(json.dumps(extracted_data_path, indent=2))
    if extracted_data_url:
        print("URL result:")
        print(json.dumps(extracted_data_url, indent=2))