# -*- coding: utf-8 -*-

# author:yield

import sqlite3

conn = sqlite3.connect('test.db')
print "Opened database successfully"
conn.execute("DROP TABLE dytt8;")
conn.execute('''CREATE TABLE dytt8 
    (name TEXT NOT NULL,
        url TEXT NOT NULL,
        download TEXT NOT NULL);''');

def add(item):
    sql = "INSERT INTO dytt8 (name, url, download) VALUES ('%s', '%s', '%s');"%(item['name'], item['url'], item['download'])
    conn.execute(sql)
    conn.commit()
    conn.close()
