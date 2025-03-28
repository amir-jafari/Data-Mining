import fitz
# %%--------------------------------------------------------------------------------------------------------------------
def extract_with_fitz(file_path):
    text = ""
    with fitz.open(file_path) as pdf:
        for page_num, page in enumerate(pdf, start=1):
            text += f"--- Page {page_num} ---\n"
            text += page.get_text()
            text += "\n"
    return text
# %%--------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    pdf_file = "Sample.pdf"
    extracted_text = extract_with_fitz(pdf_file)
    print("Text extracted using PyMuPDF (fitz):")
    print(extracted_text)