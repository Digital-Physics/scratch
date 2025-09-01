# To use this script, you first need to install the pypdf library.
# You can do this by running the following command in your terminal:
# pip install pypdf

import pypdf

def extract_pages_to_pdf(input_pdf_path, output_pdf_path, start_page, end_page):
    """
    Extracts a page range from a source PDF and saves it to a new PDF file
    using the pypdf library.

    Args:
        input_pdf_path (str): The path to the source PDF file.
        output_pdf_path (str): The path to the new PDF file to be created.
        start_page (int): The starting page number of the range (1-indexed).
        end_page (int): The ending page number of the range (1-indexed).
    """
    try:
        # Open the original PDF file in binary read mode
        with open(input_pdf_path, 'rb') as input_file:
            # Create a PdfReader object to read the input PDF
            reader = pypdf.PdfReader(input_file)
            writer = pypdf.PdfWriter()

            # Check if the page numbers are valid
            total_pages = len(reader.pages)
            if start_page < 1 or end_page > total_pages or start_page > end_page:
                print(f"Error: Invalid page range. The document has {total_pages} pages.")
                return

            # pypdf uses 0-based indexing for pages
            start_index = start_page - 1
            end_index = end_page

            # Iterate through the pages in the specified range and add them to the writer
            for page_num in range(start_index, end_index):
                writer.add_page(reader.pages[page_num])

            # Open the output file in binary write mode
            with open(output_pdf_path, 'wb') as output_file:
                writer.write(output_file)

            print(f"Successfully created '{output_pdf_path}' with pages {start_page} to {end_page}.")

    except FileNotFoundError:
        print(f"Error: The file '{input_pdf_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # --- Example Usage ---
    # You will need to replace 'input.pdf' with the path to your source PDF
    # and adjust the start and end page numbers as needed.

    # Example 1: Extract pages 95 to 100 from 'turing.pdf'
    input_file = "turing.pdf"
    output_file = "sqrt_two_turing.pdf"
    start = 115
    end = 122
    extract_pages_to_pdf(input_file, output_file, start, end)