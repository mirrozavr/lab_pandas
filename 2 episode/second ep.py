import pandas as pd
import matplotlib.pyplot as plt

Data = pd.read_csv('flights.csv', sep=',')
count = Data['CARGO'].value_counts()
group = Data.groupby('CARGO')[['PRICE', 'WEIGHT']].sum()
res = group.merge(count, left_index=True, right_index=True)
print(res)

fig, ax = plt.subplots(1, 3, figsize=[12, 8])

ax[0].bar(res.index, res['PRICE'], color='purple')
ax[0].set_title('Полная стоимость')
ax[0].grid(axis='y')
ax[1].bar(res.index, res['WEIGHT'], color='violet')
ax[1].set_title('Полная масса')
ax[1].grid(axis='y')
ax[2].bar(res.index, res['CARGO'], color='magenta')
ax[2].set_title('Количество рейсов')
ax[2].grid(axis='y')


plt.savefig("charts.png")
plt.show()