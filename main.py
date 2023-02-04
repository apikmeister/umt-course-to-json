import requests
from bs4 import BeautifulSoup
import json
import os
from dotenv import load_dotenv

load_dotenv()

# get the html page
url = os.getenv('URL')
page = requests.get(url, verify=False)

# parse the html page
soup = BeautifulSoup(page.text, 'html.parser')

# extract the table
table = soup.find('table', {'class': 'table table-bordered table-hover'})
table_rows = table.find_all('tr')

# create a dictionary to store the data
data = {}

# loop through the table to get the data
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    subject_code = row[1]
    faculty = row[3]
    subject_title = row[2]
    # store the data
    data[subject_code] = {
        'faculty': faculty,
        'title': subject_title
    }

# save the data as json
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)