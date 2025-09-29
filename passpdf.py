"""Small utility to create an encrypted copy of a PDF file.

This module exposes a simple `protect_pdf()` function that prompts the user
for a filename and password and writes an encrypted `secured.pdf`.
"""

from PyPDF2 import PdfFileWriter, PdfFileReader
import getpass


def protect_pdf():
    """Create an encrypted copy of a PDF named 'secured.pdf'."""
    # Making an instance of the PdfFileWriter class and storing it in a variable
    writer = PdfFileWriter()

    # Explicitly ask the user what the name of the original file is
    pdf_name = input('Please type the name of the pdf file (including extension): ').strip()
    if not pdf_name:
        print('No filename provided — aborting.')
        return

    # Making an instance of the PdfFileReader class with the original file as an argument
    original_file = PdfFileReader(pdf_name)

    # Copies the content of the original file to the writer variable
    for page in range(original_file.numPages):
        writer.addPage(original_file.getPage(page))

    # Retrieve a preferred password from the user
    password = getpass.getpass(prompt="Set a Password: ")

    # Encrypt the copy of the original file
    writer.encrypt(password)

    # Opens a new pdf (write binary permission) and writes the content of the 'writer' into it
    with open('secured.pdf', 'wb') as f:
        writer.write(f)


if __name__ == '__main__':
    protect_pdf()
