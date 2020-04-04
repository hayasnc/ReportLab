import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import pdfencrypt
enc=pdfencrypt.StandardEncryption("passcode",canPrint=0)
doc = SimpleDocTemplate("08_simple_doc_template_encryption.pdf",pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18,
                        encrypt=enc)

Story=[]
formatted_time = time.ctime()

styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

ptext = '<font size="12">%s</font>' % formatted_time
Story.append(Paragraph(ptext, styles["Normal"]))

logo = "python_logo.png"
magName = "Pythonista"
issueNum = 12
subPrice = "99.00"
limitedDate = "03/05/2010"
freeGift = "tin foil hat"
ptext = '<font size="12">We would like to welcome you to our subscriber base for %s Magazine! \
        You will receive %s issues at the excellent introductory price of $%s. Please respond by\
        %s to start receiving your subscription and get the following free gift: %s.</font>' % (magName, 
                                                                                                issueNum,
                                                                                        subPrice,
                                                                                                limitedDate,
                                                                                              freeGift)
Story.append(Spacer(1, 12))

Story.append(Paragraph(ptext, styles["Justify"]))

doc.build(Story)
