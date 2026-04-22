from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()



class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

#validation
class BookRequest(BaseModel):
    id: Optional[int] = Field(description='Id is not needed on create', default=None)
    title: str = Field(min_length=3, max_length=50)
    author: str = Field(min_length=1, max_length=50)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)

    model_config = { #pre define os valores, nao aparece mais o id
        "json_schema_extra":
        {
            "title": "A new book",
            "author": "codingwithroby",
            "description": "A new description of a book",
            "rating": 5
        }

    }



BOOKS = [
    Book(1, 'Sistems of information', 'Unoeste', 'A good book for those who work', 7),
    Book(2, 'Machine Learning fundamentals', 'DeeplearningAI', 'ML concepts, a great book!', 10),
    Book(3, 'Be fast with fast API', 'Eric Roby', 'A good book', 7),
    Book(4, 'Mastering endpoints', 'Eric Roby', 'Excelent book!', 7),
    Book(5, 'Backend fundamentals', 'Eric Roby', 'A great book!', 7),
    Book(6, 'AI engineer', 'IBM', 'An awesome book!', 7),
]

@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_id}")
async def read_book(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book


@app.get("/books/")
async def read_by_rating(book_rating: int):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return
    #or return [book for book in BOOKS if book.rating == book_rating]




@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))

def find_book_id(book: Book):
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1
    return book