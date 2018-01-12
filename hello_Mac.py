from flask import Flask, render_template

from flask.ext.bootstrap import Bootstrap

app= Flask (__name__)

@app.route ('/')

def home ():

     return render_template("home.html")

@app.route ('/about')

def about ():

     return redirect('http://www.bbc.com')

if __name__ =="__main__":
     app.run (debug = True)
