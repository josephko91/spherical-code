import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
'''
Parse the specified webpage and extract text from all text files on the page. 
'''
# URL of the webpage you want to extract links from
page_url = "http://neilsloane.com/packings/dim3/"
# Send a GET request to fetch the page content
response = requests.get(url)
# Where to save text files
save_directory = '/home/jko/spherical-code/data/text-files'
# find all txt links and save
soup = BeautifulSoup(response.content, "html.parser")
links = soup.find_all('a', href=True)
for link in links:
    if '.txt' in link['href']:
        filename = link['href']
        filename = filename.strip()
        save_path = os.path.join(save_directory, filename)
        file_url = urljoin(page_url, filename)
        text_response = requests.get(file_url)
        text = text_response.text
        with open(save_path, 'w') as file:
            file.write(text)