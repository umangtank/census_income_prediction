
# 👩🏻‍💻Census Income Prediction


![Home](/media/123.png)
<!-- ![Predict](/media/231.png) -->


## Overview

- This repository represents `Census income prediction` ML model.
- With the help of this project we can predict whether a person has an income of more than 50K a year or not.

## Technical aspect
- python 3.8
- Front-end: HTML, CSS
- Back-end: Flask
- IDE: Jupyter Notebook, VScode
- Database: MySql
- Deployment: Heroku


## How to run this app

Code is written in Python 3.8. If you don't have python installed on your system, click here https://www.python.org/downloads/ to install.

#### Steps
- Create virtual environment
```bash
conda create -n myenv python=3.8
```
- Activate the environment
```bash
conda activate myenv
```
- Install the packages
```bash
pip install -r requirements.txt
```
- Run the app
```bash
python app.py
```
<br>
<br>

#### Data Collection

- **Here's a brief version of what you'll find in the data file.** [Dataset](https://www.kaggle.com/overload10/adult-census-dataset)

| Features | Value     | 
| :-------- | :------- | 
| `age` | continuous. | 
| `workclass` | Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.|
| `education` | Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool |
| `education-num`| continuous |
| `marital-status`| Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse. |
| `occupation`| Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces. |
| `relationship` | Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried. |
| `race`| White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black. |
| `sex`| Female, Male. |
| `capital-gain` | continuous |
| `capital-loss`| continuous |
| `hours-per-week`| continuous |
| `Native-country`| All countries |

#### Model Creation and Evaluation

- Various classification algorithms like Logistic Regression, Random Forest, Decision Tree, Adaboost, Support Vector Machine tested.
- Random Forest & Adaboost were given better results. Adaboost was chosen as the final model.
- Model performance evaluated based on accuracy and classification report.

## Directory Tree 
```
├── static 
│   ├── images
├── templates
│   ├── welcome.html
|   ├── result.html
├── utils
|   ├── all_utils.py
|   ├── __init__.py
├── Procfile
├── README.md
├── app.py
├── Census_Income_Prediction.ipynb
├── models
├── requirements.txt
```

## Authors
Umang Tank - https://www.linkedin.com/in/umangtank/ 

## If you like this project, please do give the star. If you have any suggestions or issues, please drop me a message.
