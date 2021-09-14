from flask import Flask,render_template,request
import pickle
import numpy as np
from flask_mysqldb import MySQL
from utils.all_utils import Pred,Mysql

model = pickle.load(open('models\model.pkl', 'rb'))

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'B_311747'
app.config['MYSQL_DB'] = 'datascience'

mysql = MySQL(app)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/submit',methods=['POST','GET'])
def predict():
    ## Collecting infrmation from user
    if request.method == "POST":
        age = request.form['age']
        capital_gain = request.form['capital_gain']
        capital_loss = request.form['capital_loss']
        education_num = request.form['education_num']
        hours = request.form['hours']
        sexs = request.form['sexs']
        occupations = request.form['occupations']
        works = request.form['works']
        educations = request.form['educations']
        races = request.form['races']
        country = request.form['country']
        meritals = request.form['meritals']
        relations = request.form['relations']


        ## Add All the input data in database
        Mysql(mysql,age, capital_gain, capital_loss, education_num, hours, occupations, sexs, meritals, country, races, works, educations, relations)

        ## Predicting Income based on user input
        output = Pred(age, capital_gain, capital_loss, education_num, hours, occupations, sexs, meritals, country, races, works, educations, relations)
        models = model.predict([output])[0]

        return render_template("result.html",models = models)

if __name__ == '__main__':
    app.run(debug=True)
