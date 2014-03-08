from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask import render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return 'User:%s, Email:%s' %(self.username, self.email)

@app.route('/users', methods=['GET'])
def get_users():
	users = User.query.all()
	return render_template('challenge4.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)