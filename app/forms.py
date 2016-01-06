__author__ = 'DD_2'
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required

class LoginForm(Form):
    openid = StringField('openid', validators = [Required()])
    remember_me = SubmitField('remember_me', default = False)