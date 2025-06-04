import csv
import os
import pandas as pd
from pathlib import path

file_to_load = os.path.join("Resources,""budget_data.csv")
file_to_output = os.path.join("analysis,""budget_analysis.txt")

total_months=86
total_net=22564198

with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    header = next(reader)

    first_row=next(reader)


    total_net

    total