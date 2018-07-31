from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  bob = '<p><a href="bob">bob</a></p>'
  pam = '<p><a href="pam">pam</a></p>'
  sue = '<p><a href="sue">sue</a></p>'
  output = '<p>Hello, World!</p>'+bob+pam+sue
  return output

@app.route('/bob')
def hello_bob():
  return 'Hello, Bob!'

@app.route('/sue')
def sue():
  return 'Hello, sue!'

if __name__ == "__main__"
    app.run(host='0.0.0.0', port=8080)
