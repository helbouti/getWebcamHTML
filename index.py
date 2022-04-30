from email.policy import default
from flask import Flask, jsonify, request,render_template
import os
from werkzeug.utils import secure_filename
import time
from datetime import datetime



now = datetime.now()

youtube_id=0 #input("YOUTUBE ID : ")
#print(time.time)
if not youtube_id:
    youtube_id="jnNoNxe1LC0"

app = Flask(__name__)

#curl -F "file=@image.jpg" http://localhost:8000/save_webcam
@app.route('/save_webcam', methods=['POST'])
def save_webcam():
    myfile = request.files['file']
    print(request.files['file'].filename)
    myfile.save(os.path.join("templates",secure_filename(myfile.filename)))
    return jsonify({"status":"ok"})

@app.route('/')
def index():
    global youtube_id
    return render_template("myIndex.html",youtube_id=youtube_id,now=now)


@app.route('/index2')
def index2():
    global youtube_id
    return render_template("index2.html")

@app.route('/brython_index')
def brython_index():
    return render_template("brython_index.html");

#need pyopenssl
#use pip install pyopenssl
app.run(host="0.0.0.0",port=8000,debug=True,ssl_context='adhoc')
#app.run(ssl_context='adhoc')
#app.run(host="0.0.0.0",port=8000,debug=True)

