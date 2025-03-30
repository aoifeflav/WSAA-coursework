#This program will read a file from a repository and replace all the instances of the text "Andrew" with "Aoife" 
# The program will then commit those changes and push the file back to the repository
#Author: Aoife Flavin

from github import Github
from config import config as cfg
import requests

#load api key from config file
apiKey = cfg["githubAssignmentApiKey"]
g = Github(apiKey)

#get the repository
repo = g.get_repo("aoifeflav/Assignment-4-repo")

#get file info
fileInfo = repo.get_contents("story.txt")
urlOfFile = fileInfo.download_url

#download contents
response = requests.get(urlOfFile)
contentsOfFile = response.text
#print(contentsOfFile)

# replace names
newContents = contentsOfFile.replace("Andrew", "Aoife")
newContents = newContents.replace(" he ", " she ").replace(" his ", " her ")

# commit and push changes
commitMessage = "Replaced 'Andrew' with 'Aoife' and changes the pronouns"
gitHubResponse = repo.update_file(fileInfo.path, commitMessage, newContents, fileInfo.sha)
