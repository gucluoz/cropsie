from . import api
from ..models import RawImage, ProcessedImage
from flask import jsonify
from sqlalchemy.sql.expressions import func, select, limit


@api.route('/', methods=['GET'])
def return_random_image:
  pass