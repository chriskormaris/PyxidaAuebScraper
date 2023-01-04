import os

import bs4 as bs
import requests

base_url = 'http://www.pyxida.aueb.gr/'
txt_path = 'txt\\'


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
def pyxida_scraper(department=1, phd_or_msc='phd'):
    links_file_postfix = '_dissertations_links.txt'
    pdfs_file_postfix = '_dissertations_filenames.txt'
    authors_file_postfix = '_dissertations_authors.txt'
    titles_file_postfix = '_dissertations_titles.txt'

    if department == 1:
        if phd_or_msc.lower() == 'phd':
            # PhD Dissertations
            middle_url = 'index.php?op=view_container&object_id=5&pid=3&page='
            pages = 1
        else:
            # Postgraduate Dissertations
            middle_url = 'index.php?op=view_container&object_id=1890&pid=2&page='
            pages = 33
        links_file = 'di_' + phd_or_msc.lower() + links_file_postfix
        pdfs_file = 'di_' + phd_or_msc.lower() + pdfs_file_postfix
        authors_file = 'di_' + phd_or_msc.lower() + authors_file_postfix
        titles_file = 'di_' + phd_or_msc.lower() + titles_file_postfix
    elif department == 2:
        if phd_or_msc.lower() == 'phd':
            # PhD Dissertations
            middle_url = 'index.php?op=view_container&object_id=5&pid=26&page'
            pages = 1
        else:
            # Postgraduate Dissertations
            middle_url = 'index.php?op=view_container&object_id=4&pid=26&page='
            pages = 32
        links_file = 'ds_' + phd_or_msc.lower() + links_file_postfix
        pdfs_file = 'ds_' + phd_or_msc.lower() + pdfs_file_postfix
        authors_file = 'ds_' + phd_or_msc.lower() + authors_file_postfix
        titles_file = 'ds_' + phd_or_msc.lower() + titles_file_postfix
    elif department == 3:
        if phd_or_msc.lower() == 'phd':
            # PhD Dissertations
            middle_url = 'index.php?op=view_container&object_id=5&pid=21&page='
            pages = 1
        else:
            # Postgraduate Dissertations
            middle_url = 'index.php?op=view_container&object_id=4&pid=21&page='
            pages = 15
        links_file = 'dba_' + phd_or_msc.lower() + links_file_postfix
        pdfs_file = 'dba_' + phd_or_msc.lower() + pdfs_file_postfix
        authors_file = 'dba_' + phd_or_msc.lower() + authors_file_postfix
        titles_file = 'dba_' + phd_or_msc.lower() + titles_file_postfix
    elif department == 4:
        if phd_or_msc.lower() == 'phd':
            # PhD Dissertations
            middle_url = 'index.php?op=view_container&object_id=5&pid=23&page='
            pages = 1
        else:
            # Postgraduate Dissertations
            middle_url = 'index.php?op=view_container&object_id=4&pid=23&page='
            pages = 17
        links_file = 'daf_' + phd_or_msc.lower() + links_file_postfix
        pdfs_file = 'daf_' + phd_or_msc.lower() + pdfs_file_postfix
        authors_file = 'daf_' + phd_or_msc.lower() + authors_file_postfix
        titles_file = 'daf_' + phd_or_msc.lower() + titles_file_postfix
    elif department == 5:
        if phd_or_msc.lower() == 'phd':
            # PhD Dissertations
            middle_url = 'index.php?op=view_container&object_id=5&pid=24&page='
            pages = 1
        else:
            # Postgraduate Dissertations
            middle_url = 'index.php?op=view_container&object_id=4&pid=24&page='
            pages = 15
        links_file = 'dmc_' + phd_or_msc.lower() + links_file_postfix
        pdfs_file = 'dmc_' + phd_or_msc.lower() + pdfs_file_postfix
        authors_file = 'dmc_' + phd_or_msc.lower() + authors_file_postfix
        titles_file = 'dmc_' + phd_or_msc.lower() + titles_file_postfix
    elif department == 6:
        if phd_or_msc.lower() == 'phd':
            # PhD Dissertations
            middle_url = 'index.php?op=view_container&object_id=5&pid=25&page='
            pages = 1
        else:
            # Postgraduate Dissertations
            middle_url = 'index.php?op=view_container&object_id=4&pid=25&page='
            pages = 3
        links_file = 'dmst_' + phd_or_msc.lower() + links_file_postfix
        pdfs_file = 'dmst_' + phd_or_msc.lower() + pdfs_file_postfix
        authors_file = 'dmst_' + phd_or_msc.lower() + authors_file_postfix
        titles_file = 'dmst_' + phd_or_msc.lower() + titles_file_postfix
    elif department == 7:
        if phd_or_msc.lower() == 'phd':
            # PhD Dissertations
            middle_url = 'index.php?op=view_container&object_id=5&pid=3&page='
            pages = 2
        else:
            # Postgraduate Dissertations
            middle_url = 'index.php?op=view_container&object_id=5&pid=20&page='
            pages = 39
        links_file = 'de_' + phd_or_msc.lower() + links_file_postfix
        pdfs_file = 'de_' + phd_or_msc.lower() + pdfs_file_postfix
        authors_file = 'de_' + phd_or_msc.lower() + authors_file_postfix
        titles_file = 'de_' + phd_or_msc.lower() + titles_file_postfix
    else:
        if phd_or_msc.lower() == 'phd':
            # PhD Dissertations
            middle_url = 'index.php?op=view_container&object_id=5&pid=22&page='
            pages = 1
        else:
            # Postgraduate Dissertations
            middle_url = 'index.php?op=view_container&object_id=4&pid=22&page='
            pages = 20
        links_file = 'diees_' + phd_or_msc.lower() + links_file_postfix
        pdfs_file = 'diees_' + phd_or_msc.lower() + pdfs_file_postfix
        authors_file = 'diees_' + phd_or_msc.lower() + authors_file_postfix
        titles_file = 'diees_' + phd_or_msc.lower() + titles_file_postfix


    thesis_links = []

    for i in range(1, pages + 1):

        current_url = base_url + middle_url + str(i)
        source = requests.get(current_url).text
        soup = bs.BeautifulSoup(source, 'lxml')

        for url in (soup.find_all('a')):
            if 'page' not in url.get('href') and \
                    'javascript' not in url.get('href') and \
                    'lang' not in url.get('href'):
                if 'http' in url.get('href'):
                    thesis_links.append(url.get('href'))
                    # print(url.get('href'))
                else:
                    thesis_links.append(base_url + url.get('href'))
                    # print(prefix + url.get('href'))


    pdf_links = []
    authors = []
    titles = []
    pdf_filenames = []

    for link in thesis_links:
        source = requests.get(link).text
        soup = bs.BeautifulSoup(source, 'lxml')

        # divs = soup.find_all('div')
        # details = divs[10]

        # get the title
        table_elements = soup.find_all('table', {'class': 'view-object-table'})
        table = table_elements[1]
        table_rows = table.find_all('tr')
        for tr in table_rows:
            td = tr.find_all('td', {'valign': 'top'})
            row = [i.text for i in td]
            titles.append(row[0])
            print(row[0])

        # get the author name
        table = table_elements[2]
        if 'δημιουργός' not in str(table).lower():
            table = table_elements[3]
        table_rows = table.find_all('tr')
        for tr in table_rows:
            td = tr.find_all('td', {'valign': 'top'})
            row = [i.text for i in td]
            authors.append(row[0])
            print(row[0])

        # get the ".pdf" link
        for url in (soup.find_all('a')):
            if 'pdf' in url.get('href').lower():
                pdf_links.append(base_url + url.get('href'))
                print(base_url + url.get('href'))

                pdf_filenames.append(url.contents[0])

        print('--------------------')

    print('')
    print('Writing to files...')

    if not os.path.exists(txt_path):
        os.mkdir(txt_path)

    # write list of ".pdf" links to file
    file = open(txt_path + links_file, 'w', encoding="utf-8")
    for pdf_link in pdf_links:
        file.write("%s\n" % pdf_link)
    file.close()

    # write list of ".pdf" filenames to file
    file = open(txt_path + pdfs_file, 'w', encoding="utf-8")
    for pdf_filename in pdf_filenames:
        file.write("%s\n" % pdf_filename)
    file.close()

    # write list of titles to file
    file = open(txt_path + titles_file, 'w', encoding="utf-8")
    for title in titles:
        file.write("%s\n" % title)
    file.close()

    # write list of author names to file
    file = open(txt_path + authors_file, 'w', encoding="utf-8")
    for author in authors:
        file.write("%s\n" % author)
    file.close()

    print('[DONE]')


if __name__ == '__main__':
    pyxida_scraper(department=1, phd_or_msc='phd')
