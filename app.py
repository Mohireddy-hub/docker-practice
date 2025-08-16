# app.py
from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from Flask!"

if __name__ == "__main__":
    # Change here: host 0.0.0.0 and port 8080
    app.run(host="0.0.0.0", port=8080, debug=True)

