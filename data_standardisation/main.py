# This module should ensure that the given data-set is standardised into a pandas data-frame.

from data_standardisation import data_explorer as de
from pprint import pprint

if __name__ == '__main__':
    path_to_csv_file = "../data/customer_churn_bank.csv"
    column_y = "Exited" # This is the predictor class

    column_counts = de.get_column_counts(path_to_csv_file)
    pprint(column_counts)

    data_types = de.get_column_types(path_to_csv_file)
    pprint(data_types)


    pass
/Users/shreyasrk/PycharmProjects/ChurnPrediction/data_standardisation/main.py