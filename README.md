# ReportLab
A module to understand basics of ReportLab

For the newer Reportlab 3.x, you can now use pip on all platforms:


pip install reportlab

Note that Reportlab 3.x only supports Python 2.7 and Python 3.3+. If you are on an older version of Python 2, then you have to use Reportlab 2.x.

1. Creating a Sample PDF file

2. TO create a PDF in landscape mode

3. Note that the default Canvas size is A4, so if you happen to be American, you’ll probably want to change that to letter size. This is easy to do in Reportlab.

4. To generate a form

5. Simple doc template

6. To insert Image to PDF

8. PDF Encryption
The StandardEncryption constructor takes the following arguments:
def __init__(self, userPassword, ownerPassword=None,
                   canPrint=1,
                   canModify=1,
                   canCopy=1,
                   canAnnotate=1,
                   strength=40):

9. PLATYPUS - Page Layout and Typography Using Scripts