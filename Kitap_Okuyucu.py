import pyttsx3
import PyPDF2

hikaye = open("deep-learning.pdf","rb")
pdfOkuyucu = PyPDF2.PdFileReader(hikaye)

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

for sayfa_numarası in range(0, pdfOkuyucu.numPages):
	sayfa = pdfOkuyucu.getPage(sayfa_numarasi)
	yazi = sayfa.extractText()
	engine.say(yazi)
	engine.runAndWait()