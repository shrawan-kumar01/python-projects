import PyPDF2

a = PyPDF2.PdfFileReader('machine.pdf')
# print(a.documentInfo)
# print(a.getNumPages())
str = ""
for i in range (50,100):
    str += a.getPage(i).extract_text()

with open("text.txt" ,"w", encoding='utf-8') as f:
    f.write(str)






# print(a.getPage(5).extract_text())


