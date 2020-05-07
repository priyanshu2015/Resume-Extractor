import minecart
from PyPDF2 import PdfFileReader


def image_finder(path):
    pdf = PdfFileReader(path)
    pdffile = open(path, 'rb')
    noOfPages=pdf.getNumPages()      # using PyPDF2 to get count of no. of pages
    #print(noOfPages)
    doc = minecart.Document(pdffile)
    count=0
    for i in range(noOfPages):
        page = doc.get_page(i)
        #for shape in page.shapes.iter_in_bbox((0, 0, 100, 200)):
            #print(shape.path, shape.fill.color.as_rgb())
        count+=len(page.images)
    return(count)
    #im = page.images[0].as_pil()  # requires pillow
    #im.show()
    #print(count)
    #print(len(page.images))
#c=image_finder(r"C:\Users\Priyanshu Gupta\Desktop\Resume Extractor\Resume_1.pdf")
#print(c)

