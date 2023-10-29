from bs4 import BeautifulSoup as BS
import time

page_source = ''
with open('post.html', 'r') as f:
    page_source = f.read()
soup = BS(page_source, features='html.parser')

texts = soup.find_all(
    'div', class_='xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs x126k92a')
extracted_data = ""
for i in texts:
    extracted_data += i.text +"\n"

with open('scraed_data_fb.txt', 'w') as f:
    f.write(extracted_data)
    f.write('\n')
