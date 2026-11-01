# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API for a book list using the FastAPI framework. You will learn how routes, path parameters, request bodies, and HTTP status codes work together.

## 📝 Tasks

### 🛠️	Create Your First Endpoint

#### Description
Start the FastAPI app from the starter code and add a `GET /books` endpoint that returns the list of books.

#### Requirements
Completed program should:

- Run with `uvicorn starter-code:app --reload` without errors
- Return all books as JSON from `GET /books`
- Show the endpoint on the automatic docs page at `/docs`


### 🛠️	Read One Book by ID

#### Description
Add a `GET /books/{book_id}` endpoint that returns a single book using a path parameter.

#### Requirements
Completed program should:

- Return the matching book when the ID exists
- Return status code `404` with a clear message when the ID does not exist
- Accept only whole numbers as the ID

```
GET /books/1   ->  {"id": 1, "title": "Dune", "author": "Frank Herbert"}
GET /books/99  ->  404 {"detail": "Book not found"}
```


### 🛠️	Add a New Book

#### Description
Add a `POST /books` endpoint that accepts a new book in the request body, validated with a Pydantic model.

#### Requirements
Completed program should:

- Define a `Book` model with `title` and `author` fields
- Give the new book the next free ID and return it with status code `201`
- Reject a request with a missing field (FastAPI returns `422` automatically)
