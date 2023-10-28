from bs4 import BeautifulSoup as BS
import time

page_source=''
with open('text.html', 'r') as f:
    page_source=f.read()
soup=BS(page_source,features='html.parser')

data=soup.find_all('span',class_='css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0')

for i in data:
    extracted_data=i.text
    print(extracted_data)