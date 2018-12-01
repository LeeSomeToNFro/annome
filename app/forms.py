from flask_wtf import FlaskForm as Form
from wtforms import StringField,BooleanField,SubmitField,IntegerField,SelectMultipleField
from wtforms.validators import DataRequired,ValidationError,EqualTo
from app.models import User

class LoginForm(Form):
    student_id = StringField('请输入您的学号进行登陆：',validators=[DataRequired()])
    #remember_me = BooleanField('记住我',default=False)
    submit = SubmitField("登陆")

class RegistrationForm(Form):
    student_id = StringField('*请输入您的学号',validators=[DataRequired()])
    student_id2 = StringField('*请重复输入您的学号',validators=[DataRequired(),EqualTo('student_id')])
    name = StringField('*请输入您的称呼',validators=[DataRequired()])
    contact = StringField('您可以留下联系方式，我们会在有需要的时候联系您')
    submit = SubmitField('注册')

    def validate_student_id(self,student_id):
        user = User.query.filter_by(student_id=student_id.data).first()
        if user is not None:
            raise ValidationError('您已经注册过啦！请直接登录吧~')

