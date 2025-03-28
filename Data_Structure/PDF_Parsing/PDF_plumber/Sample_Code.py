import pdfplumber


def extract_with_pdfplumber(file_path):
    """
    Extracts text from a PDF using pdfplumber.
    """
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text


def compare_texts(text1, text2):
    """
    Compares two texts and identifies differences.
    """
    import difflib
    differ = difflib.Differ()
    diff = list(differ.compare(text1.splitlines(), text2.splitlines()))
    return "\n".join(diff)


if __name__ == "__main__":
    # Path to your PDF file
    pdf_file = "Sample.pdf"  # Replace with the path to your PDF file

    # Extract text using pdfplumber
    pdfplumber_text = extract_with_pdfplumber(pdf_file)
    print("Text extracted with pdfplumber:")
    print(pdfplumber_text)

    # Compare the results (in this case, comparing text with itself for demonstration)
    print("\nComparison of extracted texts:")
    differences = compare_texts(pdfplumber_text, pdfplumber_text)
    print(differences)