#!/usr/bin/python

from bottle import route, run, request
import html

@route('/')
def hello(username=''):  # 変数user使ってないので、usernameのはず(ここではどちらでも問題ないと思うが)
    username = request.query.get('user')
    username = '' if username is None else username
    username = html.escape(username)     # 追加されたコード

    # 変数名が変わったのは、htmlモジュールを使っており、htmlという変数名を使いたくないから
    body = "<h2> Hello {name} </h2>".format(name=username)

    return body

run(host='0.0.0.0', port=8080, debug=True)