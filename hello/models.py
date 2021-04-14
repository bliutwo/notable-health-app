from django.db import models

import csv

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class DataParser(models.Model):
    def __init__(self):
        self.patient_data = self.get_data("patients.csv")
        self.physician_data = self.get_data("physicians.csv")
        self.physicians = self.get_physicians()

    def get_data(self, csv_filename):
        data = []
        with open(csv_filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                data.append(row)
        return data

    def get_physicians(self):
        physicians = []
        line_count = 0
        print(self.physician_data)
        for row in self.physician_data:
            if line_count != 0:
                print(row[0])
                physicians.append(row[0])
            line_count += 1
        print(physicians)
        return physicians
