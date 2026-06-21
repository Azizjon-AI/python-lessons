from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Session

app = FastAPI()

DATABASE_URL = "postgresql://postgres:1234@localhost:5432/books_db"
engine = create_engine(DATABASE_URL)

class Base(DeclarativeBase):
    pass

class BookModel(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    avtor = Column(String(50))
    pages = Column(Integer)
 
Base.metadata.create_all(engine)

class BooksSchema(BaseModel):
    name: str = Field(min_length=3, max_length=30)
    avtor: str = Field(min_length=3, max_length=50)
    pages: int = Field(ge=1, le=99999)

@app.get(
    "/books",
    tags=["Книгы"],
    summary="Показать все книгы"
)
def get_books():
    with Session(engine) as session:
        books = session.query(BookModel).all()
        return books

@app.post(
    "/books",
    status_code=201,
    tags=["Книгы"],
    summary="Добавить книгу"
)
def create_book(book: BooksSchema):
    with Session(engine) as session:
        new_book = BookModel(
            name=book.name,
            avtor=book.avtor,
            pages=book.pages
        )
        session.add(new_book)
        session.commit()
        return {"message": f"Книга {book.name} добавлена!"}

@app.get(
    "/books/{book_id}",
    tags=["Книгы"],
    summary="Найти книгу по id"
)
def get_student(book_id: int):
    with Session(engine) as session:
        book = session.get(BookModel, book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Книга не найдена")
        return book

@app.put(
    "/books/{book_id}",
    tags=["Книгы"],
    summary="Обнавить книгу"
)
def update_books(book_id: int, data: BooksSchema):
    with Session(engine) as session:
        book = session.get(BookModel, book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Книга не найдена")
        book.name = data.name
        book.avtor = data.avtor
        book.pages = data.pages
        session.commit()
        return {"message": f"Книга {book_id} обнавлена!"}

@app.patch(
    "/books/{book_id}",
    tags=["Книгы"],
    summary="Обновить автора книга"
)
def update_book(book_id: int, data: BooksSchema):
    with Session(engine) as session:
        book = session.get(BookModel, book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Книга не найдена")
        book.avtor = data.avtor
        session.commit()
        return {"message": f"Автор книга {book_id} обнавлена"}

@app.delete(
    "/books/{book_id}",
    tags=["Книгы"],
    summary="Удалить книгу"
)
def book_delete(book_id: int):
    with Session(engine) as session:
        book = session.get(BookModel, book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Книга не найдена!")
        session.delete(book)
        session.commit()
        return {"message": f"Книга {book_id} удалён!"}
