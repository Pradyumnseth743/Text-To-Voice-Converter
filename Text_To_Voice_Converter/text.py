import pyttsx3
import PyPDF2
book=open('D:\Full_Stack_Development_Report.pdf','rb')
pdfReader=PyPDF2.PdfReader(book)
pages=len(pdfReader.pages)
speaker=pyttsx3.init()
n=int(input("Enter Page Number : "))
page=pdfReader.pages[n-1]
text=page.extract_text()
speaker.say(text)
speaker.runAndWait()