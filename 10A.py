from PyPDF2 import PdfReader, PdfWriter


def combine_pdfs():
    n = int(input("Enter the number of PDF documents to combine: "))
    pdf_writer = PdfWriter()

    for i in range(1, n + 1):
        pdf_file_name = input(f"Enter the name of PDF file {i}: ")
        page_num = int(input(f"Enter the page number for PDF file {i}: "))

        with open(pdf_file_name, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)

            if 1 <= page_num <= len(pdf_reader.pages):
                page = pdf_reader.pages[page_num - 1]
                pdf_writer.add_page(page)
            else:
                print(f"Page {page_num} does not exist in {pdf_file_name}.")

    output_pdf_name = input("Set the name of the output PDF file: ")

    with open(output_pdf_name, 'wb') as output:
        pdf_writer.write(output)

    print(f"Combined PDF saved as '{output_pdf_name}'")


if __name__ == "__main__":
    combine_pdfs()
