# -*- coding: utf-8 -*-
from flask import Flask, request
from flask import render_template
from model import TodoItem
from model import db
from flask import redirect, url_for

class _DefaultSettings(object):
    USERNAME = 'world'
    SECRET_KEY = 'development key'
    DEBUG = True


# create the application
app = Flask(__name__)
app.config.from_object(_DefaultSettings)
del _DefaultSettings


def init_db():
    """ Initialize the database """
    db.create_all()

@app.route('/')
def index():
    todo_list = TodoItem.query.all()
    return render_template('hello.html', todos=todo_list)


@app.route('/add', methods=['POST',])
def add_todo():
    if 'todo_item' in request.form:
        todo = TodoItem(description=request.form['todo_item'])
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('index'))
    return "Unknown Error"