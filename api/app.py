from flask import Flask
from api.database import db
from .views.item import item
import config


app = Flask(__name__)
# DB設定を読み込む
app.config.from_object('config.Config')
db.init_app(app)
app.register_blueprint(item, url_prefix='/item')
#    return app
#app = create_app()