from app import db,login
from flask_login import UserMixin
#from datetime import datetime

class User(UserMixin,db.Model):
    __tablename__='user'
    id = db.Column(db.Integer,primary_key=True)
    student_id = db.Column(db.String(16),index=True,unique=True)
    name=db.Column(db.String(64),index=True)
    count = db.Column(db.Integer,default=0,index=True)
    contact = db.Column(db.String(64))
    lastlogin = db.Column(db.DateTime,index=True)

    def __repr__(self):
        return '<User {}>'.format(self.name)

class Pic(db.Model):
    __tablename__='pic'
    id = db.Column(db.Integer,primary_key=True)
    pic_name = db.Column(db.String(64),index=True,unique=True)
    object_type = db.Column(db.String(64))
    anno1 = db.Column(db.String(12))
    user1_id = db.Column(db.Integer,db.ForeignKey('user.id'),index=True,default=0)
    user1 = db.relationship('User',foreign_keys=[user1_id])
    anno2 = db.Column(db.String(12))
    user2_id = db.Column(db.Integer,db.ForeignKey('user.id'),default=0)
    user2 = db.relationship('User',foreign_keys=[user2_id])
    user3_id = db.Column(db.Integer,db.ForeignKey('user.id'),default=0)
    user3 = db.relationship('User',foreign_keys=[user3_id])
    anno3 = db.Column(db.String(12))
    status = db.Column(db.String(16),index =True)
    annotating_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    annotating = db.relationship('User',foreign_keys=[annotating_id])
    unknown = db.Column(db.Boolean,index=True,default=False)
    label_error = db.Column(db.Boolean,index=True,default=False)
    confuse = db.Column(db.Boolean,index=True,default=False)

    def __repr__(self):
        return '<Pic {},{},{},{},{}>'.format(self.pic_name,self.user1_id,self.user2_id,self.user3_id,self.status)

class Confuse_Pic(db.Model):
    __tablename__ = 'confuse'
    id = db.Column(db.Integer,primary_key=True)
    pic_id = db.Column(db.Integer,db.ForeignKey('pic.id'))
    pic = db.relationship('Pic',foreign_keys=[pic_id])
    pic_name = db.Column(db.String(64))
    anno1 = db.Column(db.String(12))
    anno2 = db.Column(db.String(12))
    anno3 = db.Column(db.String(12))
    
    def __repr__(self):
        return '<ConfusePic {},{},{},{}>'.format(self.pic_name,self.anno1,self.anno2,self.anno3)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))