# Primera app - endpoint api en flask

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hey flask toma por culi lask"

if __name__ == "__main__":
  app.run(debug=True)

