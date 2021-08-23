from flask import Flask,render_template,request
import pickle
import numpy as np
from flask_mysqldb import MySQL

pkl_file = open('models\model.pkl','rb')
model = pickle.load(open('models\model.pkl', 'rb'))
index_dict = pickle.load(pkl_file)


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

    index_dict = pickle.load(open('models\cat','rb'))
    country_cat = pickle.load(open('models\country_cat','rb'))
    merital = pickle.load(open('models\merital','rb'))
    education = pickle.load(open('models\education','rb'))
    sex = pickle.load(open('models\sex','rb'))
    relation = pickle.load(open('models\\relation','rb'))
    occupation = pickle.load(open('models\occupation','rb'))
    work = pickle.load(open('models\work','rb'))
    race = pickle.load(open('models\\race','rb'))


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

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO userinput(age, capital_gain, capital_loss, education_year,working_hours, occupation, sex, merital, country, race, work_class, education, relation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (age, capital_gain, capital_loss, education_num, hours, occupations, sexs, meritals, country, races, works, educations, relations))
        mysql.connection.commit()
        cur.close()

        output = np.zeros(108)
        output[0] = age
        output[2] = capital_gain
        output[3] = capital_loss
        output[1] = education_num
        output[4] = hours
        
        re_sex = sexs
        if re_sex not in sex:
            pass
        else:
            output[index_dict[str(sexs)]] = 1

        result_location = meritals
        output[index_dict[str(meritals)]] = 1
            
        result_location = country
        if result_location not in country_cat:
            output[34] = 1
        else:
            output[index_dict[str(country)]] = 1

        result_location = races
        if result_location not in race:
            output[77] = 1
        else:
            output[index_dict[str(races)]] = 1
            
        result_location = works
        output[index_dict[str(works)]] = 1
            
        result_location = occupations
        if result_location not in occupation:
            output[93] = 1
            output[index_dict[str(occupations)]] = 1

        result_location = educations
        output[index_dict[str(educations)]] = 1
            
        result_location = relations
        output[index_dict[str(relations)]] = 1  
        models = model.predict([output])[0]
        return render_template("result.html",models = models)

if __name__ == '__main__':
    app.run(debug=True)
