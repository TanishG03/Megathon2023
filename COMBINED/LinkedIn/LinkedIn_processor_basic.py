from bs4 import BeautifulSoup as BS
import time

page_source=''
with open('basic.html', 'r') as f:
    page_source=f.read()
soup=BS(page_source,features='html.parser')
connections=soup.find('span', class_='t-bold').text
about=soup.find('div',class_='inline-show-more-text inline-show-more-text--is-collapsed inline-show-more-text--is-collapsed-with-line-clamp full-width')
about_txt=''
with open('scraed_data_ln.txt', 'w') as f:
        f.write(connections)
        f.write('\n')
if about:
    extracted_text = about.text.strip().replace("   ","").replace("\t","").replace("\n","")
    with open('scraed_data_ln.txt', 'a') as f:
        f.write(extracted_text)
        f.write('\n')

print(about_txt)

#exp=soup.find_all('li',class_='artdeco-list__item pvs-list__item--line-separated pvs-list__item--one-column')
#for i in exp:
#    extracted_text= i.text
#    extracted_text=extracted_text.replace("\n","")
#    extracted_text=extracted_text.replace("\t","")
#    extracted_text=extracted_text.replace("   ","")
#    if len(extracted_text) > 0:
#        print(extracted_text)