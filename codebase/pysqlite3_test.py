#!/usr/bin/env python
#-*- coding:utf-8 -*-

import json
import requests

import pysqlite3

# randomuser.me generates random 'user' data (name, email, addr, phone number, etc)
r = requests.get('http://api.randomuser.me/0.6/?nat=us&results=10')
j = r.json()['results']




data_list = []
for rec in j:
    user = rec['user']
    name = user['name']

    key = user['registered']
    fname = name['first']
    lname = name['last']
    email = user['email']
    da = (key,fname,lname,email)
    data_list.append(da)

# absolute path
with pysqlite3.Database('users.db') as db:
    # db.write('DROP TABLE IF EXISTS persons2')
    # db.write('CREATE TABLE persons2 (key int PRIMARY KEY, fname text, lname text, email text)')
    # sql1 = '''INSERT INTO persons2 (key, fname, lname, email) VALUES(?,?,?,?)'''
    # db.insert(sql1,[(123,'jason','li','jason@126.com')])
    rows = db.query('SELECT * FROM persons2')
    print(rows.export('xls'))

# 

# db = Database('users.db')
# d = db.query('SELECT * FROM persons limit 10')
# print(d.as_list(has_header=False))
# db.close()

