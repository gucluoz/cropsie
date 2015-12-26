from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_name):
  app = Flask(__name__, 
    static_folder=config[config_name].IMAGE_DIR + \
      config[config_name].IMAGE_RAW_DIR_SUFFIX,
    static_url_path=config[config_name].STATIC_URL_PATH)
  app.config.from_object(config[config_name])
  config[config_name].init_app(app)

  db.init_app(app)

  from .api_v1 import api as api_v1_blueprint
  app.register_blueprint(api_v1_blueprint, url_prefix='/api/v1')

  from .web import web as web_blueprint
  app.register_blueprint(web_blueprint, url_prefix='/')

  return app