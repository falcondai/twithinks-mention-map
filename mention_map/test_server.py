#!/usr/bin/python

import flask
import urllib2 as ul

app = flask.Flask(__name__)

@app.route('/')
def hello():
	return 'This is a simple dev server.'
	
@app.route('/count.json')
def count():
	time = flask.request.args.get('time', '0')
	d = ul.urlopen('http://twitwi.mit.edu:5000/count?time='+time)
	return d.read()
	
@app.route('/map')
def map():
	return flask.render_template('mention_map.html')

if __name__ == '__main__':
	app.run(debug=True)