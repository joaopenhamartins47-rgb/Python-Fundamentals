from typing import Optional

from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from starlette import status

app = FastAPI()



class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    publish_date: int
    def __init__(self, id, title, author, description, rating, publish_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.publish_date = publish_date

#validation
class BookRequest(BaseModel):
    id: Optional[int] = Field(description='Id is not needed on create', default=None)
    title: str = Field(min_length=3, max_length=50)
    author: str = Field(min_length=1, max_length=50)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)
    publish_date: int = Field(gt=1900, lt=2027)

    model_config = { #pre define os valores, nao aparece mais o id
        "json_schema_extra":
        {
            "title": "A new book",
            "author": "codingwithroby",
            "description": "A new description of a book",
            "rating": 5,
            "publish_date": 2017
        }

    }



BOOKS = [
    Book(1, 'Systems of information', 'Unoeste', 'A good book for those who work', 7, 1988),
    Book(2, 'Machine Learning fundamentals', 'DeeplearningAI', 'ML concepts, a great book!', 10, 2018),
    Book(3, 'Be fast with fast API', 'Eric Roby', 'A good book', 7, 2020),
    Book(4, 'Mastering endpoints', 'Eric Roby', 'Excellent book!', 7, 2020),
    Book(5, 'Backend fundamentals', 'Eric Roby', 'A great book!', 7, 2016),
    Book(6, 'AI engineer', 'IBM', 'An awesome book!', 7, 2020),
]

@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail='Item not found')

@app.get("/books/release_date/", status_code=status.HTTP_200_OK)
async def books_date(book_date: int = Query(gt=1900, lt=2027)):
    books_release = []
    for i in range(len(BOOKS)):
        if BOOKS[i].publish_date == book_date:
            books_release.append(BOOKS[i])
    return books_release

@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_by_rating(book_rating: int = Query(gt=0, lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return
    #or return [book for book in BOOKS if book.rating == book_rating]




@app.post("/create-book", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))

def find_book_id(book: Book):
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1
    return book

@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_change = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_change = True
    if not book_change:
        raise HTTPException(status_code=404, detail='Item not found')


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')