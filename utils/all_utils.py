import pickle
import numpy as np

def Pred(age, capital_gain, capital_loss, education_num, hours, occupations, sexs, meritals, country, races, works, educations, relations):
    
    index_dict = pickle.load(open('models\cat','rb'))
    country_cat = pickle.load(open('models\country_cat','rb'))
    merital = pickle.load(open('models\merital','rb'))
    education = pickle.load(open('models\education','rb'))
    sex = pickle.load(open('models\sex','rb'))
    relation = pickle.load(open('models\\relation','rb'))
    occupation = pickle.load(open('models\occupation','rb'))
    work = pickle.load(open('models\work','rb'))
    race = pickle.load(open('models\\race','rb'))

    output = np.zeros(108)
    output[0] = age
    output[2] = capital_gain
    if output[2] == 0:
        output[2]
    else:
        output[2] == np.log(output[2])

    output[3] = capital_loss
    if output[3] == 0:
        output[3] = 0
    else:
        output[3] == np.log(output[3])
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
    else:
        output[index_dict[str(occupations)]] = 1

    result_location = educations
    output[index_dict[str(educations)]] = 1

    result_location = relations
    output[index_dict[str(relations)]] = 1
    # print(output)
    return output

def Mysql(mysql,age, capital_gain, capital_loss, education_num, hours, occupations, sexs, meritals, country, races, works, educations, relations):
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO userinput(age, capital_gain, capital_loss, education_year,working_hours, occupation, sex, merital, country, race, work_class, education, relation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (age, capital_gain, capital_loss, education_num, hours, occupations, sexs, meritals, country, races, works, educations, relations))
    mysql.connection.commit()
    cur.close()