from url_processor import process_url
from pdf_generator import generate_pdf

def main():
    input_user_url = input("Enter the URL: ")
    urls = process_url(input_user_url)
    pdf_name = input("Enter the name for the PDF: ")  # Ask the user for the PDF name
    generate_pdf(urls, pdf_name)  # Pass the PDF name to the generate_pdf function

if __name__ == "__main__":
    main()
