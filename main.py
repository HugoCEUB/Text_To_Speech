# instalar as bibliotecas a seguir no terminal:

# pip install tk
# pip install PyPDF2
# pip install gTTS

from tkinter.filedialog import askopenfilename
import PyPDF2
from gtts import gTTS

pdfFileObj = askopenfilename()
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

mytext = ""

for pageNum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)

    mytext += pageObj.extractText()
print(mytext)

tts = gTTS(text=mytext, lang='pt-br')
tts.save("audiobook.mp3")
print("audiobook pronto!")
