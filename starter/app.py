
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/post/<int:post_id>")
def post_detail(post_id):
    for p in posts:
        if p [0] == post_id:
            return p
    return None
    return render_template("post.html", post=post)

@app.route("/")
def hello():
    posts = [[1, "hei", "testtekst adhaidhaidchaisdcja aidcjias jaidcja"], [2, "title", "content_html"], [3, "title", "content_html"], [4, "title", "content_html"]]
    return render_template('index.html', posts=posts)

if __name__ == "__main__":
    app.run(debug=True)
