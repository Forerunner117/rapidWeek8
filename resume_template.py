from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/resume/<name>')
def hello(name=None):
    return render_template('resume.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)