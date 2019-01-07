import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({'cigarettes': [0,10,20,30],
                    'CVD': [572,802,892,1025],
                    'lung': [14,105,208,355]})

data.plot('cigarettes', 'CVD', kind='scatter')
plt.title("Deaths for different smoking intensities")
plt.xlabel("Cigarettes smoked per day")
plt.ylabel("CVD deaths")
plt.grid()
plt.show()
print('#',50*"-")
# -----------------------
import statsmodels.formula.api as smf

df = pd.DataFrame({'cigarettes': [0,10,20,30],
                   'CVD': [572,802,892,1025],
                   'lung': [14,105,208,355]})

df.plot('cigarettes', 'CVD', kind='scatter')
lm = smf.ols("CVD ~ cigarettes", data=df).fit()
print(lm.summary())
xmin = df.cigarettes.min()
xmax = df.cigarettes.max()

X = np.linspace(xmin, xmax, 100)
Y = lm.params[0] + lm.params[1] * X

plt.plot(X, Y, color="darkgreen")
plt.grid()
plt.show()
print('#',50*"-")
# -----------------------
from sklearn.linear_model import LinearRegression
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
# y = 1 * x_0 + 2 * x_1 + 3
y = np.dot(X, np.array([1, 2])) + 3
reg = LinearRegression().fit(X, y)
print(reg.score(X, y))
print(reg.coef_)
print(reg.intercept_)
reg.predict(np.array([[3, 5]]))
print('#',50*"-")
# -----------------------
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
diabetes = datasets.load_diabetes()
diabetes_X = diabetes.data[:, np.newaxis, 2]
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]
regr = linear_model.LinearRegression()
regr.fit(diabetes_X_train, diabetes_y_train)
diabetes_y_pred = regr.predict(diabetes_X_test)
print('Coefficients: \n', regr.coef_)
print("Mean squared error: %.2f"
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))
print('Variance score: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))

plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)
plt.grid()
plt.show()
print('#',50*"-")
# -----------------------



