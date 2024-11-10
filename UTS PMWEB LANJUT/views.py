from flask import Blueprint
from app.controllers import book_controller

book_bp = Blueprint('books', __name__, url_prefix='/books')

book_bp.route('/', methods=['GET'])(book_controller.get_books)
book_bp.route('/<int:book_id>', methods=['GET'])(book_controller.get_book)
book_bp.route('/', methods=['POST'])(book_controller.add_book)
book_bp.route('/<int:book_id>', methods=['PUT'])(book_controller.update_book)
book_bp.route('/<int:book_id>', methods=['PATCH'])(book_controller.patch_book)
book_bp.route('/<int:book_id>', methods=['DELETE'])(book_controller.delete_book)
