from . import web
from flask import render_template

@web.route('/')
def index():
  return render_template('index.html.j2')

@web.route('upload/', methods=['GET', 'POST'])
def upload():
  return render_template('upload.html.j2')