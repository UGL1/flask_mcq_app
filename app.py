from flask import Flask, render_template, send_from_directory, url_for
import os

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    kwargs = {
        "page_title": "QCM01",
        "page_subtitle": "sous-titre",
        "questions": [
            {
                "question_number": "01",
                "question_text": """<pre><code class="python-code">
def f(x : int) -> int:
    return x ** 2 + 2 * x + 1</code></pre>""",
                "answer": [1, "fehn", "truc", "bibi"]
            },
            {
                "question_number": "02",
                "question_text": """<pre><code class="python-code">
print(f"Salut {codo}")</code></pre>""",
                "answer": ["popo", "fehn", "truc", "bibi"]
            },
            {
                "question_number": "03",
                "question_text": "caoiuoiuc",
                "answer": ["popo", "fehn", "truc", "bibi"]
            },
            {
                "question_number": "04",
                "question_text": "caoiuoiuc",
                "answer": ["popo", "fehn", "truc", "bibi"]
            },
            {
                "question_number": "05",
                "question_text": "caoiuoiuc",
                "answer": ["popo", "fehn", "truc", "bibi"]
            },
        ]
    }
    return render_template("mcq2.html", **kwargs)  # kwargs better be well formatted !

    # return render_template("tmpl1.html", **kwargs) # kwargs better be well formatted !


# @app.route('/')
# def hello_world():  # put application's code here
#     kwargs = {
#         "page_title": "QCM01",
#         "page_subtitle": "sous-titre",
#         "question_number": "01",
#         "question_text": "soso",
#         "answer": [1, "fehn", "truc", "bibi"]
#     }
#     return render_template("mcq.html", **kwargs)  # kwargs better be well formatted !
#
#     # return render_template("tmpl1.html", **kwargs) # kwargs better be well formatted !


if __name__ == '__main__':
    app.run()
