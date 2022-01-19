from flask import Flask, render_template, request
import sqlite3
app=Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/addstudent',methods = ['POST', 'GET'])
def addstudent():
   if request.method == 'POST':


         con = sqlite3.connect('StudentInfo.db')

         def sql_insert(con):
             first_name = request.form['first_name']
             last_name = request.form['last_name']
             gender = request.form['gender']
             grade = request.form['grade']
             cursorObj = con.cursor()
             cur = con.cursor()
             cursorObj.execute("INSERT INTO student_db (first_name,last_name,gender,grade) VALUES('"+first_name+"', '"+last_name+"', '"+gender+"','"+grade+"')")

             con.commit()


         sql_insert(con)

         return render_template("home.html")


@app.route('/getList')
def getList():
   con = sqlite3.connect("StudentInfo.db")
   con.row_factory = sqlite3.Row

   cur = con.cursor()
   cur.execute("select * from student_db")

   rows = cur.fetchall();
   return render_template("results.html",rows = rows)


@app.route('/studentsPass')
def studentsPass():
   con = sqlite3.connect("StudentInfo.db")
   con.row_factory = sqlite3.Row

   cur = con.cursor()
   cur.execute("select * from student_db where grade >=85")

   rows = cur.fetchall();
   return render_template("results.html",rows = rows)


@app.route('/deleteRecord',methods = ['POST', 'GET'])
def deleteRecord():
   if request.method == 'POST':

         con = sqlite3.connect('StudentInfo.db')
         id  = request.form['id']
         cursorObj = con.cursor()
         cur = con.cursor()
         cursorObj.execute("DELETE FROM student_db where id="+id+"")
         con.commit()
   return render_template("home.html")


@app.route('/updateRecord',methods = ['POST', 'GET'])
def updateRecord():
   if request.method == 'POST':


         con = sqlite3.connect('StudentInfo.db')
         gd = request.form['grade']
         id  = request.form['id']
         cursorObj = con.cursor()
         cur = con.cursor()
         cursorObj.execute('UPDATE student_db SET grade = ? where id =?;',(gd,id))
         con.commit()

   return render_template("home.html")
if __name__=='__main__':
     app.run(debug=True)


# References:
# https://www.youtube.com/watch?v=o-vsdfCBpsU
# https://bootniyas.wordpress.com/2014/07/23/student-record-app-using-flask/
# https://codeloop.org/flask-crud-application-with-sqlalchemy/
