import pyttsx3
import PyPDF2
book = open('p3.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getPage(0)
text = page.extractText()
speaker.say("i love pokimane :D")
speaker.runAndWait()

