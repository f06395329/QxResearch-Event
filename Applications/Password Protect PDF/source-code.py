from PyPDF2 import PdfWriter, PdfReader
import getpass


def protect_pdf(input_path='1.pdf', output_path='ho.pdf'):
    pdfwriter = PdfWriter()
    pdf = PdfReader(input_path)
    for page_num in range(len(pdf.pages)):
        pdfwriter.add_page(pdf.pages[page_num])
    passw = getpass.getpass(prompt='Enter Password: ')
    pdfwriter.encrypt(passw)
    with open(output_path, 'wb') as f:
        pdfwriter.write(f)


if __name__ == '__main__':
    protect_pdf()