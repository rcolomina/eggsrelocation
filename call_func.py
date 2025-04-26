from enum import Enum

class PDFTypes(Enum):
    TXT = 0
    RTF = 1
    HTML = 3
class ConvertPDF(object):
    def __init__(self, convert_type):
        self.convert_type = convert_type
    def __call__(self):
        if self.convert_type == PDFTypes.TXT:
            return "toTXT"
        elif self.convert_type == PDFTypes.RTF:
            return "toRTF"
        elif self.convert_type == PDFTypes.HTML:
            return "toHTML"

toTxt   = ConvertPDF(PDFTypes.TXT)
toRTF   = ConvertPDF(PDFTypes.RTF)
toHTML  = ConvertPDF(PDFTypes.HTML)

print(toTxt())