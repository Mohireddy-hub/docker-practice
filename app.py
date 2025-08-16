from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from Flask!"

if __name__ == "__main__":
    # Important: tell Flask to listen on all interfaces and correct port
    app.run(host="0.0.0.0", port=8080, debug=True)
