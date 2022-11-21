import sys
import pyttsx3
import PyPDF2


if __name__ == "__main__":
    """
    Run this script passing in the filename you want to read.
    EX:
        python main.py test.pdf
    """
    speaker = pyttsx3.init()

    filename = sys.argv[-1]
    book = open(filename, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(book)
    
    # TODO: parse out junk from text
    text_to_speech = " ".join(
        [pdf_reader.getPage(i).extract_text() for i in range(pdf_reader.numPages)]
    )


    speaker.say(text_to_speech)
    speaker.runAndWait()

