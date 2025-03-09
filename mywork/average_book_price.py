#Finds the average price of all books in the server
#Author: Aoife Flavin

import requests

url = "http://andrewbeatty1.pythonanywhere.com/books"
#response = requests.get(url)

def avg_book_price(books):
    if not books:
        print("No books found.")
        return 0
    
    total_price = sum(book.get("price", 0) for book in books)
    average_price = total_price / len(books)

    return round(average_price, 2)

if __name__ == "__main__":
    response = requests.get(url)
    books = response.json()  # Convert response to JSON
    avg_price = avg_book_price(books)
    print(f"Average book price: {avg_price}")
