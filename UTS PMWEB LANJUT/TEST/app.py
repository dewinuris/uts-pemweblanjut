
from flask import Flask, jsonify, request
app = Flask (__name__)

books = {
    1: {'id': 1, 'title': 'Python Basics', 'author': 'John Doe', 'year': 2020},
    2: {'id': 2, 'title': 'Flask for Beginners', 'author': 'Jane Smith', 'year': 2021},
    3: {'id': 3, 'title': 'Laskar Pelangi', 'author': 'Nidji', 'year': 2021}
}

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book =books.get(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    return jsonify(book)

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    new_id = max(books.keys()) + 1
    new_book ['id'] = new_id
    books [new_id] = new_book
    return jsonify({'message': 'Book added successfully!', 'book': new_book}), 201


@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    updated_book = request.get_json()
    book = books.get(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    updated_book['id'] = book_id 
    books [book_id] = updated_book
    return jsonify({'message': 'Book updated successfully!', 'book': updated_book})

@app.route('/books/<int:book_id>', methods=['PATCH'])
def patch_book(book_id):
    book = books.get(book_id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    
    patch_data = request.get_json()
    for key, value in patch_data.items():
        if key in book:
            book[key] = value
            
    return jsonify({'message': 'Book partially updated successfully!', 'book': book})

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = books.pop(book_id, None)
    if not book:
        return jsonify({'error': 'Book not found'}), 484
    return jsonify({'message': 'Book deleted successfully!'})

@app.errorhandler (404)
def not_found(error):
    return jsonify({'error': 'Not Found'}), 404

if __name__=='__main__':
    app.run(debug=True)
