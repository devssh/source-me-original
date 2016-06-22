from __future__ import division
from sklearn.cross_validation import train_test_split

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def get_data_from_csv():
    input_file = "./input/PastHires.csv"
    df = pd.read_csv(input_file, header = 0)
    return df


def clean_up_data(df):
    d = {'Y': 1, 'N': 0}
    df['Hired'] = df['Hired'].map(d)
    df['Employed?'] = df['Employed?'].map(d)
    df['Top-tier school'] = df['Top-tier school'].map(d)
    df['Interned'] = df['Interned'].map(d)
    d = {'BS': 0, 'MS': 1, 'PhD': 2}
    df['Level of Education'] = df['Level of Education'].map(d)    
    return df

def print_class_distribution(df):
    num_obs = len(df)
    num_true = len(df.loc[df['Hired'] == 1])
    num_false = len(df.loc[df['Hired'] == 0])
    print("Number of True cases:  {0} ({1}%)".format(num_true, (num_true/num_obs) * 100))
    print("Number of False cases: {0} ({1}%)".format(num_false, (num_false/num_obs) * 100))
    print("")


def split_data(df):
    feature_col_names = ['Years Experience','Employed?','Previous employers','Level of Education','Top-tier school','Interned']
    predicted_class_names = ['Hired']

    X = df[feature_col_names].values     # predictor feature columns
    y = df[predicted_class_names].values # predicted class (1=true, 0=false)
    split_test_size = 0.30

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=split_test_size, random_state=42) 
    return X_train, X_test, y_train, y_test

def print_train_test_split_percentage(X_train,df):
    print("{0:0.2f}% in training set".format((len(X_train)/len(df.index)) * 100))
    print("{0:0.2f}% in test set".format((len(X_test)/len(df.index)) * 100))
    print("")


def print_train_test_class_dist(y_train,y_test):
    print("Training True  : {0} ({1:0.2f}%)".format(len(y_train[y_train[:] == 1]), (len(y_train[y_train[:] == 1])/len(y_train) * 100.0)))
    print("Training False : {0} ({1:0.2f}%)".format(len(y_train[y_train[:] == 0]), (len(y_train[y_train[:] == 0])/len(y_train) * 100.0)))
    print("")
    print("Test True      : {0} ({1:0.2f}%)".format(len(y_test[y_test[:] == 1]), (len(y_test[y_test[:] == 1])/len(y_test) * 100.0)))
    print("Test False     : {0} ({1:0.2f}%)".format(len(y_test[y_test[:] == 0]), (len(y_test[y_test[:] == 0])/len(y_test) * 100.0)))
    print("")


data_frame = get_data_from_csv()
clean_data_frame = clean_up_data(data_frame)

print_class_distribution(clean_data_frame)

X_train, X_test, y_train, y_test = split_data(clean_data_frame)

print_train_test_split_percentage(X_train,clean_data_frame)

print_train_test_class_dist(y_train,y_test)


