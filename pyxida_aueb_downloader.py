import urllib.request
import os


# name = 'di_phd_theses'
name = 'di_msc_theses'

filename = name + '_links.txt'

if not os.path.exists(name):
    os.mkdir(name)

file = open(filename, 'r')
pdf_links = file.read().splitlines()

for pdf_link in pdf_links:
    id = pdf_link.split('iid:')[1].split('&')[0]
    result = urllib.request.urlretrieve(pdf_link, filename=name + '/' + str(id) + '.pdf')
    print(result)
