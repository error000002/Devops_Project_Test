from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Aditya...!! How's your test project is going ?"

if __name__ == "__main__":
    app.run(debug=True)
