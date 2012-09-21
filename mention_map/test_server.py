#!/usr/bin/python

import flask
import urllib2 as ul

app = flask.Flask(__name__)

@app.route('/')
def index():
	return 'This is a simple dev server. <br />site map:<br />'+reduce(lambda x,y: str(x)+'<br />'+str(y), app.url_map._rules)
	
@app.route('/count.json')
def count():
	time = flask.request.args.get('time', '0')
	d = ul.urlopen('http://twitwi.mit.edu:5000/count?time='+time)
	return d.read()

@app.route('/static/dat/times.json')
def times():
	d = ul.urlopen('http://twitwi.mit.edu:5000/static/dat/times.json')
	return d.read()
	
@app.route('/map')
def map():
	return flask.render_template('mention_map.html')

if __name__ == '__main__':
	app.run(debug=True)