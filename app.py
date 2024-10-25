import sqlite3
import pyodbc
import random
from flask import Flask, session, render_template, request, g

app = Flask(__name__)

'''
Ivo

if __name__ == '__main__':
    app.run(debug=True)
'''

app.secret_key = "manbearpig_MUDMAN888"
app.config["SESSION_COOKIE_NAME"] = "myCOOKIE_twx"

@app.route("/", methods=["POST", "GET"])
def index():
    session["all_items"], session["shopping_items"] = get_db()
    return render_template("index.html", all_items=session["all_items"],
                                         shopping_items=session["shopping_items"])

@app.route("/add_items", methods=["post"])
def add_items():
    session["shopping_items"].append(request.form["select_items"])
    session.modified = True
    return render_template("index.html", all_items=session["all_items"],
                                         shopping_items=session["shopping_items"])

@app.route("/remove_items", methods=["post"])
def remove_items():
    checked_boxes = request.form.getlist("check")

    for item in checked_boxes:
        if item in session["shopping_items"]:
            idx = session["shopping_items"].index(item)
            session["shopping_items"].pop(idx)
            session.modified = True

    return render_template("index.html", all_items=session["all_items"],
                                         shopping_items=session["shopping_items"])

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = pyodbc.connect(driver='{SQL Server}',
                               server='SRVMOD\TWINTEX2008R2',
                               database='Tutor_TWX_testes',
                               uid='sa',pwd='TWXsql#05')
        
        cursor = db.cursor()
        cursor.execute("select nome from teste")
        all_data = cursor.fetchall()
        all_data = [str(val[0]) for val in all_data]

        shopping_list = all_data.copy()
        random.shuffle(shopping_list)
        shopping_list = shopping_list[:5]
    return all_data, shopping_list

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run()