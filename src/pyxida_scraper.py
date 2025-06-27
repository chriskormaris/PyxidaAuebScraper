import os

import bs4 as bs
import requests

from src.constants import *


def is_english(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


def pyxida_scraper(department=1, phd_or_msc='phd', txt_path=txt_path):
    directory = txt_path
    if department == 1:  # Τμήμα Πληροφορικής / Department of Informatics
        if phd_or_msc.lower() == 'phd':
            middle_url = '/collections/a85735e2-7304-4ca6-ab61-f216fa9a6f97'
        else:
            middle_url = '/collections/8e06e33f-4257-40ab-9ba2-b2a3739c14d0'
        directory = os.path.join(directory, 'di')
    elif department == 2:  # Τμήμα Στατιστικής / Department of Statistics
        if phd_or_msc.lower() == 'phd':
            middle_url = '/collections/a85735e2-7304-4ca6-ab61-f216fa9a6f97?cp.page'
        else:
            middle_url = '/collections/8e06e33f-4257-40ab-9ba2-b2a3739c14d0'
        directory = os.path.join(directory, 'ds')
    elif department == 3:  # Τμήμα Οργάνωσης και Διοίκησης Επιχειρήσεων / Department of Business Administration
        if phd_or_msc.lower() == 'phd':
            middle_url = '/collections/b206877a-02e4-4feb-bc53-e7ee95b6ea75'
        else:
            middle_url = '/collections/e402ac94-d8e1-45f7-906e-6a55bb0553ed'
        directory = os.path.join(directory, 'dba')
    elif department == 4:  # Τμήμα Λογιστικής και Χρηματοοικονομικής / Department of Accounting and Finance
        if phd_or_msc.lower() == 'phd':
            middle_url = '/collections/ad63fba0-cb3e-460f-97d1-84f4b62d34ee'
        else:
            middle_url = '/collections/0981f406-0cf6-48ae-8d9f-021762e54a87'
        directory = os.path.join(directory, 'daf')
    elif department == 5:  # Τμήμα Επικοινωνίας και Μάρκετινγκ / Department of Marketing and Communication
        if phd_or_msc.lower() == 'phd':
            middle_url = '/collections/a15c9c65-c5f9-4908-a8ec-86ecaa463551'
        else:
            middle_url = '/collections/4f95cb1e-bbd4-4648-8620-5e9a7381a42f'
        directory = os.path.join(directory, 'dmc')
    elif department == 6:  # Τμήμα Διοικητικής Επιστήμης και Τεχνολογίας / Department of Management Science and Technology
        if phd_or_msc.lower() == 'phd':
            middle_url = '/collections/15f5c7d0-399b-4bf4-af65-a2d9c3abea98'
        else:
            middle_url = '/collections/d2816650-ab95-44ea-90e1-aa7eacf7f9ee'
        directory = os.path.join(directory, 'dmst')
    elif department == 7:  # Τμήμα Οικονομικής Επιστήμης / Department of Economics
        if phd_or_msc.lower() == 'phd':
            middle_url = '/collections/393f596b-20a3-48d4-803b-c3496735891a'
        else:
            middle_url = '/collections/b2e20db7-04b1-4193-8b82-62f800341cf0'
        directory = os.path.join(directory, 'de')
    # Τμήμα Διεθνών και Ευρωπαϊκών Οικονομικών Σπουδών /
    # Department of International and European Economic Studies
    else:
        if phd_or_msc.lower() == 'phd':
            middle_url = '/collections/bacd9636-439e-4652-810e-daf0781ccfb8'
        else:
            middle_url = '/collections/d3ce98d2-1f19-487e-bb47-7d671b613c1c'
        directory = os.path.join(directory, 'diees')
    directory += '_' + phd_or_msc.lower() + '_dissertations'

    links_file = os.path.join(directory, 'links.txt')
    pdfs_file = os.path.join(directory, 'filenames.txt')
    authors_file = os.path.join(directory, 'authors.txt')
    titles_file = os.path.join(directory, 'titles.txt')

    thesis_links = []

    first_page_url = pyxida_base_url + middle_url
    source = requests.get(first_page_url).text
    soup = bs.BeautifulSoup(source, 'lxml')
    page_links = soup.find_all('a', {'class': 'page-link ng-star-inserted'})
    if len(page_links) > 0:
        num_pages = int(page_links[-1].text)
    else:
        num_pages = 1

    for page in range(1, num_pages + 1):
        current_page_url = pyxida_base_url + middle_url + '?cp.page=' + str(page)
        source = requests.get(current_page_url).text
        soup = bs.BeautifulSoup(source, 'lxml')

        for url in (soup.find_all('a')):
            if url.get('href') and '/items/' in url.get('href'):
                thesis_link = pyxida_base_url + url.get('href')
                if thesis_link not in thesis_links:
                    print(thesis_link)
                    thesis_links.append(thesis_link)

    print()

    pdf_links = []
    authors = []
    titles = []
    pdf_filenames = []

    for link in thesis_links:
        source = requests.get(link).text
        soup = bs.BeautifulSoup(source, 'lxml')

        # get the title
        h1_elements = soup.find_all('h1', {'class': 'item-page-title-field'})
        if len(h1_elements) > 0:
            h1_element = h1_elements[0]
            span_element = h1_element.find_all('span')[0]
            title = span_element.text
            titles.append(title)
            print(title)
        else:
            titles.append('')

        # get the author name
        span_elements = soup.find_all('span', {'class': 'dont-break-out ng-star-inserted'})
        if len(span_elements) > 0:
            if is_english(span_elements[0]) or len(span_elements) == 1:
                author = span_elements[0].text
            else:
                author = span_elements[1].text
            authors.append(author)
            print(author)
        else:
            authors.append('')

        ds_file_download_links = soup.find_all('ds-file-download-link')
        if len(ds_file_download_links) > 0:
            # get the ".pdf" link
            ds_file_download_link = ds_file_download_links[0]
            url = ds_file_download_link.find_all('a')[0]
            pdf_link = pyxida_base_url + url.get('href')
            pdf_links.append(pdf_link)
            print(pdf_link)

            # get the ".pdf" filename
            pdf_filename = url.find_all('span')[0].text
            pdf_filenames.append(pdf_filename)
        else:
            pdf_links.append('')
            pdf_filenames.append('')

        print('--------------------')

    print('')
    print('Writing to files...')

    if not os.path.exists(txt_path):
        os.mkdir(txt_path)

    if not os.path.exists(directory):
        os.mkdir(directory)

    # write list of ".pdf" links to file
    file = open(links_file, 'w', encoding="utf-8")
    for pdf_link in pdf_links:
        file.write("%s\n" % pdf_link)
    file.close()

    # write list of ".pdf" filenames to file
    file = open(pdfs_file, 'w', encoding="utf-8")
    for pdf_filename in pdf_filenames:
        file.write("%s\n" % pdf_filename)
    file.close()

    # write list of titles to file
    file = open(titles_file, 'w', encoding="utf-8")
    for title in titles:
        file.write("%s\n" % title)
    file.close()

    # write list of author names to file
    file = open(authors_file, 'w', encoding="utf-8")
    for author in authors:
        file.write("%s\n" % author)
    file.close()

    print('[DONE]')
    print()


if __name__ == '__main__':
    pyxida_scraper(department=1, phd_or_msc='phd', txt_path=os.path.join('..', txt_path))
