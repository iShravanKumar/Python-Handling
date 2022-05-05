import mysql.connector
import pandas
from log_generator import logging
from database_handler import CRUD
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

crud = CRUD()
database_name = 'fakestore'
table_name = 'data'


@app.route('/')
@app.route('/index', methods=["GET", "POST"])
def index():
    return render_template("Index.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST" and request.files:
        csv_file = request.files["file"]
        csv_dataframe = pandas.read_csv(csv_file)
        try:
            mydb, check = crud.establish_connection('shravan', 'Vvu8z9D')
            if not check:
                raise mysql.connector.Error
            command = "CREATE TABLE fakestore.data (" \
                      "`ID` int NOT NULL," \
                      "`TITLE` varchar(300) DEFAULT NULL," \
                      "`PRICE` decimal(20,2) DEFAULT NULL," \
                      "`DESCRIPTION` varchar(3000) DEFAULT NULL," \
                      "`CATEGORY` varchar(150) DEFAULT NULL," \
                      "`IMAGE` varchar(500) DEFAULT NULL," \
                      "`RATING_RATE` decimal(5,2) DEFAULT NULL," \
                      "`RATING_COUNT` int DEFAULT NULL," \
                      "PRIMARY KEY (`ID`))"
            if not crud.create_table(mydb, database_name, table_name, command):
                raise mysql.connector.Error

            command = "INSERT INTO fakestore.data " \
                      "(ID, TITLE, PRICE, DESCRIPTION, CATEGORY, IMAGE, RATING_RATE, RATING_COUNT) " \
                      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            data_list = []
            for i, rows in csv_dataframe.iterrows():
                data_list.append(tuple(rows))
            if not crud.insert_values(mydb, database_name, table_name, command, data_list):
                raise mysql.connector.Error

        except mysql.connector.Error:
            print("MySQL ERROR, Program Terminate")

        except Exception as error:
            print("Unknown ERROR, Program Terminate")
            logging.error('Unknown Error, ', error)

        return redirect("/index")
    return render_template("Upload.html")


if __name__ == "__main__":
    app.run(host="localhost", port=int("5000"))

'''
Update:
    SELECT primary_key from TABLE
    Save to list primary_key_list
    HTML FORM
        Drop Down primary_key_list
        Fill New Values
    UPDATE TABLE with HTML FORM
    
Delete:
    SELECT primary_key from TABLE
    Save to list primary_key_list
    HTML FORM
        Drop Down primary_key_list
    DELETE FROM TABLE WHERE column=primary_key_list_item from HTML FORM
'''