from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "title one","author": "author one","category": "science"},
    {"title": "title two", "author": "author two", "category": "science"},
    {"title": "title three", "author": "author three", "category": "history"},
    {"title": "title four", "author": "author four", "category": "math"},
    {"title": "title five", "author": "author five", "category": "math"},
    {"title": "title six", "author": "author two", "category": "math"},
]

@app.get("/books")
async def read_all_books():
    return BOOKS

#Dynamic path parameters
@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

#Query parameters
@app.get("/books/category/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

#Query parameters and path parameters
@app.get("/books/author/{book_author}/")
async def read_author_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == book_author.casefold() and book.get("category").casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return





