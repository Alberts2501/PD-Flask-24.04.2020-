from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def getIndex():
  return "Tas ir PD apr Flask"

@app.route('/health')
def getReturnOk():
  return "OK"

if __name__ == '__main__':
  app.run(threaded = True, port = 5000, debug = True)