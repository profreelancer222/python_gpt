from spire.pdf import *

from spire.pdf.common import*

 


pdf = PdfDocument()

pdf.LoadFromFile("123.pdf")
for i in range(pdf.Pages.Count):
    page = pdf.Pages.get_Item(i)  
    result = page.FindText("and", TextFindParameter.IgnoreCase).Finds
    for text in result:
        text.ApplyHighLight(Color.get_Cyan())
pdf.SaveToFile("output/FindHighlight.pdf")
pdf.Close()
