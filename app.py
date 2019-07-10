#!/usr/bin/env python

from flask import Flask
from flask import request,render_template
app = Flask(__name__)

from jinja2 import Template

@app.route('/jinjas/', strict_slashes=False)
def jin_ja():
    return render_template('index.html')


@app.route('/API/jinja/', strict_slashes=False, methods=['GET','POST'])
def jinjaapi():
    from jinja2 import Template
    data = request.get_data().decode('utf-8')

    data = data.replace('\n','')
    tem = Template(data)
    return tem.render()

if __name__ == '__main__':
    app.run(host='10.39.10.215', port=9999, debug=True)


