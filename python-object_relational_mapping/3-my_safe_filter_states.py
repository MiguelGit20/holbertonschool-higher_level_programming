#!/usr/bin/python3
"""
SQL Injection...
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute(
        """ SELECT *
            FROM states
            WHERE name LIKE BINARY %s
            ORDER BY id ASC""", (str(argv[4]),))

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    db.close()
