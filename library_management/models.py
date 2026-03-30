from database import connect_db
from datetime import datetime

# ---------- BOOK ----------

def add_book(title, author, quantity):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, quantity) VALUES (?, ?, ?)",
                   (title, author, quantity))
    conn.commit()
    conn.close()

def view_books():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    data = cursor.fetchall()
    conn.close()
    return data

def search_book(keyword):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE title LIKE ?", ('%' + keyword + '%',))
    data = cursor.fetchall()
    conn.close()
    return data

def delete_book(book_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()

# ---------- MEMBER ----------

def add_member(name, contact):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO members (name, contact) VALUES (?, ?)",
                   (name, contact))
    conn.commit()
    conn.close()

def view_members():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM members")
    data = cursor.fetchall()
    conn.close()
    return data

# ---------- TRANSACTION ----------

def issue_book(book_id, member_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT quantity FROM books WHERE id = ?", (book_id,))
    result = cursor.fetchone()

    if result and result[0] > 0:
        issue_date = datetime.now().strftime("%Y-%m-%d")

        cursor.execute("""
        INSERT INTO transactions (book_id, member_id, issue_date, status)
        VALUES (?, ?, ?, ?)
        """, (book_id, member_id, issue_date, "Issued"))

        cursor.execute("UPDATE books SET quantity = quantity - 1 WHERE id = ?", (book_id,))
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False

def return_book(transaction_id):
    conn = connect_db()
    cursor = conn.cursor()

    return_date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("""
    UPDATE transactions SET return_date = ?, status = 'Returned'
    WHERE id = ?
    """, (return_date, transaction_id))

    cursor.execute("SELECT book_id FROM transactions WHERE id = ?", (transaction_id,))
    book = cursor.fetchone()

    if book:
        cursor.execute("UPDATE books SET quantity = quantity + 1 WHERE id = ?", (book[0],))

    conn.commit()
    conn.close()

def view_transactions():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    data = cursor.fetchall()
    conn.close()
    return data