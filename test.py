import datasets
X,Y = datasets.load_linear_example1()
print(X,Y)

#ver1
import regression
model = regression.LinearRegression()
print(model.x)

#ver2
import importlib
importlib.reload(regression)
model = regression.LinearRegression()
model.fit(X,Y)
print(model.theta)

#ver3
importlib.reload(regression)
model = regression.LinearRegression()
model.fit(X,Y)
model.predict(X)
print(model.predict(X))