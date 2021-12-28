
import pytesseract
import os
import argparse
imgpath = "img/testcapt.png"
tesseract = pytesseract.pytesseract.tesseract_cmd
try:
    import Image, ImageOps, ImageEnhance, imread
except ImportError:
    from PIL import Image, ImageOps, ImageEnhance

def solve_captcha(path):
    image = Image.open(path).convert('RGB')
    image = ImageOps.autocontrast(image)

    filename = "{}.png".format(os.getpid())
    image.save(filename)

    text = pytesseract.image_to_string(Image.open(filename), config='digits')
    return text

def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-i", "--image", required=True, help=imgpath)
    args = vars(argparser.parse_args())
    path = args['image']
    captcha_text = solve_captcha(path)
    print(captcha_text)

main()