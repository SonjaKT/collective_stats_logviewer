from flask import render_template
from flask import Flask, request, jsonify, json
from model import db, app

def init_db():
    """ Initialize the database """
    db.create_all()


class _DefaultSettings(object):
    USERNAME = 'world'
    SECRET_KEY = 'development key'
    DEBUG = True


app.config.from_object(_DefaultSettings)
del _DefaultSettings

@app.route('/')
@app.route('/index/')
def index():
    data_store = {'reqs_sec': 1.74011, 'time_per_request': 0.2188, 'optimal_requests': 4.577, 'news': 38.88,
    'time_per_request': 2.46}
    return render_template("index.html", data=data_store)


@app.route('/reponse_time_details/', methods=['GET', 'POST'])
def response_time_details():
    url = "/newscenter/inthenewsview"

    data = [
       { "timestamp": "2013-02-18T20:18:15",
           "render_time": "0.7223",
       },
       { "timestamp": "2013-02-18T20:18:25",
           "render_time": "1.4157",
       },
       { "timestamp": "2013-02-18T20:21:14",
           "render_time": "4.567",
       }
    ]
    return jsonify(url=url, data=data)


@app.route('/super_url/', methods=['POST'])
def super_url():
	if request.method == 'POST':
		line = json.loads(request.json())["line"] 
		line_number = json.loads(request.json())["line_number"]	
		logs.do_it(line)
    return jsonify(["success %d" %(line_number)])
