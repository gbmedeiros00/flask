from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/contato")
def contato():
    return render_template('contato.html')

@app.route("/quemsomos")
def quemsomos():
    return render_template('quemsomos.html')

if __name__ == "__main__":
    app.run(debug=True)