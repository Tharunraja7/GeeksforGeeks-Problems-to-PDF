from url_processor import process_url
from pdf_generator import generate_pdf

def main():
    input_user_url = input("Enter the GeeksforGeeks user input URL: ")
    urls = process_url(input_user_url)
    generate_pdf(urls)

if __name__ == "__main__":
    main()
