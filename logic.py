import glob
import os
import sys

import pytesseract
from pdf2image import convert_from_path
from api import get_classification

# Path of the pdf
tesseract_loc = r"/opt/homebrew/bin/tesseract"
poppler_path = r"/opt/homebrew/Cellar/poppler/24.04.0/bin"

def move_file_by_classification(classification, file_path):
    # Move the file to the respective folder based on the classification
    return

# Recognizing text from the images using OCR
def pdf2txt(PDF_file):
    pytesseract.pytesseract.tesseract_cmd = tesseract_loc
    PDF_file = PDF_file
    pdfs = glob.glob(PDF_file)
    text = ''
    for pdf_path in pdfs:
        pages = convert_from_path(pdf_path, poppler_path=poppler_path)
        for pageNum, imgBlob in enumerate(pages):
            filename = pdf_path[:-4] + '_page' + str(pageNum) + '.jpg'
            print('saving ' + filename)
            # Save the image of the page in system
            imgBlob.save(filename, 'JPEG')

            text = text + pytesseract.image_to_string(filename, lang='eng+ara', config=f'--psm 3')

        # text = text.replace('\n', ' ')
        f = open("playground.txt", "w")
        f.write(text)
        f.close()

    return (text)

def main(args=None):
    current_working_directory = os.getcwd()
    os.environ["TESSDATA_PREFIX"] = f'{current_working_directory}/lang/'

    text = pdf2txt(args[0])
    classification = get_classification(text)
    # move_file_by_classification(classification, args[0])
    return classification

if __name__ == "__main__":
    main(sys.argv[1:])