import pandas as pd

Data = pd.read_csv('transactions.csv', sep=',')
print(Data[Data['STATUS'] == 'OK'].sort_values(by='SUM', ascending=False).head(3))
Data1 = Data[Data['STATUS'] == 'OK']
print('Umbrella receipts =', Data1[Data1['CONTRACTOR'] == 'Umbrella, Inc']['SUM'].sum())