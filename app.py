from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

app = Flask(__name__)

# flask-restxの設定
app.config['RESTX_MASK_SWAGGER'] = False
api = Api(app, version='1.0', title='Sample API', description='A sample API')

# Flask-SQLAlchemyの設定
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1/my_schema?charset=utf8mb4'
db = SQLAlchemy(app)

# Flask-Migrateの設定
migrate = Migrate(app, db)

# 別ファイルをインポートする
from routes.user import user_module
app.register_blueprint(user_module)
