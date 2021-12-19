import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_html('results_ejudge.html')
data1 = pd.read_excel('students_info.xlsx')
AllData = data[0].merge(data1, left_on='User', right_on='login')
A = AllData.groupby('group_faculty')[['Solved']].mean()
B = AllData.groupby('group_out')[['Solved']].mean()

A.plot(kind='bar', color='purple')
plt.xticks(rotation=0)
plt.savefig("group_faculty.png")
B.plot(kind='bar', color='violet')
plt.xticks(rotation=0)
plt.savefig("group_out.png")
plt.show()
C = AllData[(AllData['G'] >= 10) | (AllData['H'] >= 10)]
print(C['group_faculty'].unique(), C['group_out'].unique())