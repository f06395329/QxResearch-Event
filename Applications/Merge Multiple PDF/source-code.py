from PyPDF4 import PdfFileMerger
import os


def merge_pdfs(output='Final_pdf.pdf', source_dir='.'):
  """Merge all PDFs in source_dir into a single output PDF.

  The function will skip the output file if it already exists in the directory
  and will remove source PDFs after merging.
  """
  merger = PdfFileMerger()
  files = [f for f in os.listdir(source_dir) if f.endswith('.pdf')]

  # If there are no PDFs, do nothing
  if not files:
    print('No PDF files found to merge.')
    return

  # Ensure output is not included in the inputs
  files = [f for f in files if f != output]

  if not files:
    print('No PDF files to merge after excluding the output file.')
    return

  # Append files in alphabetical order to make behavior deterministic
  for fname in sorted(files):
    merger.append(os.path.join(source_dir, fname))

  merger.write(os.path.join(source_dir, output))
  merger.close()

  # Remove source files that were merged
  for fname in files:
    try:
      os.remove(os.path.join(source_dir, fname))
    except OSError:
      print(f"Could not remove {fname}; skipping.")


if __name__ == '__main__':
  merge_pdfs()