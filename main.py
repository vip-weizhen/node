import time
import requests
from bs4 import BeautifulSoup

urls = [
  'https://cdn.weizhen.xyz/https://raw.githubusercontent.com/freefq/free/master/v2',
  'https://cdn.weizhen.xyz/https://raw.githubusercontent.com/Jsnzkpg/Jsnzkpg/Jsnzkpg/Jsnzkpg',
  'https://cdn.weizhen.xyz/https://raw.githubusercontent.com/ripaojiedian/freenode/main/sub',
  'https://sub.sharecentre.online/sub',
  'https://cdn.weizhen.xyz/https://raw.githubusercontent.com/1218749540/work/main/jdnew',
  'https://freefq.neocities.org/free.txt'
]

with open('node.txt', 'a', encoding='utf-8') as f:

  for url in urls:
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    text_content = soup.get_text()
    f.write(text_content)

while True:
  time.sleep(600)
