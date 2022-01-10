import pandas as pd

# df = pd.read_csv('../data/patient_tb.csv')
df = pd.read_csv('data/patient_tb.csv')
first_name = df['PatientFirstName']
print(first_name)