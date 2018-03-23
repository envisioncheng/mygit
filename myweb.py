import datetime
from flask import Flask,render_template,request
app=Flask(__name__)
app.debug = True
# app.config['DEBUG'] = True

@app.route("/")
def index():
    # return "hello,word  again  aa qq"
    names=["a","b","c"]
    return render_template("index.html",test=datetime.datetime.now(),names=names)

@app.route("/<string:name>")
def dav(name):
    return f"<h1>hello,word {name} g2</h1>"

@app.route("/more")
def more():
    return render_template("more.html")

@app.route("/hello", methods=["POST"])
def hello():
    name=request.form.get("name")
    return render_template("hello.html",name=name)

if __name__=="__main__":
    app.run()
