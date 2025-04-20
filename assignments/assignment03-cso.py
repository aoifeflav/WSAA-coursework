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




#References
#https://stackoverflow.com/questions/37398301/json-dumps-format-python (formating json dump)
# https://data.cso.ie/table/FIQ02 (Dataset used)
# How I found the correct dataset: I know that the exchequer data would be under the Central Bank of Ireland datasets 
# so I went to the CBI database and searched the word exchequer
# ChatGPT used for debugging