import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.consilium.europa.eu/prado/en/prado-latest-authentic.html'
try:
  response = requests.get(url)
  response
except requests.exceptions.RequestException as e:  # This is the correct syntax
  raise SystemExit(e)


soup = BeautifulSoup(response.text, 'html.parser')

e = 0
image_page_link = 'https://www.consilium.europa.eu/prado/images'

all_images = []

for div in soup.find_all('div', attrs={'class': 'doc-thumbnails col-sm-4'}):
  try:
    a = div.find_all('a')
    img = div.find_all('img')[1]
    if len(a) > 0:
      ref = a[1]['href']

      file_extension = img['src'].split('.')[-1]
      person_id = ref.split('/')[0]
      image_id = ref.split('/')[1].split('-')[1].split('.')[0]

      final_link = image_page_link+'/'+person_id+'/'+image_id+'.'+file_extension
      print(final_link)
  except:
    print('EXC')
    continue

  all_images.append(final_link)

df = pd.DataFrame(all_images, columns=["links"])
df.to_csv('image_links.csv', index=False)