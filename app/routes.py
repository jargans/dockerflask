from flask import current_app as app
from flask import render_template, jsonify

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/status')
def status():
    return jsonify({"message": "Server is up and running"})
