from flask import Flask
from flask import render_template,request

app = Flask(__name__) 

@app.route("/") #telling flask the first line to read is this
def index(): #renders template
    return(render_template("index.html"))

if __name__ == "__main__": #confirming that the application belongs to us
    app.run(port=1234)
