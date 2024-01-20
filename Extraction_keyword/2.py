import PyPDF2
from summa import keywords
def extract_text_from_pdf(pdf_path): 
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    return text

extracted_text = extract_text_from_pdf('./123.pdf')

TR_keywords = keywords.keywords(extracted_text, scores=True)
print(TR_keywords[0:10])