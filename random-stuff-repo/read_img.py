# NOT WORKING 
# import cv2
# import pytesseract
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# img = cv2.imread('breakingnews.png')
# text = pytesseract.image_to_string(img)
# print(text)


# WORKING NICE NICE
import pyautogui
from PIL import Image
from pytesseract import *
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = Image.open(r"C:\Users\Wetooa\Documents\Educational\Grade 12\Comsci\PYTHON\random stuff\testingIMG.png")
output = pytesseract.image_to_string(img)
print(output)