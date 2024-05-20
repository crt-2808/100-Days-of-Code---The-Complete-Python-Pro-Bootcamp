from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app=Flask(__name__)

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///new-books-collection.db"
db=SQLAlchemy(model_class=Base)
db.init_app(app)

class Book(db.Model):
    __tablename__="books"
    id: Mapped[int]=mapped_column(Integer, primary_key=True)
    title: Mapped[str]=mapped_column(String(250),nullable=False, unique=True)
    author: Mapped[str]=mapped_column(String(250),nullable=False)
    rate: Mapped[float]=mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()

with app.app_context():
    new_book=Book(id=1, title="Harry Potter", author="JK. Rowlling", rate=10)
    db.session.add(new_book)
    db.session.commit()