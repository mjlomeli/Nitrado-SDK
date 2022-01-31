from PIL import Image
import pytesseract
import os


def ocr(image_path):
    """
    Download the Tesseract-OCR and save the executable path in the environment paths
    'C:\Program Files\Tesseract-OCR\tesseract.exe'
    :param image_path: path to the image
    :return: str, the text from an image
    """
    tesseract_exe_path = os.environ.get('TESSERACT')
    pytesseract.pytesseract.tesseract_cmd = tesseract_exe_path
    return pytesseract.image_to_string(Image.open(image_path))


if __name__ == '__main__':
    from pathlib import Path
    for file in Path.cwd().iterdir():
        if file.suffix.lower() in ['.png', '.jpeg']:
            file_name = str(file.name)
            text = ocr(str(file))

            print('\033[93m' + f"Transcribing text from image: {file_name}" + '\033[0m')
            print(text)
            print("\n\n")
