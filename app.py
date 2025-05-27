from flask import Flask

app=Flask(__name__)

@app.route('/')

def webout():

 return '<h1>DevOps is so much fun to learn now and more easy to learn now bca.</h1>'

app.run(host='0.0.0.0',port=7000)
