from flask import Flask
from flask import render_template,request

app = Flask(__name__) 

@app.route("/", methods=["GET", "POST"]) #telling flask the first line to read is this
def index(): #renders template
    return(render_template("index.html"))

@app.route("/prediction", methods=["GET", "POST"]) #telling flask the first line to read is this
def prediction(): #renders template
    return(render_template("prediction.html"))

@app.route("/predicted_DBS", methods=["GET", "POST"]) #telling flask the first line to read is this
def predicted_DBS(): #renders template
    q = float(request.form.get("q"))
    return(render_template("predicted_DBS.html",r=(-50.6*q)+90.2))

if __name__ == "__main__": #confirming that the application belongs to us
    app.run(port=1234)
