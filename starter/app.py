import sqlite3
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)
DB_PATH = "blog.db"

def fetch_all_posts():
    with sqlite3.connect(DB_PATH) as con:
        con.row_factory = sqlite3.Row
        rows = con.execute(
            "SELECT id, title, content FROM posts ORDER BY id DESC;").fetchall()
    return [[r["id"], r["title"], r["content"]] for r in rows]

def fetch_post_by_id(post_id: int):
    with sqlite3.connect(DB_PATH) as con:
        con.row_factory = sqlite3.Row
        row = con.execute(
            "SELECT id, title, content FROM posts WHERE id = ?;",
            (post_id)
        ).fetchone()
    if row is None:
        return None
    return [row["id"], row["title"], row["content"]]

def post_detail(post_id):
    for p in posts:
        if p [0] == post_id:
            return p
    return None
    return render_template("post.html", post=post)

@app.route("/")
def hello():
    posts = fetch_all_posts()
    return render_template('index.html', posts=posts)

@app.route("/admin/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        brukernavn = "admin"
        passord = "admin123"

        if brukernavn == brukernavn and passord == passord:
            return redirect(url_for('admin_menu'))
        else:
            return render_template('/admin/login.html', feil=True)
    return render_template("admin/login.html")

@app.route("/admin/admin_menu")
def admin_menu():
    posts = fetch_all_posts()
    return render_template("/admin/admin_menu.html", posts=posts)

if __name__ == "__main__":
    app.run(debug=True)
