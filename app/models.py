from . import db
from sqlalchemy_imageattach.entitiy import Image,image_attachment

class RawImage(db.Model, Image):
  __tablename__ = 'raw_image'

  id = db.Column(db.Integer, primary_key=True)
  original_filename = db.Column(db.String(100), nullable=True)
  upload_date = db.Column(db.DateTime)

class ProcessedImage(db.Model, Image):
  __tablename__ = 'processed_image'

  id = db.Column(db.Integer, primary_key=True)
  original_filename = db.Column(db.String(100), nullable=True)
  upload_date = db.Column(db.DateTime)