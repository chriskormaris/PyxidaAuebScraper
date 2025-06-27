import os

import requests

from src.constants import *


def pyxida_downloader(department=1, phd_or_msc='phd'):
    if department == 1:  # Τμήμα Πληροφορικής / Department of Informatics
        directory = 'di'
    elif department == 2:  # Τμήμα Στατιστικής / Department of Statistics
        directory = 'ds'
    elif department == 3:  # Τμήμα Οργάνωσης και Διοίκησης Επιχειρήσεων / Department of Business Administration
        directory = 'dba'
    elif department == 4:  # Τμήμα Λογιστικής και Χρηματοοικονομικής / Department of Accounting and Finance
        directory = 'daf'
    elif department == 5:  # Τμήμα Επικοινωνίας και Μάρκετινγκ / Department of Marketing and Communication
        directory = 'dmc'
    elif department == 6:  # Τμήμα Διοικητικής Επιστήμης και Τεχνολογίας / Department of Management Science and Technology
        directory = 'dmst'
    elif department == 7:  # Τμήμα Οικονομικής Επιστήμης / Department of Economics
        directory = 'diees'
    # Τμήμα Διεθνών και Ευρωπαϊκών Οικονομικών Σπουδών / Department of International and European Economic Studies
    else:
        directory = 'de'

    if phd_or_msc.lower() == 'phd':  # PhD Dissertations
        directory += '_phd'
    else:  # Postgraduate Dissertations
        directory += '_msc'
    directory += '_dissertations\\'

    if not os.path.exists(pdfs_path):
        os.mkdir(pdfs_path)

    if not os.path.exists(pdfs_path + directory):
        os.mkdir(pdfs_path + directory)

    pdf_links_file = directory + 'links.txt'
    file = open(txt_path + pdf_links_file, 'r')
    pdf_links = file.read().splitlines()
    file.close()

    pdf_names_file = directory + 'filenames.txt'
    file = open(txt_path + pdf_names_file, 'r')
    pdf_filenames = file.read().splitlines()
    file.close()

    for i, pdf_link in enumerate(pdf_links):
        if pdf_link != '':
            response = requests.get(pdf_link)
            filename = pdfs_path + directory + pdf_filenames[i]
            open(filename, 'wb').write(response.content)
            print(pdf_filenames[i])

    print('[DONE]')
    print()


if __name__ == '__main__':
    pyxida_downloader(department=1, phd_or_msc='phd')
