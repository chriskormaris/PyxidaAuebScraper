import urllib.request
import os


department = 1  # Τμήμα Πληροφορικής / Department of Informatics
# department = 2  # Τμήμα Στατιστικής / Department of Statistics (652)
# department = 3  # Τμήμα Οργάνωσης και Διοίκησης Επιχειρήσεων / Department of Business Administration
# department = 4  # Τμήμα Λογιστικής και Χρηματοοικονομικής / Department of Accounting and Finance
# department = 5  # Τμήμα Επικοινωνίας και Μάρκετινγκ / Department of Marketing and Communication
# department = 6  # Τμήμα Διοικητικής Επιστήμης και Τεχνολογίας / Department of Management Science and Technology
# department = 7  # Τμήμα Οικονομικής Επιστήμης / Department of Economics
# department = 8  # Τμήμα Διεθνών και Ευρωπαϊκών Οικονομικών Σπουδών / Department of International and European Economic Studies

PhDOrMSc = 'phd'
# PhDOrMSc = 'msc'

if department == 1:
    if PhDOrMSc.lower() == 'phd':
        name = 'di_phd_theses'
    else:
        name = 'di_msc_theses'
elif department == 2:
    if PhDOrMSc.lower() == 'phd':
        name = 'ds_phd_theses'
    else:
        name = 'ds_msc_theses'
elif department == 3:
    if PhDOrMSc.lower() == 'phd':
        name = 'dba_phd_theses'
    else:
        name = 'dba_msc_theses'
elif department == 4:
    if PhDOrMSc.lower() == 'phd':
        name = 'daf_phd_theses'
    else:
        name = 'daf_msc_theses'
elif department == 5:
    if PhDOrMSc.lower() == 'phd':
        name = 'dmc_phd_theses'
    else:
        name = 'dmc_msc_theses'
elif department == 6:
    if PhDOrMSc.lower() == 'phd':
        name = 'dmst_phd_theses'
    else:
        name = 'dmst_msc_theses'
elif department == 7:
    if PhDOrMSc.lower() == 'phd':
        name = 'de_phd_theses'
    else:
        name = 'de_msc_theses'
else:
    if PhDOrMSc.lower() == 'phd':
        name = 'diees_phd_theses'
    else:
        name = 'diees_msc_theses'

if not os.path.exists(name):
    os.mkdir(name)

filename = name + '_links.txt'
file = open(filename, 'r')
pdf_links = file.read().splitlines()
file.close()

pdfnames_file = name + '_filenames.txt'
file = open(pdfnames_file, 'r')
pdf_filenames = file.read().splitlines()
file.close()

for i, pdf_link in enumerate(pdf_links):
    # id = pdf_link.split('iid:')[1].split('&')[0]
    urllib.request.urlretrieve(pdf_link, filename=name + '/' + pdf_filenames[i])
    print(pdf_filenames[i])
