from bs4 import BeautifulSoup as BS
import time
import json

page_source = ''
with open('text.html', 'r') as f:
    page_source = f.read()
soup = BS(page_source, features='html.parser')

data = soup.find_all(
    'div', class_='css-901oao css-cens5h r-1nao33i r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0')

for i in data:
    extracted_data = i.text.strip().replace("\n", " ").replace("\t", " ").replace("   ", " ").replace("'","").replace('"',"")
    with open('scraed_data.txt', 'a') as f:
        f.write(extracted_data)
        f.write('\n')

data_x=soup.find('script',type='application/ld+json')
data = json.loads(str(data_x.text))

person_name = data['author']['givenName']
description = data['author']['description']
interaction_counters = data['author']['interactionStatistic']

# Extracting interaction counters of all types
interaction_types = [counter['interactionType'] for counter in interaction_counters]
user_interaction_counts = [counter['userInteractionCount'] for counter in interaction_counters]

# Printing the extracted information
with open("meta_data.txt","w") as f:
    f.write("Person's Name:"+ person_name+"\n")
    f.write("Description:"+ description+"\n")
    f.write("Interaction Types:"+ str(interaction_types)+"\n")
    f.write("User Interaction Counts:"+ str(user_interaction_counts)+"\n")

