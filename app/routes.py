from app import app
from flask import render_template,flash,redirect,url_for,request
from .forms import LoginForm
from flask_login import current_user,login_user
from app.models import User,Pic,Confuse_Pic
from flask_login import login_required,logout_user
from werkzeug.urls import url_parse
from app import db
from app.forms import RegistrationForm
from app.STATICS import possible_verbs_explanations,to_anno,object_explain
from datetime import datetime
import json
from sqlalchemy import and_

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(student_id = form.student_id.data).first()
        if user is None:
            flash('您还未注册！请通过您的学号注册，便于我们发放补助')
            return redirect(url_for('login'))
        login_user(user)#,remember=form.remember_me.data)
        user.lastlogin = datetime.now()
        db.session.commit()
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc !='':
            next_page = (url_for('index'))
        return redirect(next_page)
    return render_template('login.html',
        title='登陆',form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(student_id=form.student_id.data,name=form.name.data, \
            contact=form.contact.data)
        db.session.add(user)
        db.session.commit()
        flash('恭喜您注册成功！')
        return redirect(url_for('login'))
    return render_template('register.html',title='Register',form=form)


@app.route('/annotation',methods=['GET','POST'])
@login_required
def annotation():#annos:标注来的checklist,anno:000010001格式的标注数据
    if request.method=="POST":#接收用户标记好的数据
        annos = request.form.getlist('anno')
        pic_id = request.form.getlist('picid')
        problem = request.form.getlist('problem')
        print(annos,pic_id,problem)
        annotate(annos,problem,pic_id)
    pic = Pic.query.filter_by(annotating_id=current_user.id).first()
    if pic is None:
        pic = Pic.query.filter(and_(Pic.user1_id != current_user.id, \
            Pic.user2_id != current_user.id)).filter(Pic.status == '待标注').first()
    if pic is None:
        return render_template('finish.html',title=current_user.name,user=current_user)
    else:
        pic.status = '标注中'
        pic.annotating_id = current_user.id
        db.session.commit()
        print('---新图提取---',pic)
        verbs = possible_verbs_explanations(pic.object_type)
        return render_template('annotation.html',pic=pic,verbs=verbs, \
            object_explain=object_explain(pic.object_type),title=current_user.name)

def is_valid_anno(annos,problem):#后端逻辑判断本次标注是否合法
    if len(problem)>0:
        result = True
    else:
        if len(annos)==0:
            flash('请至少选择一项')
            result = False
        elif ('not_interacting_with' in annos) and len(annos)>1:
            flash('【无交互】与其他选项互斥')
            result = False
        else:
            result = True
    return result

def annotate(annos,problem,pic_id):
    if is_valid_anno(annos,problem):
        pic = Pic.query.filter_by(id=int(pic_id[0])).first()
        user = User.query.filter_by(id=current_user.id).first()
        user.count +=1
        #----先写入problem------
        if 'er' in problem:
            pic.label_error = True
        if 'un' in problem:
            pic.unknown = True
        #-----首次标注----------
        if pic.anno1 is None:
            pic.anno1 = to_anno(annos)
            pic.user1_id = current_user.id
            pic.annotating_id = None
            pic.status = "待标注"
        #-----第二次标注--------
        elif pic.anno2 is None:
            pic.anno2 = to_anno(annos)
            pic.user2_id = current_user.id
            pic.annotating_id = None
            if pic.label_error or pic.unknown:
                pic.status = "有问题"
            elif pic.anno1 == pic.anno2:
                pic.status = "已完成"
            else:
                pic.status = "待标注"
        #-----第三次标注-------
        else:
            pic.anno3 = to_anno(annos)
            pic.user3_id = current_user.id
            pic.annotating_id = None
            if pic.anno3 == pic.anno2 or pic.anno3 == pic.anno1:
                pic.status = "已完成"
            elif pic.confuse:
                pic.status = "难判断"
            else:
                pic.confuse = True
                confuse_pic = Confuse_Pic(pic_id=pic.id,pic_name=pic.pic_name, \
                    anno1=pic.anno1,anno2=pic.anno2,anno3=pic.anno3)
                db.session.add(confuse_pic)
                pic.anno1,pic.anno2,pic.anno3 = [None,None,None]
                pic.user1_id,pic.user2_id,pic.user3_id = [0,0,0]
                pic.status = "待标注"
        db.session.commit()



