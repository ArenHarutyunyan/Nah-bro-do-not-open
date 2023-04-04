from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/credits')
def credits():
    return render_template('posts.html')

@app.route('/trailers')
def trailers():
    return render_template('trailers.html')

if __name__ == "__main__":
    app.run()
