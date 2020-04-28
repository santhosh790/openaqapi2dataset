import json
import csv
import numpy as np

class DSCreater:

    def __init__(self):
        """
        This is a class file for converting the Dataframe input into a dataset
        Then write it into a CSV file.

        """


    def convert_to_csv(self, df={}, fname = "aqDS.csv"):
        if df is {}:
            return

        dsFile = open(fname, "w", newline='', encoding='utf-8')

        csv_writer = csv.DictWriter(dsFile, fieldnames = df[10].keys(), restval = np.NaN)

        csv_writer.writeheader()

        for each in df:
            csv_writer.writerow(each)

        dsFile.close()