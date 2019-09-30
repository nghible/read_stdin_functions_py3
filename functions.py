# Hackerrank STDIN:

import sys
from io import StringIO
import numpy as np
import pandas as pd

def read_to_pd():

    # Get the data set information:
    info = sys.stdin.readline().split(' ')

    columns, rows = int(info[0]), int(info[1])
    string = StringIO( sys.stdin.read() )

    full_data = pd.read_csv(string, sep = ' ',skiprows = 0, header = None)

    X_train = full_data.iloc[ :rows, :columns]
    y_train = full_data.iloc[ :rows, columns]

    X_test = full_data.iloc[rows+1: , :columns]

    return(X_train, X_test, y_train)




X_train, X_test, y_train = read_to_pd()

# y_test we do not have.
   
