import pdfplumber
# %%--------------------------------------------------------------------------------------------------------------------
def extract_with_pdfplumber(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text
# %%--------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    pdf_file = "Sample.pdf"
    pdfplumber_text = extract_with_pdfplumber(pdf_file)
    print("Text extracted with pdfplumber:")
    print(pdfplumber_text)