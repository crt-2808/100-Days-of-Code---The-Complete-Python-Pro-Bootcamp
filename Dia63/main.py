from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


app = Flask(__name__)

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(model_class=Base)
db.init_app(app)


class Book(Base):
    __tablename__="books"
    id: Mapped[int]=mapped_column(Integer, primary_key=True)
    title: Mapped[str]=mapped_column(String, unique=True, nullable=False)
    author: Mapped[str]=mapped_column(String, nullable=False)
    rate: Mapped[float]=mapped_column(Float, nullable=False)




@app.route('/')
def home():
    result=db.session.execute(db.select(Book).order_by(Book.title)).scalars().all()
    all_books=result
    return render_template('index.html', books=all_books)



@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method=="POST":
        new_book=Book(
            title=request.form["title"],
            author=request.form["author"],
            rate=request.form["rating"],
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("add.html")

@app.route("/editar/<int:id>", methods=["GET", "POST"])
def edit(id):
    book=db.session.get(Book, id)
    if not book:
        return "No se encontro"
    if request.method=="POST":
        book.rate=float(request.form["rating"])
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", book=book)

@app.route("/delete")
def delete():
    book_id=request.args.get('id')
    book_to_delete=db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)

