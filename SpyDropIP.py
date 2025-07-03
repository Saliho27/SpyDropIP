from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "مرحبًا بك في أداة بايثون الخاصة بي على GitHub!"

if __name__ == '__main__':
    app.run(debug=True)