from flask import Flask

app = Flask(__name__)


@app.route("/")
def groot():
  return "<h1>We are GROOT</h1>"


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
