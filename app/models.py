from . import db
import datetime

class Image(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  filename = db.Column(db.String(100), nullable=True, index=True)
  processed = db.Column(db.Boolean, default=True, index=True)
  upload_date = db.Column(db.DateTime)

  def __init__(self,filename):
    self.filename = filename
    self.processed = False
    self.upload_date = datetime.datetime.utcnow()

  def serialize(self):
    return {
      'id': self.id,
      'filename': self.filename,
      'processed': self.processed, 
      'upload_date': self.upload_date
    }