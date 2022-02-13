from flask import Flask

app = Flask(__name__)
# ---start
@app.route("/")
def hello_world():
    return "<p>Hello, Luyao</p>"


# ---end
if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)