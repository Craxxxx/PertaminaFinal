#from . equivalent using website
from . import db
from flask_login import UserMixin
from sqlalchemy.ext.associationproxy import association_proxy
#MODEL FOR DATABASE AND TO INITIATE DATABASE

#NO LONGER USED
#ASSOCIATION TABLE
# user_cctv = db.Table('user_cctv',
#     db.Column('user_id',db.Integer,db.ForeignKey('user.id')),
#     db.Column('CCTV_id',db.Integer,db.ForeignKey('cctv.id'))
# )
#ASSOCIATION TABLE
#NO LONGER USED


#ASSOCIATION CLASS
class UserCCTV(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id')) #user_id column
    cctv_id = db.Column('cctv_id', db.Integer, db.ForeignKey('cctv.id')) #CCTV_id column
    date_followed = db.Column(db.DateTime)
    
    #RELATIONS
    # points back to cctv   UserTable
    user = db.relationship('User', back_populates='cctv_association')
    #points back to cctv

    #points back to user    CCTVtable
    cctv = db.relationship('CCTV', back_populates='users')
    #points back to user
    #RELATIONS
#ASSOCIATION CLASS

#MODEL UNTUK USER
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True)
    # email = db.Column(db.String(100), unique=True)
    username   = db.Column(db.String(100), unique=True)
    password   = db.Column(db.String(100))
    permission = db.Column(db.String(200))

    #RELATIONSHIP WITH THE cctv TABLE USING THE UserCCTV TABLE
    cctv_association = db.relationship('UserCCTV', back_populates='user')

    #association proxt skipping cctv_association and go directly to users
    cctvs             = association_proxy("cctv_association","cctv")
    
    #RELATIONSHIP WITH THE cctv TABLE USING THE UserCCTV TABLE
    
    #NO LONGER USED
    #SQLALCHEMY ORM
    # subscribed = db.relationship('CCTV', secondary=user_cctv) 
    #SQLALCHEMY ORM
    #NO LONGER USED
#MODEL UNTUK USER

#MODEL UNTUK CCTV
class CCTV(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hostname = db.Column(db.String(200))
    name_cctv = db.Column(db.String(100), unique=True)
    link_cctv = db.Column(db.String(200), unique=True)
    brand_cctv = db.Column(db.String(200))
    
    #RELATIONSHIP WITH THE USER TABLE USING THE UserCCTV table
    users = db.relationship('UserCCTV', back_populates='cctv')
    #RELATIONSHIP WITH THE USER TABLE USING THE UserCCTV table
#MODEL UNTUK CCTV

#MODEL FOR DATABASE AND TO INITIATE DATABASE



