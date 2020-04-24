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

@app.route('calc.html')
def returnCalcHtml():
  return render_template("calc.html")

if __name__ == '__main__':
  app.run(threaded = True, port = 5000, debug = True)