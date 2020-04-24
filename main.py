from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def getIndex():
  return "Tas ir PD apr Flask"

@app.route('/health')
def getReturnOk():
  return "OK"

@app.route('/home')
def returnHomeHtml():
  return render_template("home.html")

@app.route('/calc' , methods = ["POST"])
def returnCalcHtml():
  return render_template("calc.html")
  sk1 = int(input())
  sk2 = int(input())
  darb = str(input())
  JSON = {
    "sk1" :  sk1
    "sk2" :  sk2
    "darb" :  darb
  }

@app.route('/getResults', methods = ["GET"])  
def getResults():
  if darb == "+":
    actionReslt = JSON["sk1"] + JSON["sk2"] 
  elif darb == "-":
     actionReslt = JSON["sk1"] - JSON["sk2"] 
  elif darb == "*":
    actionReslt = JSON["sk1"] * JSON["sk2"] 
  elif darb == "/":
    actionReslt = JSON["sk1"] / JSON["sk2"]
  JSON1 = {
    "rez" : actionReslt 
  }

  print(JSON1["rez"])

@app.route('/about')
def returnAboutHtml():
  return render_template("about.html")

if __name__ == '__main__':
  app.run(threaded = True, port = 5000, debug = True)