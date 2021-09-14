from flask import Flask,render_template
import requests,json
import time

app = Flask(__name__)
def get_distance():
    data_s = requests.get("https://poumy7jw4l.execute-api.us-east-1.amazonaws.com/v1/get-data/")
    data = json.loads(data_s.text)
    return data['Item']['distance']['N']
@app.route('/')
@app.route('/Frontend_Index.html')
def index():
    return render_template("Frontend_Index.html",out=get_distance())
@app.route('/contactus.html')
def contactus():
    return render_template("contactus.html")
@app.route('/aboutproject.html')
def aboutproject():
    return render_template("aboutproject.html")

if __name__=='__main__':
         app.run(debug=True)