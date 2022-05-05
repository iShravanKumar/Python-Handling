import requests
from flatten_json import flatten
from flask import Flask, render_template
import mysql.connector

strReq = "https://fakestoreapi.com/products"
response = requests.get(strReq)
prodList = xmlCopy = response.json()
htmlCopy = []
for x in prodList:
    htmlCopy.append(flatten(x))

mydb = mysql.connector.connect(host="localhost", user="shravan", password="Vvu8z9D")
database_cursor = mydb.cursor()
database_cursor.execute("SELECT * FROM fakestore.flask_data")
result = database_cursor.fetchall()
for x in result:
    print(x)
print(list(result))
print(htmlCopy)

app = Flask(__name__)


@app.route('/')
def table():
    return render_template('fake_store.html', htmlList=htmlCopy)


if __name__ == "__main__":
    app.run(host="localhost", port=int("5000"))
