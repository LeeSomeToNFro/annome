from app import db
from app.models import User,Pic
import glob
from flask import url_for
import json

'''PATH="D:\\_interaction\\annome\\app\\static\\pics"+"/*.json"
print(PATH)
filelist=glob.glob(PATH)
for fi in filelist:
    f = open(fi)
    jsobj = json.loads(f.read())
    pic_name=fi.split('\\')[-1].split('.')[0]
    #print(picname)
    object_type = jsobj['object']['type'].replace('-','_')
    status = '待标注'
    pic=Pic(pic_name=pic_name,object_type=object_type,status=status)
    db.session.add(pic)
db.session.commit()'''
pics = Pic.query.all()
for pic in pics:
    print(pic,pic.unknown,pic.label_error,pic.confuse,pic.anno1,pic.anno2,pic.anno3)