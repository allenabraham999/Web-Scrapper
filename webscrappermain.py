
# link inorder to understand working https://www.digitalocean.com/community/tutorials/how-to-work-with-web-data-using-requests-and-beautiful-soup-with-python-3
import requests
from bs4 import BeautifulSoup
import csv

# Collect and parse first page

pages = []
for i in range(1, 5):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + str(i) + '.htm'
    pages.append(url)

f = csv.writer(open("names.csv",'w'))
f.writerow(['Name', 'Link'])


for items in pages:
    page = requests.get(items)
    soup = BeautifulSoup(page.text, "html.parser")
    #basically to destroy the last unwanted parts
    last_links = soup.find(class_='AlphaNav')
    last_links.decompose()

    # Pull all text from the BodyText div
    artist_name_list = soup.find(class_='BodyText')

    # Pull text from all instances of <a> tag within BodyText div
    artist_name_list_items = artist_name_list.find_all('a')


    # Create for loop to print out all artists' names

    for artist_name in artist_name_list_items:
        names = artist_name.contents[0]
        links = 'https://web.archive.org' + artist_name.get('href')

        f.writerow([names, links])
