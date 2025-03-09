# Using python to analyse books in an API
#Author: Aoife Flavin

import requests

url = "http://andrewbeatty1.pythonanywhere.com/books"
response = requests.get(url)

#print(response.json)

def readbooks():
    response = requests.get(url)
    return response.json()
#if __name__ == "__main__":
    #print(readbooks())

def readbook(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    return response.json()
#if __name__ == "__main__":
#    print(readbook(1478))

def createbook(book):
    response = requests.post(url, json=book)
    return response.json
#if __name__ == "__main__":
#    new_book = {'author': 'William Sheakespeare', 'id': 3333, 'price': 33.3, 'title': 'King Lear'}
#    print(createbook(new_book))

def updatebook(id, book):
    puturl = url + "/" +str(id)
    response = requests.put(puturl, json=book)
    return response.json
#if __name__ == "__main__":
#    updated_book = {'author': 'William Sheakespeare I', 'price': 13.3, 'title': 'King Lear!'}
#    print(updatebook(3333, updated_book))

def deletebook(id):
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)
if __name__ == "__main__":
    print(deletebook(1521))