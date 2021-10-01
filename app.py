from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    name = request.args.get("name", "world")
    return render_template("index.html", name=name)


if __name__ == '__main__':
    app.run()
