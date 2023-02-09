#libraries
import streamlit as st
import numpy as np
import pandas as pd
import shutil
import matplotlib.pyplot as plt


from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier



#data

data=pd.read_csv("Hotel Reservations.csv")

#model

data=data.drop(axis=1,columns='Booking_ID')
data=data.drop(axis=1,columns='type_of_meal_plan')
data=data.drop(axis=1,columns='room_type_reserved')

#encoding target
labelencoder = LabelEncoder()


data['booking_status'] = labelencoder.fit_transform(data['booking_status'])
#data['booking_status']



target=data["booking_status"]
data.drop(axis=1,columns="booking_status",inplace=True)


data['market_segment_type'] = labelencoder.fit_transform(data['market_segment_type'])
data['market_segment_type'].value_counts()



X_train=data.iloc[:29020]
y_train=target.iloc[:29020]

X_test=data.iloc[29020:]
y_test=target.iloc[29020:]


clf = DecisionTreeClassifier(criterion="entropy", max_depth=4,min_samples_leaf=2)

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)









#Deployment_pickle
import pickle

# save the model to disk


pickle_out = open("clf.pkl", "wb")
pickle.dump(clf, pickle_out)
pickle_out.close()
    



