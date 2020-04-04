from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

c = canvas.Canvas('letter_size.pdf', pagesize=letter)
width, height = letter
print(width, height)
c.drawString(100,750,"Letter Size PDF")
c.save()