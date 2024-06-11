import pandas as pd
from sklearn import tree
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from IPython.display import Image
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC 
from matplotlib import pyplot as plt
from sklearn.datasets import make_regression, make_swiss_roll
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor, AdaBoostRegressor, RandomForestClassifier, ExtraTreesClassifier
from sklearn.svm import SVR
import os

df = pd.read_csv("clean_df.csv")
case_id = input('Enter the case ID: ')
patient_questionnaire = pd.read_csv(f"patient_questionnaire_data_{case_id}.csv")
 # Define features set
df3 = patient_questionnaire.copy()
# just the columns we want
df = df[["MARSTAT", "EMPLOY", "LIVARAG", "DAYWAIT", "SERVICES", "FRSTUSE1", "FREQ_ATND_SELF_HELP_D", "PRIMPAY", "DIVISION", "PREG", "METHUSE"]]
df3 = df3[["MARSTAT", "EMPLOY", "LIVARAG", "DAYWAIT", "SERVICES", "FRSTUSE1", "FREQ_ATND_SELF_HELP_D", "PRIMPAY", "DIVISION", "PREG", "METHUSE"]]
# clean the data recieved

df3['MARSTAT'] = df3['MARSTAT'].replace('Never married', 1)
df3['MARSTAT'] = df3['MARSTAT'].replace('Now married', 2)
df3['MARSTAT'] = df3['MARSTAT'].replace('Separated', 3)
df3['MARSTAT'] = df3['MARSTAT'].replace('Divorced, widowed', 4)

df3['EMPLOY'] = df3['EMPLOY'].replace('Full-time', 1)
df3['EMPLOY'] = df3['EMPLOY'].replace('Part-time', 2)
df3['EMPLOY'] = df3['EMPLOY'].replace('Unemployed', 3)
df3['EMPLOY'] = df3['EMPLOY'].replace('Not in labor force', 4)

df3['LIVARAG'] = df3['LIVARAG'].replace('Homeless', 1)
df3['LIVARAG'] = df3['LIVARAG'].replace('Dependent living', 2)
df3['LIVARAG'] = df3['LIVARAG'].replace('Independent living', 3)

df3['DAYWAIT'] = df3['DAYWAIT'].replace('1–7', 1)
df3['DAYWAIT'] = df3['DAYWAIT'].replace('8–14', 2)
df3['DAYWAIT'] = df3['DAYWAIT'].replace('15–30', 3)
df3['DAYWAIT'] = df3['DAYWAIT'].replace('31 or more', 4)

df3['SERVICES'] = df3['SERVICES'].replace('Detox, 24-hour, hospital inpatient', 1)
df3['SERVICES'] = df3['SERVICES'].replace('Detox, 24-hour, free-standing residential', 2)
df3['SERVICES'] = df3['SERVICES'].replace('Rehab/residential, hospital (non-detox)', 3)
df3['SERVICES'] = df3['SERVICES'].replace('Rehab/residential, short term (30 days or fewer)', 4)
df3['SERVICES'] = df3['SERVICES'].replace('Rehab/residential, long term (more than 30 days)', 5)
df3['SERVICES'] = df3['SERVICES'].replace('Ambulatory, intensive outpatient', 6)
df3['SERVICES'] = df3['SERVICES'].replace('Ambulatory, non-intensive outpatient', 7)
df3['SERVICES'] = df3['SERVICES'].replace('Ambulatory, detoxification', 8)

df3['FRSTUSE1'] = df3['FRSTUSE1'].replace('11 years and under', 1)
df3['FRSTUSE1'] = df3['FRSTUSE1'].replace('12–14 years', 2)
df3['FRSTUSE1'] = df3['FRSTUSE1'].replace('15–17 years', 3)
df3['FRSTUSE1'] = df3['FRSTUSE1'].replace('18–20 years', 4)
df3['FRSTUSE1'] = df3['FRSTUSE1'].replace('21–24 years', 5)
df3['FRSTUSE1'] = df3['FRSTUSE1'].replace('25–29 years', 6)
df3['FRSTUSE1'] = df3['FRSTUSE1'].replace('30 years and over', 7)

df3['FREQ_ATND_SELF_HELP_D'] = df3['FREQ_ATND_SELF_HELP_D'].replace('No attendance', 1)
df3['FREQ_ATND_SELF_HELP_D'] = df3['FREQ_ATND_SELF_HELP_D'].replace('1–3 times per month', 2)
df3['FREQ_ATND_SELF_HELP_D'] = df3['FREQ_ATND_SELF_HELP_D'].replace('4–7 times per month', 3)
df3['FREQ_ATND_SELF_HELP_D'] = df3['FREQ_ATND_SELF_HELP_D'].replace('8–30 times per month', 4)
df3['FREQ_ATND_SELF_HELP_D'] = df3['FREQ_ATND_SELF_HELP_D'].replace('Some attendance, frequency is unknown', 5)

df3['PRIMPAY'] = df3['PRIMPAY'].replace('Self-pay', 1)
df3['PRIMPAY'] = df3['PRIMPAY'].replace('Private insurance', 1)
df3['PRIMPAY'] = df3['PRIMPAY'].replace('Medicare', 1)
df3['PRIMPAY'] = df3['PRIMPAY'].replace('Medicaid', 1)
df3['PRIMPAY'] = df3['PRIMPAY'].replace('Other government payments', 1)
df3['PRIMPAY'] = df3['PRIMPAY'].replace('No charge', 1)
df3['PRIMPAY'] = df3['PRIMPAY'].replace('Other', 1)

df3['DIVISION'] = df3['DIVISION'].replace('U.S. territories', 0)
df3['DIVISION'] = df3['DIVISION'].replace('New England', 1)
df3['DIVISION'] = df3['DIVISION'].replace('Middle Atlantic', 2)
df3['DIVISION'] = df3['DIVISION'].replace('East North Central', 1)
df3['DIVISION'] = df3['DIVISION'].replace('West North Central', 1)
df3['DIVISION'] = df3['DIVISION'].replace('South Atlantic', 1)
df3['DIVISION'] = df3['DIVISION'].replace('East South Central', 1)
df3['DIVISION'] = df3['DIVISION'].replace('West South Central', 1)
df3['DIVISION'] = df3['DIVISION'].replace('Mountain', 1)
df3['DIVISION'] = df3['DIVISION'].replace('Pacific', 1)

df3['PREG'] = df3['PREG'].replace('Yes', 1)
df3['PREG'] = df3['PREG'].replace('No', 2)

df3['METHUSE'] = df3['METHUSE'].replace('Yes', 1)
df3['METHUSE'] = df3['METHUSE'].replace('No', 2)

# reshape and use the entire dataset as the training data. Using the questionaire answers as the test data
y3 = df["REASON"].values.reshape(-1, 1)
X3 = df3.copy()
# X3.drop("REASON", axis=1, inplace=True)
X_train = df[["MARSTAT", "EMPLOY", "LIVARAG", "DAYWAIT", "SERVICES", "FRSTUSE1", "FREQ_ATND_SELF_HELP_D", "PRIMPAY", "DIVISION", "PREG", "METHUSE"]] 
X_test = df3[["MARSTAT", "EMPLOY", "LIVARAG", "DAYWAIT", "SERVICES", "FRSTUSE1", "FREQ_ATND_SELF_HELP_D", "PRIMPAY", "DIVISION", "PREG", "METHUSE"]]
y_train = df["REASON"].values.reshape(-1, 1)
# y_test = train_test_split(X2, y2, random_state=78)
scaler = StandardScaler()
X_scaler = scaler.fit(X_train)
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)
 # Create the decision tree classifier instance
model = tree.DecisionTreeClassifier()
 # Fit the model
model = model.fit(X_train_scaled, y_train)

 # Making predictions using the testing data
predictions = model.predict(X_test_scaled)
if predictions == 1:
    print("This person has a high probability of success")
else:
    print("This person has a low probability of success")

