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

@api.route('/raw/<int:id>')
def return_raw_image(id):
  img = Image.query.filter_by(processed=False, id=id).first()
  if img:
    return jsonify(img.serialize())
  return 'not found',404

@api.route('/raw/', methods=['POST'])
def save_raw_image():
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
  else:
    return 'extension not allowed',500
  return 'unspecified error',500

@api.route('/processed/<int:id>', methods=['POST', 'GET'])
def save_processed_image(id):
  if request.method == 'GET':
    img = Image.query.filter_by(processed=True, id=id).first()
    if img:
      return jsonify(img.serialize())
    return 'not found',404

  f = request.files['file']
  if f and is_file_allowed(f.filename):
    raw_image = Image.query.filter_by(processed=False).first()
    if not raw_image:
      return 'raw image not found',500

    filename = secure_filename(f.filename)
    if(processed_file_exists(filename)):
      return 'file already exists',500

    f.save(os.path.join(current_app.config['IMAGE_DIR']+\
      current_app.config['IMAGE_PROCESSED_DIR_SUFFIX'], filename))

    raw_image.processed = True
    db.session.commit()

  return '',200
