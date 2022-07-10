from flask import Flask, render_template, send_from_directory,url_for
import os

app = Flask(__name__)



@app.route('/')
def hello_world():  # put application's code here
    kwargs = {
        "page_title": "QCM01",
        "page_subtitle": "sous-titre",
        "question_number": "01",
        "question_text": "soso",
        "answer": [1, "fehn", "truc", "bibi"]
    }
    return render_template("mcq.html", **kwargs)  # kwargs better be well formatted !

    # return render_template("tmpl1.html", **kwargs) # kwargs better be well formatted !


if __name__ == '__main__':
    app.run()
