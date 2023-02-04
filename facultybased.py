import requests
from bs4 import BeautifulSoup
import json
import os
from dotenv import load_dotenv

load_dotenv()

# get the html page
url = os.getenv('URL')
response = requests.get(url, verify=False)

# parse the html page
soup = BeautifulSoup(response.text, 'html.parser')

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

    # check if faculty is already in the dictionary
    if faculty in data:
        # add the new course to the existing list
        data[faculty].append({"course_code":subject_code,"course_name":subject_title})
    else:
        # create a new list and add the course
        data[faculty] = [{"course_code":subject_code,"course_name":subject_title}]

# convert the dictionary to json format
data_json = json.dumps(data, indent=4)

# write the json data to a file
with open('scraped_data.json','w') as f:
    f.write(data_json)