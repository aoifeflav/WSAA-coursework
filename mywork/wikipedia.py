#Converts a Wikipediapage into a pdf
#Author: Aoife Flavin

import requests

import urllib.parse

from wikiconfig import config as cfg

target_url = "https://en.wikipedia.org/wiki/John_McLaren_(baseball)"

apiKey = cfg["htmltopdfkey"]
#api = 'https://api.html2pdf.app/v1/generate?html=https://example.com&apiKey={your-api-key}'

api_url = 'https://api.html2pdf.app/v1/generate'

params = {'url': target_url, 'apiKey': apiKey}
parsedparams = urllib.parse.urlencode(params)
request_url = api_url + "?" + parsedparams

response = requests.get(request_url)
print(response.status_code)

result = response.content
with open("document.pdf", "wb") as handler:
    handler.write(result)