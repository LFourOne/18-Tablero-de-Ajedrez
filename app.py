from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index(numy=4,numx=4):
    return render_template("index.html", numx=numx, numy=numy)

@app.route("/<int:numx>")
def slashnum(numy=2, numx=None):
    return render_template("index.html", numx=numx, numy=numy)

@app.route("/<int:numx>/<int:numy>")
def slashnumxnumy(numy=None, numx=None):
    return render_template("index.html", numx=numx, numy=numy)

@app.route("/<int:numx>/<int:numy>/<color1>/<color2>")
def slashnumxnumycolor1color2(numy=None, numx=None, color1=None, color2=None):
    return render_template("index.html", numx=numx, numy=numy, color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)