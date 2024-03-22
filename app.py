import mysql.connector
from flask import Flask, render_template, redirect, request, g,  url_for

app = Flask(__name__)

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="AlphaOmega20",
            auth_plugin="mysql_native_password",
            database="Library",
        )
    return g.db

@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@app.route("/confirmation")
def confirmation():
    return render_template("confirmation.html")

# Display menu options
@app.route("/")
def display_index():
    return render_template("index.html")

# Display all books
@app.route("/all_books", methods=["GET"])
def display_all_books():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    sql = """
    SELECT b.Title, b.PublicationYear, b.InStock, a.AuthorName, p.PublisherName
    FROM Book b
    LEFT JOIN Writes w ON b.BookID = w.BookID
    LEFT JOIN Author a ON w.AuthorID = a.AuthorID
    LEFT JOIN Publisher p ON b.PublisherID = p.PublisherID
    """
    cursor.execute(sql)
    books = cursor.fetchall()
    cursor.close()
    return render_template("all_books.html", books=books)

@app.route("/search", methods=["GET"])
def display_search_form():
    return render_template("search.html")

# book search based on book name or author name
@app.route("/search", methods=["POST"])
def search_book():
    if request.method == "POST":
        search_query = request.form["search_query"]
        db = get_db()
        cursor = db.cursor()

        # search for books based on book title or author name
        sql = """
        SELECT b.Title, b.InStock, b.PublicationYear, a.AuthorName, p.PublisherName
        FROM Book b
        LEFT JOIN Writes w ON b.BookID = w.BookID
        LEFT JOIN Author a ON w.AuthorID = a.AuthorID
        LEFT JOIN Publisher p ON b.PublisherID = p.PublisherID
        WHERE b.Title LIKE %s OR a.AuthorName LIKE %s
        """
        val = ('%' + search_query + '%', '%' + search_query + '%')
        cursor.execute(sql, val)
        results = cursor.fetchall()
        cursor.close()

        if results:
            return render_template("search_result_book.html", results=results)
        else:
            return "No results found."

@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]

        db = get_db()
        cursor = db.cursor()
        sql = "INSERT INTO User_ (FirstName, LastName, UserStatus) VALUES (%s, %s, %s)"
        val = (first_name, last_name, "Active")  # Set user status as "Active" by default
        cursor.execute(sql, val)
        db.commit()
        cursor.close()

        return redirect(url_for("display_index"))  # Redirect back to the index page after adding the user

    return render_template("add_user.html")  # Render the form template


@app.route("/top_authors", methods=["GET"])
def top_authors():
    db = get_db()
    cursor = db.cursor()

    # SQL query to find top 5 most prolific authors
    sql = """
    SELECT a.AuthorID, a.AuthorName, COUNT(w.BookID) AS NumBooks, COUNT(DISTINCT b.PublisherID) AS NumPublishers
    FROM Author a
    JOIN Writes w ON a.AuthorID = w.AuthorID
    JOIN Book b ON w.BookID = b.BookID
    GROUP BY a.AuthorID
    ORDER BY NumBooks DESC
    LIMIT 5
    """
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)  # Print results

    if results:
        authors_info = []
        for result in results:
            author_id, author_name, num_books, num_publishers = result
            authors_info.append({
                "author_id": author_id,
                "author_name": author_name,
                "num_books": num_books,
                "num_publishers": num_publishers
            })
        return render_template("top_authors.html", authors_info=authors_info)
    else:
        return "No data found."

@app.route("/students_with_outstanding_payments")
def students_with_outstanding_payments():
    db = get_db()
    cursor = db.cursor()

    # select students with outstanding payments
    sql = """
    SELECT UserID, FirstName, LastName
    FROM User_
    WHERE UserID IN (
        SELECT DISTINCT UserID
        FROM Fine
        WHERE PaymentStatus = 'NOT PAID'
    )
    """
    cursor.execute(sql)
    students = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template("students_with_outstanding_payments.html", students=students)


if __name__ == "__main__":
    app.run(debug=True)