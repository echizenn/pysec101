#!/usr/bin/python

from bottle import route, run

@route('/hello')
def index():  # nameを定義しておらずエラー出るので消しました
    return '<h1>Hello</h1>'

run(host='0.0.0.0', port=8080)