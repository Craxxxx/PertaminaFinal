from flask import Flask , redirect
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_migrate import Migrate
from flask_login import LoginManager

# config the sqlalchemy
db = SQLAlchemy()
DB_NAME = "pertamina"
# config the sqlalchemy

# CREATING THE FLASK APP
def create_app():
    # CONFIG THE APP
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'SI2020'
    #CONNECT THE DATABASE
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:@localhost:3306/{DB_NAME}'
    #CONNECT THE DATABASE
    
   

    # create an instance of the database module
    #INITIALIZE SQLALCHEMY APPLICATION AS THE CURRENT APP
    db.init_app(app) # use this db as the app 
    #INITIALIZE SQLALCHEMY APPLICATION AS THE CURRENT APP
    #CONFIG THE APP

    #CREATE MIGRATION
    migrate = Migrate(app,db)
    #CREATE MIGRATION

    
    # REGISTER THE BLUEPRINT
    # import the views function from views file
    from .views import views
    from .auth import auth
    from .playvid import playvid
    from .playvid2 import playvid2
    from .playvid3 import playvid3
    # import the views function from views file
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/') # prefixes if '/auth/' you have to go to auth and then slash and then whatever the name of the view inside the py files 
    app.register_blueprint(playvid, url_prefix='/')
    app.register_blueprint(playvid2, url_prefix='/')
    app.register_blueprint(playvid3, url_prefix='/')
    # REGISTER THE BLUEPRINT

    from .models import User,CCTV
    
    #CREATE TABLE IF NOT EXIST
    with app.app_context():
        db.create_all()
    #CREATE TABLE IF NOT EXIST
    
    #LOGIN MANAGER
    login_manager = LoginManager()
    #if not login go here
    login_manager.login_view = 'auth.login'
    #if not login go here   
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    #LOGIN MANAGER

   
    
    # There is no need for that create_database function. SQLAlchemy will already not overwrite an existing file, 
    # and the only time the database wouldn't be created is if it raised an error.

    #CREATE DATABASE IF PATH NOT 
    #create_database(app) #app is to tell create the database for this app
    #CREATE DATABASE IF PATH NOT EXIST

    return app
# creating the flask app

#CREATE THE DATABASE
# def create_database(app):
#     if not path.exists('website/' + DB_NAME):
#         db.create_all(app=app)
#         print('Created Database!')

# Flask-SQLAlchemy 3 no longer accepts an app argument to methods like create_all. Instead, 
# it always requires an active Flask application context.