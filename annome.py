from app import app,db
from app.models import User,Pic

@app.shell_context_processor
def make_shell_context():
    return {'app':app,'db':db}

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080)