# converting an text written book into audio book
import pyttsx3
import PyPDF2

book = open('One Indian Girl-Chetan Bhagat.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
#print(pages)

speaker = pyttsx3.init()
for i in range(13, pages):
    page = pdfReader.getPage(i)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()