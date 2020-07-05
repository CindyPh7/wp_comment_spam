#!/usr/bin/python3


import sys
import mysql.connector
from mysql.connector import Error

# Connect to database from credentials typed in params
db = mysql.connector.connect(user=sys.argv[1], password=sys.argv[2], host=sys.argv[3], database = sys.argv[4])

db_cursor = db.cursor()


# Select query to check number of comments posted in the last 4 hours
db_cursor.execute("SELECT COUNT(c.comment_date) FROM wp_comments as c where hour(timediff( localtime(), c.comment_date ) ) < 4;")

result = db_cursor.fetchall()


for nb_comment in result:
    string = " durant les 4 dernières heures"
    if int(nb_comment[0]) >= int(sys.argv[5]):
        print("WARNING: Il y a eu plus de %s commentaires" % (sys.argv[5]) + string)
    elif int(nb_comment[0]) >= int(sys.argv[6]):
        print("CRITICAL: Il y a eu plus de %s commentaires" % (sys.argv[6]) + string)
    else:
        print("OK: Pas plus de %s commentaires" % (sys.argv[5]) + string)

print("Hello %s" % (sys.argv[0]))
