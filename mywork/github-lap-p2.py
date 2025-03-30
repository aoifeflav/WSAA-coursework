#Pracise getting an API key from a private github account
#Author: Aoife Flavin

import requests
from config import config as cfg
import json

url = 'https://api.github.com/repos/aoifeflav/aprivateone'
apiKey = cfg["githubapikey"]

response = requests.get(url, auth=('token',apiKey))
repoJSON = response.json()
#print (response.json())
with open("githubapi.json", 'w') as fp:
    json.dump(repoJSON, fp, indent=4)


