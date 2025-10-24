import sqlite3

connection = sqlite3.connect('blog.db')
cursor = connection.cursor()

with sqlite3.connect("blog.db") as con:
    con.executescript("""
    CREATE TABLE IF NOT EXISTS posts (
        id      INTEGER PRIMARY KEY AUTOINCREMENT,
        title   TEXT    NOT NULL,
        content TEXT    NOT NULL
    );

    INSERT INTO posts (title, content) VALUES  
        ("første innlegg", "Hei og velkommen til mini-bloggen!"),
        ("flask-tips", "bli bedre");
    """)

connection.commit()
connection.close()

print("Database laget!")