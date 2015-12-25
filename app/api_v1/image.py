from . import api
from ..models import Image
from flask import jsonify, request, current_app
from sqlalchemy.sql.expression import func
from werkzeug import secure_filename
from .. import db
import os

def is_file_allowed(filename):
  lower_filename = filename.lower()
  return '.' in lower_filename and \
    lower_filename.rsplit('.',1)[1] in current_app.config['ALLOWED_EXTENSIONS']

def raw_file_exists(filename):
  return Image.query.filter_by(processed=False, filename=filename).first() != None

@api.route('/raw/', methods=['GET'])
def return_random_image():
  img = Image.query.filter_by(processed=False).order_by(func.random()).limit(1).first()
  if img:
    return jsonify(img.serialize())
  return 'not found',404

@api.route('/raw/<name>')
def return_raw_image(name):
  img = Image.query.filter_by(processed=False, filename=name).first()
  if img:
    return jsonify(img.serialize())
  return 'not found',404

@api.route('/raw/', methods=['POST'])
def save_processed_image():
  f = request.files['file']
  if f and is_file_allowed(f.filename):
    filename = secure_filename(f.filename)
    while(raw_file_exists(filename)):
      filename = '_' + filename
    f.save(os.path.join(current_app.config['IMAGE_DIR']+\
      current_app.config['IMAGE_RAW_DIR_SUFFIX'], filename))

    img = Image(filename)
    db.session.add(img)
    db.session.commit()

  return '',200
