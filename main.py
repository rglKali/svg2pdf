import os
import requests
from PyPDF2 import PdfMerger
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF


def download():
    link = input('Введите ссылку на svg-файл. Если предыдущий файл был последним, оставьте поле пустым\n ~~ ')
    if not link:
        end()
    open('temp.svg', 'wb').write(requests.get(link).content)
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
    os.remove('temp.pdf')
    os.remove('temp.svg')
    name = input('Введите название файла\n ~~ ')
    os.rename('file.pdf', f'{name}.pdf')
    print('Thx for using!')
    exit()


def main():
    download()


if __name__ == '__main__':
    main()