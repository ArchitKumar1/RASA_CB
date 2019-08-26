from flask import Flask, redirect, url_for, request, render_template, make_response
from werkzeug import secure_filename
from shutil import copyfile
import os
app = Flask(__name__,)


@app.route('/main')
def success():

    return render_template('index.html')


@app.route('/stories', methods=['POST', 'GET'])
def stories():
    if request.method == 'POST':
        user = request.form['nm']

        return render_template('first.html')


@app.route('/domain', methods=['POST', 'GET'])
def domain():
    if request.method == 'POST':
        user = request.form['nm']

        return render_template('second.html')


@app.route('/intent', methods=['POST', 'GET'])
def intent():
    if request.method == 'POST':
        user = request.form['nm']

        return render_template('third.html')


@app.route('/final', methods=['POST', 'GET'])
def final():
    if request.method == 'POST':
        user = request.form['nm']
	
        return render_template('final.html')

@app.route('/cb', methods=['POST', 'GET'])
def cb():
	if request.method == 'POST':
		user = request.form['nm']
		os.system("rasa train")
		os.system("rasa x")
		return '', 204

@app.route('/visual', methods=['POST', 'GET'])
def visual():
	if request.method == 'POST':
		user = request.form['nm']
		os.system("rasa visualize ")
		APP_ROOT = os.getcwd()
		APP_SRC= os.path.join(APP_ROOT, 'graph.html')
		APP_DEST = os.path.join(APP_ROOT, 'templates\graph.html')
		copyfile(APP_SRC,APP_DEST)
		return render_template("graph.html")
		
@app.route('/up1', methods=['POST', 'GET'])
def up1():
	if request.method == 'POST':
		f = request.files['file']
		filename = secure_filename(f.filename)
		APP_ROOT = os.getcwd()
		APP_SRC= os.path.join(APP_ROOT, 'data')
		f.save(os.path.join(APP_SRC, filename))
		return '', 204


@app.route('/up2', methods=['POST', 'GET'])
def up2():
	if request.method == 'POST':
		f = request.files['file']
		filename = secure_filename(f.filename)
		APP_ROOT = os.getcwd()
		APP_SRC= os.path.join(APP_ROOT, 'data')
		f.save(os.path.join(APP_SRC, filename))
		return '', 204


@app.route('/up3', methods=['POST', 'GET'])
def up3():
	if request.method == 'POST':
		f = request.files['file']
		filename = secure_filename(f.filename)
		APP_ROOT = os.getcwd()
		f.save(os.path.join(APP_ROOT, filename))
		return '', 204


if __name__ == '__main__':
    app.run(debug=True)
