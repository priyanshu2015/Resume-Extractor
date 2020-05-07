# from pdfminer3.layout import LAParams, LTTextBox
# from pdfminer3.pdfpage import PDFPage
# from pdfminer3.pdfinterp import PDFResourceManager
# from pdfminer3.pdfinterp import PDFPageInterpreter
# from pdfminer3.converter import PDFPageAggregator
# from pdfminer3.converter import TextConverter
# import io

# resource_manager = PDFResourceManager()
# fake_file_handle = io.StringIO()
# converter = TextConverter(resource_manager, fake_file_handle)
# page_interpreter = PDFPageInterpreter(resource_manager, converter)

# with open(r"C:\Users\Priyanshu Gupta\Desktop\Resume Extractor\priyanshu.pdf", 'rb') as fh:

#     for page in PDFPage.get_pages(fh,
#                                   caching=True,
#                                   check_extractable=True):
#         page_interpreter.process_page(page)

#     text = fake_file_handle.getvalue()

# # close open handles
# converter.close()
# fake_file_handle.close()

# print(text)



# using pdfminer3k
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine

def convert_pdf_to_txt(path):
    fp = open(path, 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument()
    parser.set_document(doc)
    doc.set_parser(parser)
    doc.initialize('')
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    laparams.char_margin = 1.0
    laparams.word_margin = 1.0
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    extracted_text = ''

    for page in doc.get_pages():
        interpreter.process_page(page)
        layout = device.get_result()
        for lt_obj in layout:
            if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                extracted_text += lt_obj.get_text()
    return(extracted_text)
#print(extracted_text)