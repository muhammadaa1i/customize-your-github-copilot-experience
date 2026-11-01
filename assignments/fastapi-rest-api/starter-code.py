# Starter Code for the Building REST APIs with FastAPI assignment
# Run with: uvicorn starter-code:app --reload

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Book List API")

books = [
    {"id": 1, "title": "Dune", "author": "Frank Herbert"},
    {"id": 2, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
]


class Book(BaseModel):
    title: str
    author: str


# TODO: Task 1 - return all books
# @app.get("/books")
# def list_books():
#     ...

# TODO: Task 2 - return one book or raise HTTPException(404)
# @app.get("/books/{book_id}")
# def get_book(book_id: int):
#     ...

# TODO: Task 3 - add a new book and return it with status 201
# @app.post("/books", status_code=201)
# def add_book(book: Book):
#     ...
