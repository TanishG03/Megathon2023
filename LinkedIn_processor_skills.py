from bs4 import BeautifulSoup as BS
import time

page_source=''
with open('skills.html', 'r') as f:
    page_source=f.read()
soup=BS(page_source,features='html.parser')

texts=soup.find_all('div',class_='display-flex flex-column full-width align-self-center')

for i in texts:
    extracted_text=i.text.strip().replace("  ","").replace("\t"," ").replace("\n","")

    with open('scraed_data.txt', 'a') as f:
        f.write(extracted_text)
        f.write('\n')