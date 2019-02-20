##
# SQLite3 is a very easy to use database engine. It is self-contained, serverless, zero-configuration and transactional.
# It is very fast and lightweight, and the entire database is stored in a single disk file.
# It is used in a lot of applications as internal data storage. The Python Standard Library 
# includes a module called "sqlite3" intended for working with this database.
# This module is a SQL interface compliant with the DB-API 2.0 specification
# download https://www.sqlite.org/download.html
#  https://www.guru99.com/sqlite-database.html
#  https://www.pythoncentral.io/introduction-to-sqlite-in-python/
#
import sqlite3

db = sqlite3.connect('D:\sqlite\sqlite-tools-win32-x86-3270100/testDb.db')

cursor = db.cursor()
cursor.execute('''SELECT Id, name FROM guru99''')
for row in cursor:
    # row[0] returns the first column in the query (name), row[1] returns email column.
    print('{0} : {1}'.format(row[0], row[1]))