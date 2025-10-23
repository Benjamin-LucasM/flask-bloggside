import sqlite3

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

print("Database laget!")