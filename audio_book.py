# Python program to show
import PyPDF2
# how to convert text to speech
import pyttsx3
import datetime
# Initialize the converter
converter = pyttsx3.init()

# Set properties before adding
# Things to say
# Sets speed percent
# Can be more than 100
converter.setProperty('rate', 160)
# Set volume 0-1
converter.setProperty('volume', 1)
voices = converter.getProperty('voices')
converter.setProperty('voice', voices[1].id) #changing index changes voices but ony 0 and 1 are working here

# Open the PDF file
book = open("class.pdf", "rb")
pdf_reader = PyPDF2.PdfFileReader(book)

# if pdf contains more then one pages
pages = pdf_reader.numPages
print("Total Pages: ", pages)

for page_num in range(pages):
    print("Current page: ", page_num + 1)
    page = pdf_reader.getPage(page_num)  # getting each pages from pdf

    text = page.extractText()  # extracting text from current page
    print(text)
    converter.say(text)  # now extract text will passed here to listen
    curr_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    converter.save_to_file(text, f"{curr_datetime}.mp3")
    converter.runAndWait()

# Empties the say() queue
# Program will not continue
# until all speech is done talking
converter.runAndWait()