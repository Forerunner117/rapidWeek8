from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Austin Longo - Rapid Prototyping 2014 Rules!!'

@app.route('/find', methods=['GET'])
def find_response():
	searchword = request.args.get('class', '')
	if(searchword == 'CSCI1300'):
		return 'Find the classroom for %s... ATLAS 100' %searchword
	elif(searchword == 'CSCI2240'):
		return 'Find the classroom for %s... ITLL 1B50'  %searchword
	else:		
   		return 'Find the classroom for %s... Sorry. No result for %s' %(searchword, searchword)

@app.route('/notification')
def notification_response():
    return 'Get notification. To be implemented...'

if __name__ == '__main__':
    app.run(debug=True)