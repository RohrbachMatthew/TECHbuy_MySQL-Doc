"""
Connection Test for MySLQ TECHbuy Database
-Use this to view the database and make sure information on page aligns with information
seen on the page.

1. pip install mysql-connector-python
2. pip install tabulate
3. run
4. Should connect to the database and Display the Products table
* Ignore the configuring data sources warning.
"""

import mysql.connector
from tabulate import tabulate

connection = mysql.connector.connect(
    host='sql5.freesqldatabase.com',
    user='sql5764068',
    password='CjiQ9eFlZQ',
    database='sql5764068'
)

cursor = connection.cursor()
cursor.execute("""Select * FROM products ORDER BY category""")

rows = cursor.fetchall()

headers = ['ProductID', 'Serial Number', 'Name', 'Category', 'Price', 'Manufacturing Cost', 'Quantity']

print(tabulate(rows, headers=headers, tablefmt='grid'))

cursor.close()
connection.close()