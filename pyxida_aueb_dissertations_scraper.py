# -*- coding: utf-8 -*-

import urllib.request
import bs4 as bs
import sys


__author__ = 'c.kormaris'

prefix_url = 'http://www.pyxida.aueb.gr/'

department = -1
PhDOrMSc = -1
try:
    department = int(sys.argv[1])
    PhDOrMSc = sys.argv[2]
except IndexError:
    print('Usage: python pyxida_aueb_scraper.py department_number PhDOrMSc')

# department = 1  # Τμήμα Πληροφορικής / Department of Informatics
# department = 2  # Τμήμα Στατιστικής / Department of Statistics
# department = 3  # Τμήμα Οργάνωσης και Διοίκησης Επιχειρήσεων / Department of Business Administration
# department = 4  # Τμήμα Λογιστικής και Χρηματοοικονομικής / Department of Accounting and Finance
# department = 5  # Τμήμα Επικοινωνίας και Μάρκετινγκ / Department of Marketing and Communication
# department = 6  # Τμήμα Διοικητικής Επιστήμης και Τεχνολογίας / Department of Management Science and Technology
# department = 7  # Τμήμα Οικονομικής Επιστήμης / Department of Economics
# department = 8  # Τμήμα Διεθνών και Ευρωπαϊκών Οικονομικών Σπουδών / Department of International and European Economic Studies

# PhDOrMSc = 'phd'
# PhDOrMSc = 'msc'

if department == 1:
    if PhDOrMSc.lower() == 'phd':
        # PhD Theses
        middle_url = 'index.php?op=view_container&object_id=5&pid=3&page='
        links_file = 'di_phd_dissertations_links.txt'
        pdfs_file = 'di_phd_dissertations_filenames.txt'
        authors_file = 'di_phd_dissertations_authors.txt'
        titles_file = 'di_phd_dissertations_titles.txt'
        pages = 1
    else:
        # Postgraduate dissertations
        middle_url = 'index.php?op=view_container&object_id=1890&pid=2&page='
        links_file = 'di_msc_dissertations_links.txt'
        pdfs_file = 'di_msc_dissertations_filenames.txt'
        authors_file = 'di_msc_dissertations_authors.txt'
        titles_file = 'di_msc_dissertations_titles.txt'
        pages = 33
elif department == 2:
    if PhDOrMSc.lower() == 'phd':
        # PhD Theses
        middle_url = 'index.php?op=view_container&object_id=5&pid=26&page'
        links_file = 'ds_phd_dissertations_links.txt'
        pdfs_file = 'ds_phd_dissertations_filenames.txt'
        authors_file = 'ds_phd_dissertations_authors.txt'
        titles_file = 'ds_phd_dissertations_titles.txt'
        pages = 1
    else:
        # Postgraduate dissertations
        middle_url = 'index.php?op=view_container&object_id=4&pid=26&page='
        links_file = 'ds_msc_dissertations_links.txt'
        pdfs_file = 'ds_msc_dissertations_filenames.txt'
        authors_file = 'ds_msc_dissertations_authors.txt'
        titles_file = 'ds_msc_dissertations_titles.txt'
        pages = 32
elif department == 3:
    if PhDOrMSc.lower() == 'phd':
        # PhD Theses
        middle_url = 'index.php?op=view_container&object_id=5&pid=21&page='
        links_file = 'dba_phd_dissertations_links.txt'
        pdfs_file = 'dba_phd_dissertations_filenames.txt'
        authors_file = 'dba_phd_dissertations_authors.txt'
        titles_file = 'dba_phd_dissertations_titles.txt'
        pages = 1
    else:
        # Postgraduate dissertations
        middle_url = 'index.php?op=view_container&object_id=4&pid=21&page='
        links_file = 'dba_msc_dissertations_links.txt'
        pdfs_file = 'dba_msc_dissertations_filenames.txt'
        authors_file = 'dba_msc_dissertations_authors.txt'
        titles_file = 'dba_msc_dissertations_titles.txt'
        pages = 15
elif department == 4:
    if PhDOrMSc.lower() == 'phd':
        # PhD Theses
        middle_url = 'index.php?op=view_container&object_id=5&pid=23&page='
        links_file = 'daf_phd_dissertations_links.txt'
        pdfs_file = 'daf_phd_dissertations_filenames.txt'
        authors_file = 'daf_phd_dissertations_authors.txt'
        titles_file = 'daf_phd_dissertations_titles.txt'
        pages = 1
    else:
        # Postgraduate dissertations
        middle_url = 'index.php?op=view_container&object_id=4&pid=23&page='
        links_file = 'daf_msc_dissertations_links.txt'
        pdfs_file = 'daf_msc_dissertations_filenames.txt'
        authors_file = 'daf_msc_dissertations_authors.txt'
        titles_file = 'daf_msc_dissertations_titles.txt'
        pages = 17
elif department == 5:
    if PhDOrMSc.lower() == 'phd':
        # PhD Theses
        middle_url = 'index.php?op=view_container&object_id=5&pid=24&page='
        links_file = 'dmc_phd_dissertations_links.txt'
        pdfs_file = 'dmc_phd_dissertations_filenames.txt'
        authors_file = 'dmc_phd_dissertations_authors.txt'
        titles_file = 'dmc_phd_dissertations_titles.txt'
        pages = 1
    else:
        # Postgraduate dissertations
        middle_url = 'index.php?op=view_container&object_id=4&pid=24&page='
        links_file = 'dmc_msc_dissertations_links.txt'
        pdfs_file = 'dmc_msc_dissertations_filenames.txt'
        authors_file = 'dmc_msc_dissertations_authors.txt'
        titles_file = 'dmc_msc_dissertations_titles.txt'
        pages = 15
elif department == 6:
    if PhDOrMSc.lower() == 'phd':
        # PhD Theses
        middle_url = 'index.php?op=view_container&object_id=5&pid=25&page='
        links_file = 'dmst_phd_dissertations_links.txt'
        pdfs_file = 'dmst_phd_dissertations_filenames.txt'
        authors_file = 'dmst_phd_dissertations_authors.txt'
        titles_file = 'dmst_phd_dissertations_titles.txt'
        pages = 1
    else:
        # Postgraduate dissertations
        middle_url = 'index.php?op=view_container&object_id=4&pid=25&page='
        links_file = 'dmst_msc_dissertations_links.txt'
        pdfs_file = 'dmst_msc_dissertations_filenames.txt'
        authors_file = 'dmst_msc_dissertations_authors.txt'
        titles_file = 'dmst_msc_dissertations_titles.txt'
        pages = 3
elif department == 7:
    if PhDOrMSc.lower() == 'phd':
        # PhD Theses
        middle_url = 'index.php?op=view_container&object_id=5&pid=3&page='
        links_file = 'de_phd_dissertations_links.txt'
        pdfs_file = 'de_phd_dissertations_filenames.txt'
        authors_file = 'de_phd_dissertations_authors.txt'
        titles_file = 'de_phd_dissertations_titles.txt'
        pages = 2
    else:
        # Postgraduate dissertations
        middle_url = 'index.php?op=view_container&object_id=5&pid=20&page='
        links_file = 'de_msc_dissertations_links.txt'
        pdfs_file = 'de_msc_dissertations_filenames.txt'
        authors_file = 'de_msc_dissertations_authors.txt'
        titles_file = 'de_msc_dissertations_titles.txt'
        pages = 39
else:
    if PhDOrMSc.lower() == 'phd':
        # PhD Theses
        middle_url = 'index.php?op=view_container&object_id=5&pid=22&page='
        links_file = 'diees_phd_dissertations_links.txt'
        pdfs_file = 'diees_phd_dissertations_filenames.txt'
        authors_file = 'diees_phd_dissertations_authors.txt'
        titles_file = 'diees_phd_dissertations_titles.txt'
        pages = 1
    else:
        # Postgraduate dissertations
        middle_url = 'index.php?op=view_container&object_id=4&pid=22&page='
        links_file = 'diees_msc_dissertations_links.txt'
        pdfs_file = 'diees_msc_dissertations_filenames.txt'
        authors_file = 'diees_msc_dissertations_authors.txt'
        titles_file = 'diees_msc_dissertations_titles.txt'
        pages = 20


thesis_links = []

for i in range(1, pages + 1):

    current_url = prefix_url + middle_url + str(i)
    source = urllib.request.urlopen(current_url).read()
    soup = bs.BeautifulSoup(source, 'lxml')

    for url in (soup.find_all('a')):
        if 'page' not in url.get('href') and \
                'javascript' not in url.get('href') and \
                'lang' not in url.get('href'):
            if 'http' in url.get('href'):
                thesis_links.append(url.get('href'))
                # print(url.get('href'))
            else:
                thesis_links.append(prefix_url + url.get('href'))
                # print(prefix + url.get('href'))


pdf_links = []
authors = []
titles = []
pdf_filenames = []

for link in thesis_links:
    source = urllib.request.urlopen(link).read()
    soup = bs.BeautifulSoup(source, 'lxml')

    # divs = soup.find_all('div')
    # details = divs[10]

    # get the title
    table = soup.find_all('table', {'class': 'view-object-table'})[1]
    table_rows = table.find_all('tr')
    for tr in table_rows:
        td = tr.find_all('td', {'valign': 'top'})
        row = [i.text for i in td]
        titles.append(row[0])
        print(row[0])

    # get the author name
    table = soup.find_all('table', {'class': 'view-object-table'})[2]
    if 'δημιουργός' not in str(table).lower():
        table = soup.find_all('table', {'class': 'view-object-table'})[3]
    table_rows = table.find_all('tr')
    for tr in table_rows:
        td = tr.find_all('td', {'valign': 'top'})
        row = [i.text for i in td]
        authors.append(row[0])
        print(row[0])

    # get the ".pdf" link
    for url in (soup.find_all('a')):
        if 'pdf' in url.get('href').lower():
            pdf_links.append(prefix_url + url.get('href'))
            print(prefix_url + url.get('href'))

            pdf_filenames.append(url.contents[0])


print('')
print('Writing to file...')
# write list of ".pdf" links to file
file = open(links_file, 'w')
for pdf_link in pdf_links:
    file.write("%s\n" % pdf_link)
file.close()

# write list of ".pdf" filenames to file
file = open(pdfs_file, 'w')
for pdf_filename in pdf_filenames:
    file.write("%s\n" % pdf_filename)
file.close()

# write list of titles to file
file = open(titles_file, 'w')
for title in titles:
    file.write("%s\n" % title)
file.close()

# write list of author names to file
file = open(authors_file, 'w')
for author in authors:
    file.write("%s\n" % author)
file.close()
print('DONE')

