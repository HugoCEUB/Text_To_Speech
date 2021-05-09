import PyPDF2
from gtts import gTTS


pdfFileObj = open("test.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

mytext = ""

for pageNum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)

    mytext += pageObj.extractText()
print(mytext)
pdfFileObj.close()

tts = gTTS(text=mytext, lang='pt-br')
tts.save("audiobook.mp3")
print("audiobook pronto!")
