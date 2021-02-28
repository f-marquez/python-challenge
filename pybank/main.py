#import my dependancies
import os
import csv


#create file path
budget_data_path = os.path.join("../pybank/resources/budget_data.csv")


#open and read data path
with open(budget_data_path) as budget_data_file:
    reader = csv.reader(budget_data_file)
