import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

doc = SimpleDocTemplate("06_image.pdf",pagesize=letter, rightMargin=72,
                      leftMargin=0.0 * inch ,
                      topMargin=0.0 * inch,
                      bottomMargin=0.0 * inch)
width, height = letter
print(width, height)
Story=[]
logo = "margin.png"
img_width = 50
img_height = 780
im = Image(filename='margin.png', width=img_width, height=img_height, hAlign='LEFT')
Story.append(im)
doc.build(Story)