from flask import Flask, jsonify, request

libniryan = Flask(__name__)

books = [
    {
        "book_id": 1,
        "title": "Florante at Laura",
        "author": "Francisco Balagtas",
        "copies": 3,
        "available": 3
    },
    {
        "book_id": 2,
        "title": "The King in Yellow",
        "author": "Robert W. Chambers",
        "copies": 1,
        "available": 1
    },
    {
        "book_id": 3,
        "title": "House of Leaves",
        "author": "Mark Z. Danielewski",
        "copies": 2,
        "available": 2
    }
]

transactions = []


# Put your code here and test it
# You can also modify the code

if __name__ == '__main__':
    libniryan.run(host='127.0.0.1', port=5133, debug=True)