from flask import Flask, jsonify, request

libniryan = Flask(__name__)

# Complete book inventory (including all books added by the team)
books = {
    1: {"book_id": 1, "title": "Florante at Laura", "author": "Francisco Balagtas", "copies": 3, "available": 3},
    2: {"book_id": 2, "title": "The King in Yellow", "author": "Robert W. Chambers", "copies": 1, "available": 1},
    3: {"book_id": 3, "title": "House of Leaves", "author": "Mark Z. Danielewski", "copies": 2, "available": 2}
}

# for borrowing
transactions = {}

# ==========================================
# CASSEY: GET /api/books
# ==========================================
@libniryan.route('/api/books', methods=['GET'])
def get_books():
    # Return 404 Not Found if the catalog is empty
    if not books:
        return jsonify({
            "status": "error",
            "message": "No books found in the library catalog."
        }), 404

    # Return 200 OK with the full book list
    return jsonify({
        "status": "success",
        "count": len(books),
        "data": books
    }), 200

       # ==========================================
# MOHAMMAD: GET /api/books/{id}
# ==========================================
@libniryan.route('/api/books/<int:book_id>', methods=['GET'])
def get_book_by_id(book_id):
    book = books.get(book_id)
    if not book:
        return jsonify({
            "status": "error",
            "message": "Book not found."
        }), 404

    return jsonify({
        "status": "success",
        "data": book
    }), 200

# MERCADO: POST /api/books

@libniryan.route('/api/books', methods=['POST'])
def add_book():
    data = request.get_json(silent=True)

    #Validate
    if not isinstance(data, dict):
        return jsonify({
            "status": "error",
            "message": "Invalid JSON request."
        }), 400

    title = data.get("title")
    author = data.get("author")
    copies = data.get("copies")

    if not title or not author or type(copies) is not int or copies <= 0:
        return jsonify({
            "status": "error",
            "message": "Invalid or missing book information."
        }), 400

    #New Book ID
    new_id = max(books.keys(), default=0) + 1

    #Create Book
    new_book = {
        "book_id": new_id,
        "title": title,
        "author": author,
        "copies": copies,
        "available": copies
    }

    #Add Book
    books[new_id] = new_book

    return jsonify({
        "status": "success",
        "message": "Book successfully added.",
        "data": new_book
    }), 201

# SUBA: PUT /api/return/{transaction_id}

@libniryan.route('/api/return/<int:transaction_id>', methods=['PUT'])
def return_book(transaction_id):

    # Finds the transaction
    transaction = transactions.get(transaction_id)

    # Checks if transaction exists
    if not transaction:
        return jsonify({
            "status": "error",
            "message": "Transaction not found."
        }), 404

    # Checks if the book has already been returned
    if transaction["status"] == "returned":
        return jsonify({
            "status": "error",
            "message": "Book already returned."
        }), 409

    book = books.get(transaction["book_id"])

    # If book exsist
    if not book:
        return jsonify({
            "status": "error",
            "message": "Book not found."
        }), 404

    # Updates book availability and status
    book["available"] += 1
    transaction["status"] = "returned"

    # Success
    return jsonify({
        "status": "success",
        "message": "Book successfully returned.",
        "data": transaction
    }), 200


if __name__ == '__main__':
    libniryan.run(host='127.0.0.1', port=5133, debug=True)
