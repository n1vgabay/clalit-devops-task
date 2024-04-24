from flask import Flask

app = Flask(__name__)

@app.route('/')
def print_welcome():
    return 'Welcome!'

@app.route('/readiness')
def readiness():
    return '', 200

@app.route('/liveness')
def liveness():
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)