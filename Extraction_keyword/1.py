import yake
import PyPDF2
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

kw_extractor = yake.KeywordExtractor(top=20, stopwords=None)
keywords = kw_extractor.extract_keywords(extracted_text)
for kw, v in keywords:
  print(kw, ": score", v)
  
  