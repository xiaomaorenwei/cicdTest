# web_app.py
# 图书管理系统Web前端

from flask import Flask, render_template, request, redirect, url_for, flash
from book import Book
from library import Library

app = Flask(__name__)
app.secret_key = 'library_secret_key'
library = Library()

@app.route('/')
def index():
    books = library.list_all_books()
    return render_template('index.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        book_id = request.form['book_id']
        title = request.form['title']
        author = request.form['author']
        publisher = request.form['publisher']
        book = Book(book_id, title, author, publisher)
        library.add_book(book)
        flash('添加成功！')
        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/delete/<book_id>')
def delete_book(book_id):
    library.remove_book(book_id)
    flash('删除成功！')
    return redirect(url_for('index'))

@app.route('/search', methods=['GET', 'POST'])
def search_books():
    results = []
    keyword = ''
    if request.method == 'POST':
        keyword = request.form['keyword']
        results = library.search_books(keyword)
    return render_template('search.html', results=results, keyword=keyword)

@app.route('/borrow/<book_id>', methods=['GET', 'POST'])
def borrow_book(book_id):
    if request.method == 'POST':
        borrower = request.form['borrower']
        library.borrow_book(book_id, borrower)
        flash('借阅成功！')
        return redirect(url_for('index'))
    return render_template('borrow.html', book_id=book_id)

@app.route('/return/<book_id>')
def return_book(book_id):
    library.return_book(book_id)
    flash('归还成功！')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)