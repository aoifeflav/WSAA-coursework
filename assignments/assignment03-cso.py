# Save a dataset for the exchequer account (historical series) into a json file
#Author: Aoife Flavin

import requests
import json

# api
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

#get the data from the api
response = requests.get(url)


with open("cso.json", "w") as file:
    json.dump(requests.get(url).json(), file, indent=4)

print("Data saved to cso.json")






#https://stackoverflow.com/questions/37398301/json-dumps-format-python
# I know that the exchequer would be under the CBI so I went to the CBI database and searced th word exchequer