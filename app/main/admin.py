from flask import Flask
from app import app,db
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView 
from ..models import User,Post





# admin = Admin(app, name='Dashboard', template_mode='bootstrap3')

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))