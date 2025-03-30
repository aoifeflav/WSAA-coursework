# Practicing using pygithub
#Author: Aoife Flavin

from github import Github
from config import config as cfg
import requests

apiKey = cfg["githubapikey"]
g = Github(apiKey)

repo = g.get_repo("aoifeflav/aprivateone")
print(repo.clone_url)

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url

#print(urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
#print (contentOfFile)

newContents = contentOfFile + " more stuff \n"
print (newContents)


gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",
newContents,fileInfo.sha)
#print (gitHubResponse)

