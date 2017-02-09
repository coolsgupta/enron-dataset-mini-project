#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
num = len(enron_data)
print num
print (len(enron_data['SKILLING JEFFREY K']))
c1 = 0
c2 = 0
c3 = 0
c4 = 0
name = 'SKILLING JEFFREY K'
for key in enron_data.keys():
    if enron_data[key]["poi"] == 1:
        c1 = c1 + 1
    if (enron_data[key]["salary"] != "NaN"):
        c2+=1
    if enron_data[key]["email_address"] != "NaN":
        c3+=1
    if (enron_data[key]["total_payments"] == "NaN"):
        c4+=1

print c1

print enron_data["PRENTICE JAMES"]["total_stock_value"]
print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
print enron_data["SKILLING JEFFREY K"]["total_payments"]
print enron_data["LAY KENNETH L"]["total_payments"]
print enron_data["FASTOW ANDREW S"]["total_payments"]
print c2
print c3
print c4
per = (c4*100)/num
print per