import pytesseract
from PIL import Image


def run_ocr(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)

    return text
