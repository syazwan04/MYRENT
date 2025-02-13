from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager



db=SQLAlchemy()
DB_NAME='database.db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'  # This first
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_NAME}'
    db.init_app(app)


    print("Secret key:", app.config['SECRET_KEY'])

    #do imports later
    from .views import views
    from .auth import auth


    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Note #to make sure it run the python file to define the class and create database

    create_database(app)

    login_manager=LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app): #purpose for create nonexistent database without duplicate
    if not path.exists('website/'+ DB_NAME):
        with app.app_context():    # Using context manager
            db.create_all()        # No app parameter needed
        print('Created Database!')