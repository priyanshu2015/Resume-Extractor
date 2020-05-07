
# PyPDF2 can also be used to find the no. of pages in a pdf
# Problem with PyPDF2 : add extra \n while extracting text from PDF
# Thats why I used PDFminer to extract text from PDF

# For finding the font style of pdf using PyPDF2
from PyPDF2 import PdfFileReader
from pprint import pprint
import PyPDF2

def walk(obj, fnt, emb):
    '''
    If there is a key called 'BaseFont', that is a font that is used in the document.
    If there is a key called 'FontName' and another key in the same dictionary object
    that is called 'FontFilex' (where x is null, 2, or 3), then that fontname is 
    embedded.
    
    We create and add to two sets, fnt = fonts used and emb = fonts embedded.
    '''
    if not hasattr(obj, 'keys'):
        return None, None
    fontkeys = set(['/FontFile', '/FontFile2', '/FontFile3'])
    if '/BaseFont' in obj:
        fnt.add(obj['/BaseFont'])
    if '/FontName' in obj:
        if [x for x in fontkeys if x in obj]:# test to see if there is FontFile
            emb.add(obj['/FontName'])

    for k in obj.keys():
        walk(obj[k], fnt, emb)

    return fnt, emb     # return the sets for each page

def font_style(fname):
    #fname = r"C:\Users\Priyanshu Gupta\Desktop\Resume Extractor\priyanshu.pdf"
    pdf = PdfFileReader(fname)
    fonts = set()
    embedded = set()
    for page in pdf.pages:         # using PyPDF2 to traverse to each page 
        obj = page.getObject()
        # updated via this answer:
        # https://stackoverflow.com/questions/60876103/use-pypdf2-to-detect-non-embedded-fonts-in-pdf-file-generated-by-google-docs/60895334#60895334 
        # in order to handle lists inside objects. Thanks misingnoglic !
        # untested code since I don't have such a PDF to play with.
        if type(obj) == PyPDF2.generic.ArrayObject:  # You can also do ducktyping here
            for i in obj:
                if hasattr(i, 'keys'):
                    f, e = walk(i, fonts, embedded_fonts)
                    fonts = fonts.union(f)
                    embedded = embedded.union(e)
        else:
            f, e = walk(obj['/Resources'], fonts, embedded)
            fonts = fonts.union(f)
            embedded = embedded.union(e)
    #return fonts
    unembedded = fonts - embedded
    #print('Font List')
    fonts=sorted(list(fonts))
    if unembedded:
        #print('\nUnembedded Fonts')
        #print(unembedded)
        pass
    return fonts

#f=font_style(r"C:\Users\Priyanshu Gupta\Desktop\Resume Extractor\Resume_1.pdf")
#print(f)






