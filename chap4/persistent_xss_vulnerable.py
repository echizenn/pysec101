#!/usr/bin/python

from bottle import route, run, request, redirect
import sqlite3

db_name = 'tasklist.db'
conn = sqlite3.connect(db_name)  # dbと接続
cursor = conn.cursor()           # db操作用のオブジェクトのようなもの

@route('/')
def hello(user=''):
    tasks = get_tasklist()

    html = "<h2>Persistent XSS Demo</h2>"
    html += "<form action='./' method='POST'>"
    html += "タスク名： <input type='text' name='name' /><br>"
    html += "内容： <input type='text' name='detail' /><br>"
    html += "<input type='submit' name='register' value='登録'/>"
    html += "</form>"
    html += tasks

    return html

@route('/', method='POST')
def register():
    name = request.forms.get('name')
    detail = request.forms.get('detail')

    sql_query = 'INSERT INTO tasklist values(?, ?)'
    cursor.execute(sql_query, (name, detail))   # nameとdetailをsqlに追加
    conn.commit()

    return redirect('/')

def get_tasklist():
    sql_query = 'SELECT * FROM tasklist'
    result = cursor.execute(sql_query)

    html = '<table border="1">'
    for row in result:
        html += '<tr><td>'
        # html +=  row[0].encode('utf-8')   versionの問題かもしれないが、encodeする必要がなさそう
        html += row[0]
        html +=  '</td><td>'
        # html +=  row[1].encode('utf-8')
        html += row[1]
        html += '</td></tr>'

    html += '</table>'
    return html

run(host='0.0.0.0', port=8080, debug=True)