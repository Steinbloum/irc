#!/usr/bin/python3
# coding: utf-8

import pytesseract
import os
import argparse
from PIL import Image, ImageOps, ImageEnhance
from htmlextractor import Htmlator
 

# imgpath = 'img/testcapt.png'
tesseract = pytesseract.pytesseract.tesseract_cmd
h = Htmlator()

# def solve_captcha(path):
 
#     """
#     Convert a captcha image into a text, 
#     using PyTesseract Python-wrapper for Tesseract
#     Arguments:
#         path (str):
#             path to the image to be processed
#     Return:
#         'textualized' image
#     """
#     image = Image.open(path).convert('RGB')
#     image = ImageOps.autocontrast(image)
    
#     filename = "{}.png".format(os.getpid())
#     image.save(filename)
 
#     text = pytesseract.image_to_string(Image.open(filename))
#     return text
 
 
# if __name__ == '__main__':
#     argparser = argparse.ArgumentParser()
#     argparser.add_argument("-i", "--image", required=True, help="img/testcapt.png")
#     args = vars(argparser.parse_args())
#     path = args["image"]
#     print('-- Resolving')
#     captcha_text = solve_captcha(path)
#     print('-- Result: {}'.format(captcha_text))
raw = h.extract_html('http://challenge01.root-me.org/programmation/ch8/')
idx = raw.find('<img src="')
start_index = idx + len('<img src="')
end_index = raw.find('" /><br><br><')
result = raw[start_index:end_index]
imgpath = h.save_img_from_url(result, 'img/captcha.png')

text = pytesseract.image_to_string(Image.open(imgpath))
print (text)