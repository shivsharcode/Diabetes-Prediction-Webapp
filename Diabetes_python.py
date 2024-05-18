
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


#Load dataset
df = pd.read_csv(r'mlModel/Diabetes.csv')
df.head()

X = df.drop('diabetes', axis = 1)
y = df['diabetes']

# Split the dataset into training set and testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)


# Create Logistic Regression model 
model = LogisticRegression()

model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)


#Evaluate the model accuracy
accuracy = accuracy_score(y_test, y_pred)

conf_matrix = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

    

def diabetes_predictor(form_data):
    row = pd.DataFrame(form_data)
    
    global scaler, model 
    #separate x and y
    # X_sample = row.drop('diabetes', axis=1)
    # y_sample = row['diabetes']
    
    # Standardize X
    X_sample = scaler.transform(row)

    # Predict = model.predict(X_sample)
    y_pred = model.predict(X_sample)
    print("Predicted Class : ", y_pred)

    if(y_pred == 0):
        return "Non-Diabetic"
    else : 
        return "Diabetic"
    
    

