
# count no. text lines and no. of characters on each page of pdf
import fitz
import nltk
import pandas as pd


def total_lines_and_char(path):
    pdf_document = path
    doc = fitz.open(pdf_document)
    #print ("number of pages: %i" % doc.pageCount)
    #print(doc.pageCount)
    #print(doc.metadata)
    total=[]
    for i in range(doc.pageCount):
        page1 = doc.loadPage(i)
        page1text = page1.getText("text")
        #print(page1text)
        sen=[]
        count=0
        sen=[el.strip() for el in page1text.split("\n") if len(el) > 0]
        for j in sen:
            #print(j)
            count+=len(j)
        #print(len(sen))
        #df['Textline+Totalchar on each Page']=count
        total.append(len(sen)+count)
        #print(count)
        #print(len(sen))
    return total
#print(df['Textline+Totalchar on each Page'])
#print(page1text)