from flask import Flask
from flask import render_template

app = Flask(__name__)

subtitle = "This is Austin Longo's Flask + Jinja page!"
navigation = [{'href': 'http://www.austinlongo.com', 'caption': "Austin Longo"},
	 		  {'href': 'http://www.sochi.ru', 'caption': "Sochi"}, 
			  {'href': 'http://www.xkcd.com', 'caption': "xkcd"}
			]


@app.route('/home')
def hi():
	return render_template('minimal_template_bootstrap.html', subtitle=subtitle, navigation=navigation)

#@app.route('/hello/<name>')
#def hello(name=None):
#    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)