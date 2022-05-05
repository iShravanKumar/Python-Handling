# Covered Concepts

- REST API
```Python
import requests
requests.get('url', params={'key':'value'})

# handle json response
from flatten_json import flatten
```

- [FILE GENERATING](Code/file_generator.py)
```Python
import pdfkit
import pandas
from json2xml import json2xml
```

- [DATA VISUALIZATION](Code/trending_crypto_charts.py)
```Python
import pandas
import matplotlib.pyplot as plt
```

- LOGGING

```Python
import logging
from datetime import date
logging.basicConfig(filename=f'Log-{date.today().strftime("%b-%d-%Y")}.log', level=logging.INFO)
```

- PyPI

- [Database CRUD Operations](Code/database_handler.py)
```Python
import mysql.connector
database_connection = mysql.connector.connect(host="localhost", user='user', password='password')
database_cursor = database_connection.cursor()
database_cursor.execute()
database_cursor.executemany()
database_connection.commit()
database_connection.close()
```

- PyUNIT
```Python
import unittest
class Test(unittest.TestCase):
    def __init__(self):
        None
    def setUp(self):
        None # pre testing set up
    def tearDown(self):
        None # end of tests execute
    def test_function(self):
        None # asserting tests
```

- [Zip/UnZip](Code/zip_handler.py)
```Python
import zipfile
```

- [SMTP EMail](Code/email_handler.py)
```Python
import os
import smtplib
from email.message import EmailMessage
# best practice to save authentication in environment variables
```
