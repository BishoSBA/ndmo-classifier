import glob
import os
import sys

import pytesseract
from pdf2image import convert_from_bytes
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
    text = ''
    pages = convert_from_bytes(PDF_file.stream.read())
    file_name = PDF_file.filename.split('/')[-1]
    for pageNum, imgBlob in enumerate(pages):
        filename = file_name + '_page' + str(pageNum) + '.jpg'
        print('saving ' + file_name)
        # Save the image of the page in system
        imgBlob.save(filename, 'JPEG')

        text = text + pytesseract.image_to_string(filename, lang='eng+ara', config=f'--psm 3')

    return (text)

def classify_file(file):
    current_working_directory = os.getcwd()
    os.environ["TESSDATA_PREFIX"] = f'{current_working_directory}/lang/'

    text = pdf2txt(file)
    classification = get_classification(text)
    # move_file_by_classification(classification, args[0])
    return classification


# def main(args=None):
#     current_working_directory = os.getcwd()
#     os.environ["TESSDATA_PREFIX"] = f'{current_working_directory}/lang/'

#     text = pdf2txt(args[0])
#     classification = get_classification(text)
#     # move_file_by_classification(classification, args[0])
#     return classification

# if __name__ == "__main__":
#     main(sys.argv[1:])