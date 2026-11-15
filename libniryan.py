from flask import Flask, jsonify, request

libniryan = Flask(__name__)

# Complete book inventory (including all books added by the team)
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


# SUBA: PUT /api/return/{transaction_id}

@libniryan.route('/api/return/<int:transaction_id>', methods=["PUT"])
def return_book(transaction_id):

    # Finds the transaction
    for transaction in transactions:

        if transaction["transaction_id"] == transaction_id:

            # Checks if the book has already been returned
            if transaction["status"] == "returned":
                return jsonify({
                    "status": "error",
                    "message": "Book has already been returned."
                }), 409


            # Updates the book availability
            for book in books:
                if book["book_id"] == transaction["book_id"]:

                    book["available"] += 1
                    transaction["status"] = "returned"

                    return jsonify({
                        "status": "success",
                        "message": "Book successfully returned.",
                        "data": transaction
                    }), 200


    # Transaction not found
    return jsonify({
        "status": "error",
        "message": "Transaction not found."
    }), 404


if __name__ == '__main__':
    libniryan.run(host='127.0.0.1', port=5133, debug=True)
