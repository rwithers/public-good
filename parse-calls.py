from bs4 import BeautifulSoup

import requests
import googlemaps 
import os
import json

from call import Call

gmaps = googlemaps.Client(os.environ['API_KEY'])

headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

url = "http://www.slmpd.org/cfs.aspx"
req = requests.get(url, headers)
 
soup = BeautifulSoup(req.content, "lxml")

rows = soup.find_all('tr')

for row in rows:
	elements = row.find_all('td')

	c = Call(elements[0], elements[1], elements[2], elements[3])

	print(c.toString())
	print()

	result = gmaps.geocode(c.getAddress())

	print(result[0]["formatted_address"])
	print(result[0]["geometry"])


