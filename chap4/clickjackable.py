#!/usr/bin/python

from bottle import route, run

@route('/')
def hello():
    html = '<h2>ターゲットのWebサイト</h2>'
    html += '<button type="button" value="button" '
    html += 'onclick="alert(\'商品Aを購入しました\')">'
    html += '商品Aを購入する</button>'
    return html

run(host='0.0.0.0', port=8000, debug=True)