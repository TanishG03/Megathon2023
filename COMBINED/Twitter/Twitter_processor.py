from bs4 import BeautifulSoup as BS
import time
import json

with open('text.html', 'r') as f:
    page_source = f.read()
soup = BS(page_source, features='html.parser')

data = soup.find_all(
    'div', class_='css-901oao css-cens5h r-1nao33i r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0')

first = True
for i in data:
    if first == True:
        perm = 'w'
        first = False
    else:
        perm = 'a'
    extracted_data = i.text.strip().replace("\n", " ").replace("\t", " ").replace("   ", " ").replace("'","").replace('"',"")
    with open('scraed_data_tw.txt', perm) as f:
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

index = page_source.find("<span class=\"css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0\" style=\"text-overflow: unset;\">Joined")
end = page_source.find('<', index+len("<span class=\"css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0\" style=\"text-overflow: unset;\">Joined"))
joined = (page_source[index+len("<span class=\"css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0\" style=\"text-overflow: unset;\">"):end])
# Printing the extracted information
with open("meta_data_tw.txt","w") as f:
    f.write("Person's Name:"+ person_name+"\n")
    f.write("Description:"+ description+"\n")
    f.write(f"Followers: {user_interaction_counts[0]}\nFollowing: {user_interaction_counts[1]}\n")
    f.write(joined+"\n")

with open("scraed_data_tw.txt","r+") as f:
    txt=f.read()
    txt=txt.replace("   "," ")
    txt=txt.replace("'"," ")
    txt=txt.replace('"'," ")
    f.write(txt)
