import os

import requests

from src.constants import *


def pyxida_downloader(department=1, phd_or_msc='phd', pdfs_path=pdfs_path, txt_path=txt_path):
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
    directory += '_dissertations'

    if not os.path.exists(pdfs_path):
        os.mkdir(pdfs_path)

    if not os.path.exists(os.path.join(pdfs_path, directory)):
        os.mkdir(os.path.join(pdfs_path, directory))

    pdf_links_file_path = os.path.join(directory, 'links.txt')
    pdf_links_file = open(os.path.join(txt_path, pdf_links_file_path), 'r')
    pdf_links = pdf_links_file.read().splitlines()
    pdf_links_file.close()

    pdf_names_file_path = os.path.join(directory, 'filenames.txt')
    pdf_names_file = open(os.path.join(txt_path, pdf_names_file_path), 'r')
    pdf_filenames = pdf_names_file.read().splitlines()
    pdf_names_file.close()

    for i, pdf_link in enumerate(pdf_links):
        if pdf_link != '':
            response = requests.get(pdf_link)
            filename = os.path.join(pdfs_path, directory, pdf_filenames[i])
            open(filename, 'wb').write(response.content)
            print(pdf_filenames[i])

    print('[DONE]')
    print()


if __name__ == '__main__':
    pyxida_downloader(
        department=1,
        phd_or_msc='phd',
        pdfs_path=os.path.join('..', pdfs_path),
        txt_path=os.path.join('..', txt_path)
    )
