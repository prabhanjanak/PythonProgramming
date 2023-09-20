import requests
import os
from bs4 import BeautifulSoup

# User input for comic number
n = input("Input the comic number: ")
url = f'https://xkcd.com/{n}/'

# Create a directory and download the comic if it exists
if (res := requests.get(url)).status_code == 200:
    os.makedirs('xkcd', exist_ok=True)
    comic_url = 'http:' + BeautifulSoup(res.text, 'html.parser').select_one('#comic img')['src']
    if (image := requests.get(comic_url)).status_code == 200:
        with open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb') as image_file:
            image_file.write(image.content)
        print('Successfully downloaded')
    else:
        print('Failed to download comic image.')
else:
    print('Comic not found for the specified number.')
