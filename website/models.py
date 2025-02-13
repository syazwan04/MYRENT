from . import db #it import current package the db object
from flask_login import UserMixin #module for log in and infeherent from user
from sqlalchemy.sql import func 

class Note(db.Model): #this just layout for  loop print for object to store in database
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # this always store id in user class user , one user can have many Note



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # when create the object in database need PK
    email =  db.Column(db.String(150), unique=True) # create for prevent user create same email 
    password = db.Column(db.String(150))
    firstName =  db.Column(db.String(150))
    notes = db.relationship('Note')# tell sql to create user relation add note ID


#for rent user page.
class RentUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pdf_preview = db.Column(db.String(150))  # Store PDF preview image path
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    status = db.Column(db.String(50))
    overdue = db.Column(db.Boolean, default=False)
    file_name = db.Column(db.String(150))
    note = db.Column(db.String(10000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# for News Dashboard
class NewsUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    content = db.Column(db.Text)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    pdf_file = db.Column(db.String(150))

#for report user page
class ReportUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150))
    request = db.Column(db.Text)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#for faq user to view
class FAQ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200))
    answer = db.Column(db.Text)