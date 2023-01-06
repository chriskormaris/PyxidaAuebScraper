import os

import requests

from src.constants import *


# department = 1  # Τμήμα Πληροφορικής / Department of Informatics
# department = 2  # Τμήμα Στατιστικής / Department of Statistics
# department = 3  # Τμήμα Οργάνωσης και Διοίκησης Επιχειρήσεων / Department of Business Administration
# department = 4  # Τμήμα Λογιστικής και Χρηματοοικονομικής / Department of Accounting and Finance
# department = 5  # Τμήμα Επικοινωνίας και Μάρκετινγκ / Department of Marketing and Communication
# department = 6  # Τμήμα Διοικητικής Επιστήμης και Τεχνολογίας / Department of Management Science and Technology
# department = 7  # Τμήμα Οικονομικής Επιστήμης / Department of Economics
# department = 8  # Τμήμα Διεθνών και Ευρωπαϊκών Οικονομικών Σπουδών /
#                   Department of International and European Economic Studies

# PhDOrMSc = 'phd'
# PhDOrMSc = 'msc'
def pyxida_downloader(department=1, phd_or_msc='phd'):
    if department == 1:
        if phd_or_msc.lower() == 'phd':
            name = 'di_phd_dissertations'
        else:
            name = 'di_msc_dissertations'
    elif department == 2:
        if phd_or_msc.lower() == 'phd':
            name = 'ds_phd_dissertations'
        else:
            name = 'ds_msc_dissertations'
    elif department == 3:
        if phd_or_msc.lower() == 'phd':
            name = 'dba_phd_dissertations'
        else:
            name = 'dba_msc_dissertations'
    elif department == 4:
        if phd_or_msc.lower() == 'phd':
            name = 'daf_phd_dissertations'
        else:
            name = 'daf_msc_dissertations'
    elif department == 5:
        if phd_or_msc.lower() == 'phd':
            name = 'dmc_phd_dissertations'
        else:
            name = 'dmc_msc_dissertations'
    elif department == 6:
        if phd_or_msc.lower() == 'phd':
            name = 'dmst_phd_dissertations'
        else:
            name = 'dmst_msc_dissertations'
    elif department == 7:
        if phd_or_msc.lower() == 'phd':
            name = 'de_phd_dissertations'
        else:
            name = 'de_msc_dissertations'
    else:
        if phd_or_msc.lower() == 'phd':
            name = 'diees_phd_dissertations'
        else:
            name = 'diees_msc_dissertations'

    if not os.path.exists(output_path + name):
        os.mkdir(output_path + name)

    pdf_links_file = name + '_links.txt'
    file = open(txt_path + pdf_links_file, 'r')
    pdf_links = file.read().splitlines()
    file.close()

    pdf_names_file = name + '_filenames.txt'
    file = open(txt_path + pdf_names_file, 'r')
    pdf_filenames = file.read().splitlines()
    file.close()

    for i, pdf_link in enumerate(pdf_links):
        # id = pdf_link.split('iid:')[1].split('&')[0]
        response = requests.get(pdf_link)
        filename = output_path + name + '/' + pdf_filenames[i]
        open(filename, "wb").write(response.content)
        print(pdf_filenames[i])

    print('[DONE]')


if __name__ == '__main__':
    pyxida_downloader(department=1, phd_or_msc='phd')
