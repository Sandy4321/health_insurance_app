# minimal example from:
# http://flask.pocoo.org/docs/quickstart/

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/explore')
def explore():
    return render_template('explore.html')

@app.route('/model')
def model():
    return render_template('model.html')

@app.route('/insurance')
def insurance():
    return render_template('insurance.html')

@app.route('/poverty')
def poverty():
    return render_template('poverty.html')

if __name__ == '__main__':
    app.run()
