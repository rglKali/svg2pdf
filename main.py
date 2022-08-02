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
    name = input('Введите название файла\n ~~ ')
    open(f'pdf/{name}.pdf', 'wb').write(open('file.pdf', 'rb').read())
    os.remove('file.pdf')
    os.remove('temp.pdf')
    os.remove('temp.svg')
    print('Thx for using!')
    exit()


def main():
    print('|| Не удаляйте файлы temp.svg, temp.pdf и file.pdf во время работы программы!!! ||\n')
    download()


if __name__ == '__main__':
    main()
