import os
import requests
from PyPDF2 import PdfMerger
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF


def download():
    link = input('Input the direct link to SVG-file. If the previous one was last, leave this space empty\n ~~ ')
    if not link:
        end()
    try:
        open('temp.svg', 'wb').write(requests.get(link).content)
    except requests.exceptions.MissingSchema:
        print('Wrong url!')
        download()
    convert()


def convert():
    drawing = svg2rlg("temp.svg")
    renderPDF.drawToFile(drawing, "temp.pdf")
    merge()


def merge():
    if os.path.exists('file.pdf'):
        merger = PdfMerger()

        os.rename('file.pdf', 'file_.pdf')

        for pdf in ['file_.pdf', 'temp.pdf']:
            merger.append(pdf)

        merger.write('file.pdf')
        merger.close()
        os.remove('file_.pdf')
    else:
        os.rename('temp.pdf', 'file.pdf')
    download()


def end():
    name = input('Input file name\n ~~ ')
    if not os.path.exists('pdf'):
        os.mkdir('pdf')
    try:
        open(f'pdf/{name}.pdf', 'wb').write(open('file.pdf', 'rb').read())
    except OSError:
        print('Wrong file name!')
        end()
    os.remove('temp.svg')
    os.remove('file.pdf')
    try:
        os.remove('temp.pdf')
    except:
        pass
    print('Thx for using!')
    exit()


def main():
    print('|| DO NOT DELETE FILES temp.svg, temp.pdf & file.pdf WHILE THE PROGRAM WORKS!!! ||\n')
    download()


if __name__ == '__main__':
    main()
