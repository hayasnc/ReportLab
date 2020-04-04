from reportlab.pdfgen import canvas

from reportlab.lib.pagesizes import landscape, letter


c = canvas.Canvas("landscape.pdf")
c.setPageSize( landscape(letter) )
c.drawString(200,500,"Welcome to Reportlab in Landscape!")
c.save()