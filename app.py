# import libraries
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.sql import func
from flask import redirect
from flask import request

# create object
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# class for database
class TaskManager(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(200), nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    date = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return f"{self.sno}-{self.title}"
    
# create routes
@app.route("/", methods=['GET','POST'])
def task_manager():
    if request.method == "POST":
        title= request.form['title']
        desc = request.form['desc']
        deadline = request.form['date']
        status = 0
        if deadline != '':
            date = datetime.strptime(deadline, '%Y-%m-%d').date()
            new_task = TaskManager(title = title, desc = desc, status = status, date=date)
        else:
            new_task = TaskManager(title = title, desc = desc, status = status)

        db.session.add(new_task)
        db.session.commit()

        return redirect("/")

    return render_template("index.html")
    
@app.route("/alltasks")
def all_tasks():
    assigned = TaskManager.query.filter_by(status = 0).all()
    completed = TaskManager.query.filter_by(status = 1).all()

    return render_template("table.html", assigned = assigned, completed = completed)

@app.route("/delete/<int:sno>")
def delete(sno):
    del_task = TaskManager.query.filter_by(sno= sno).first()
    db.session.delete(del_task)
    db.session.commit()

    return redirect("/alltasks")

@app.route("/update/<int:sno>", methods=['GET', 'POST'])
def update(sno):
    if request.method == "POST":
        upd_title = request.form['title']
        upd_desc = request.form['desc']
        upd_deadline = request.form['date']
        new_task = TaskManager.query.filter_by(sno = sno).first()
        new_task.title = upd_title
        new_task.desc = upd_desc 
        if upd_deadline != '':
            date = datetime.strptime(upd_deadline, '%Y-%m-%d').date()
            new_task.date = date

        db.session.add(new_task)
        db.session.commit()

        return redirect("/alltasks")


    old_task = TaskManager.query.filter_by(sno =sno).first()

    return render_template("update.html", old_task = old_task)

@app.route("/completed/<int:sno>")
def completed(sno):
    new_task = TaskManager.query.filter_by(sno = sno).first()
    new_task.status = 1

    db.session.add(new_task)
    db.session.commit()

    return redirect("/alltasks")

@app.route("/deleteall/<string:category>")
def deleteall(category):
    if category == 'assigned':
        assigned_tasks = TaskManager.query.filter_by(status= 0).all()
        for task in assigned_tasks:
            db.session.delete(task)
    
    elif category == 'completed':
        completed_tasks = TaskManager.query.filter_by(status= 1).all()
        for task in completed_tasks:
            db.session.delete(task)

    else :
        return redirect("/alltasks")
    
    db.session.commit()
    return redirect("/alltasks")

@app.route("/priortise")
def priortise():
    pass


@app.route("/about")
def about_text():
    return render_template("about.html")

# run from here...
if __name__ =="__main__":
    app.run(debug=True, port=8000)


