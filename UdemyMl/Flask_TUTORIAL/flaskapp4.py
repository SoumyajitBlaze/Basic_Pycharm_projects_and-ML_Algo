from flask import Flask,render_template,request,jsonify

app=Flask(__name__)


@app.route('/',methods=['GET','POST'])
def home_page():
    return render_template('index1.html')

