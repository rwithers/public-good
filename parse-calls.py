from bs4 import BeautifulSoup

import requests
import googlemaps 
import os
import json
from call import Call
from callDao import CallDao 

dao = CallDao()

gmaps = googlemaps.Client(os.environ['API_KEY'])

headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

# todo remove url to configuration / environment variable
url = "http://www.slmpd.org/cfs.aspx"
req = requests.get(url, headers)
 
soup = BeautifulSoup(req.content, "lxml")

rows = soup.find_all('tr')

for row in rows:
	elements = row.find_all('td')

	c = Call(elements[0].string, elements[1].string, elements[2].string, elements[3].string)

	print(c.toString())
	print()

	extended_address = gmaps.geocode(c.getAddress())

	print (extended_address)

	formatted_address = extended_address[0]["formatted_address"]
	latval = extended_address[0]["geometry"]["location"]["lat"]
	lonval = extended_address[0]["geometry"]["location"]["lng"]

	print(formatted_address)
	print(f"{latval}, {lonval}")

	dao.storeCall(c, extended_address, formatted_address, latval, lonval)





