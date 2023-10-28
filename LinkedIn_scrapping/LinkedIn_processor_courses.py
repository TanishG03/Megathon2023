from bs4 import BeautifulSoup as BS
import time

page_source=''
with open('courses.html', 'r') as f:
    page_source=f.read()
soup=BS(page_source,features='html.parser')

texts=soup.find_all('span',class_='visually-hidden')

for i in texts[5:]:
    extracted_text=i.text.strip().replace("   ","").replace("\t","").replace("\n","")

    with open('scraed_data.txt', 'a') as f:
        f.write(extracted_text)
        f.write('\n')