from flask import Flask, render_template, request, redirect
import pandas
from database_handler import CRUD
import mysql.connector

app = Flask(__name__)


@app.route('/')
@app.route('/index', methods=["GET", "POST"])
def index():
    return render_template("Index.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST" and request.files:
        csv_file = request.files["file"]
        csv_dataframe = pandas.read_csv(csv_file)
        mydb = mysql.connector.connect(host="localhost", user="shravan", password="Vvu8z9D")
        database_cursor = mydb.cursor()
        command = "CREATE TABLE fakestore.flask_data (" \
                  "`ID` int NOT NULL," \
                  "`TITLE` varchar(300) DEFAULT NULL," \
                  "`PRICE` decimal(20,2) DEFAULT NULL," \
                  "`DESCRIPTION` varchar(3000) DEFAULT NULL," \
                  "`CATEGORY` varchar(150) DEFAULT NULL," \
                  "`IMAGE` varchar(500) DEFAULT NULL," \
                  "`RATING_RATE` decimal(5,2) DEFAULT NULL," \
                  "`RATING_COUNT` int DEFAULT NULL," \
                  "PRIMARY KEY (`ID`))"
        database_cursor.execute("DROP TABLE IF EXISTS fakestore.flask_data")
        database_cursor.execute(command)
        mydb.commit()
        command = "INSERT INTO fakestore.flask_data " \
                  "(ID, TITLE, PRICE, DESCRIPTION, CATEGORY, IMAGE, RATING_RATE, RATING_COUNT) " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        for i, rows in csv_dataframe.iterrows():
            database_cursor.execute(command, tuple(rows))
            mydb.commit()

        return redirect("/view")
    return render_template("Upload.html")


@app.route('/view')
def table():
    mydb = mysql.connector.connect(host="localhost", user="shravan", password="Vvu8z9D")
    database_cursor = mydb.cursor()
    database_cursor.execute("SELECT * FROM fakestore.flask_data")
    result = database_cursor.fetchall()
    result_list = []
    for x in result:
        result_list.append(list(x))
    return render_template('fake_store.html', htmlList=result_list)


if __name__ == "__main__":
    app.run(host="localhost", port=int("5000"))
