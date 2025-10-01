"""Small utility to create an encrypted copy of a PDF file.

This module exposes a simple `protect_pdf()` function that prompts the user
for a filename and password and writes an encrypted `secured.pdf`.
"""

from PyPDF2 import PdfFileWriter, PdfFileReader
import os
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
    if not os.path.isfile(pdf_name):
        print(f"File not found: {pdf_name}")
        return

    # Making an instance of the PdfFileReader class with the original file as an argument
    try:
        original_file = PdfFileReader(pdf_name)
    except Exception as e:
        print(f"Failed to open PDF: {e}")
        return

    # Copies the content of the original file to the writer variable
    for page in range(original_file.numPages):
        writer.addPage(original_file.getPage(page))

    # Retrieve a preferred password from the user
    password = getpass.getpass(prompt="Set a Password: ")
    if not password:
        print('No password provided — aborting.')
        return

    # Encrypt the copy of the original file
    writer.encrypt(password)

    # Determine a safe output filename and write the encrypted PDF
    output_name = 'secured.pdf'
    if os.path.exists(output_name):
        base, ext = os.path.splitext(output_name)
        counter = 1
        while os.path.exists(f"{base}({counter}){ext}"):
            counter += 1
        output_name = f"{base}({counter}){ext}"

    with open(output_name, 'wb') as f:
        writer.write(f)
    print(f"Encrypted PDF written to: {output_name}")


if __name__ == '__main__':
    protect_pdf()
