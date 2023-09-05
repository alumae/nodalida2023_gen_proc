import os
import sys
import json
#from dotenv import load_dotenv
import time
import openai

from PyPDF2 import PdfFileReader
import backoff

# Load environment variables from .env file
#load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')


# Function to extract text from the first page of a PDF file
def extract_first_page_text(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf = PdfFileReader(file)
        first_page = pdf.getPage(0)
        text = first_page.extractText()
        if "Abstract\n" in text:
          text = text[: text.index("Abstract\n")]
        #breakpoint()
        return text
        
# Function to get the country of the institution using OpenAI ChatGPT API
@backoff.on_exception(backoff.expo, openai.error.RateLimitError)
def get_institution_country(text):
    
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {'role': 'system', 'content': 'You are a researcher trying to determine the country of the institution of the authors based on the extracted text from the first page of a PDF file. If several institutions or countries are mentioned, respond with a comma-seperated list of all countries mentioned, without any final punctuation mark. Respond with an empty string, if you cannot infer the country.' },
            {'role': 'user', 'content': f'Text: {text}\nCountry:'}
        ]
    )    
    #breakpoint()
    country = completion.choices[0]["message"]["content"].strip()


    return country


# Function to process the PDF files in a directory
def process_pdf_files(directory):
    results = {}

    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            file_path = os.path.join(directory, filename)
            text = extract_first_page_text(file_path)
            country = get_institution_country(text)
            print(file_path, country)
            time.sleep(1)
            results[filename] = country

    return results


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please provide the PDF directory as a command-line argument.')
        sys.exit(1)

    pdf_directory = sys.argv[1]

    if not os.path.isdir(pdf_directory):
        print('Invalid PDF directory.')
        sys.exit(1)

    # Process PDF files and save results to a JSON file
    results = process_pdf_files(pdf_directory)

    output_file = 'output.json'

    with open(output_file, 'w') as f:
        json.dump(results, f, indent=4)

    print('Extraction and analysis complete. Results saved to', output_file)
