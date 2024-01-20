import fitz  # PyMuPDF
import PyPDF2
from spire.pdf import *
from spire.pdf.common import *
import openai
    

# @get text form the pdf file and return it
# @input: pdf file path
# @output: pdf file 's text
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

# @create new pdf file based on original file and keyword
# @input: original, new file path, extract keyword
# @output: new pdf file


def bold_keywords(input_pdf, output_pdf, keywords):
    # Open the existing PDF
    pdf = PdfDocument()

    pdf.LoadFromFile(input_pdf)
    
    for i in range(pdf.Pages.Count):
        page = pdf.Pages.get_Item(i)  
        print(keywords.split(', '))
        key_list = keywords.split(', ')
        for keyword in key_list:
            result = page.FindText(keyword, TextFindParameter.IgnoreCase).Finds
            for text in result:
                text.ApplyHighLight(Color.get_Cyan())
    pdf.SaveToFile(output_pdf)
    pdf.Close()



# @extract text form the pdf file with openai
# @input: text, which is extracted
# @output: String
def get_extract_keywords(text, prompt="In the text below, print 10 words only very important words that imply the content of the document."):

    openai.api_key = "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"    #write your API key......

    response = openai.chat.completions.create(
        model="gpt-4",  # Replace with appropriate GPT model name
        messages=[
            {"role": "user", "content": prompt + text}
        ]
    )
    return (response.choices[0].message.content)


if __name__ == "__main__":
    bold_keywords('./test.pdf', './test_1.pdf', get_extract_keywords(extract_text_from_pdf('./test.pdf')))
    bold_keywords('./test.pdf', './test_2.pdf', get_extract_keywords(extract_text_from_pdf('./test.pdf'), prompt = "Extract important keyword based on next data"))
