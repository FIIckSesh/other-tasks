import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('volume_of_sales.csv', delimiter=';')

X = df['X']
y = df['Y']
n = len(X)

sum_X = sum(X)
sum_y = sum(y)

sum_sqrX = sum(X**2)
sum_sqry = sum(y**2)
multipl_Xy = sum(X*y)

a = (sum_y * sum_sqrX - sum_X * multipl_Xy) / (n*sum_sqrX - sum_X**2)
b = (n*multipl_Xy - sum_y * sum_X) / (n*sum_sqrX - sum_X**2)

y_pred = a + b*df['X']
ss_res = sum((df['Y'] - y_pred)**2)
ss_tot = sum((df['Y'] - df['Y'].mean())**2)

r2 = round(1 - ss_res/ss_tot, 4)

print(r2)
x = np.arange(0,50,0.01)
fx = a + b*x

plt.title('Поле корреляции')
plt.xlabel('Цена за единицу, руб.')
plt.ylabel('Объем продаж, тыс.руб.')
plt.plot(x,fx)
plt.scatter(X, y)
plt.grid()
plt.text(10, 1100, f'y = {round(b, 3)}x + {round(a, 3)}')
plt.text(10, 1050, f'R2 = {r2}')


plt.show()
