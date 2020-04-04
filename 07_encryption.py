from reportlab.pdfgen import canvas
from reportlab.lib import pdfencrypt
enc=pdfencrypt.StandardEncryption("passcode",canPrint=0)
def hello(c):
    c.drawString(100,100,"How to Encrypt")
c = canvas.Canvas("07_encryption.pdf",encrypt=enc)
hello(c)
c.showPage()
c.save()
