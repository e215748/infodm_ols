import datasets
X,Y = datasets.load_linear_example1()
print(X,Y)

import regression
model = regression.LinearRegression()
print(model.x)
