import numpy as np
import matplotlib.pyplot as plt

# load the data
X = []
Y = []
for line in open('data_1d.csv'):
    x, y = line.split(',')
    X.append(float(x))
    Y.append(float(y))

# turn X and Y into numpy arrays
X = np.array(X)
Y = np.array(Y)

plt.scatter(X,Y)
plt.show()

# apply the equations we learned to calculate a and b

denominator = X.dot(X) - X.mean() * X.sum()
a = ( X.dot(Y) - Y.mean() * X.sum() ) / denominator
b = ( Y.mean() * X.dot(X) - X.mean() * X.dot(Y) ) / denominator

# calculate predicted Y
Yhat = a*X + b

# plot all

plt.scatter(X, Y)
plt.plot(X, Yhat)`
plt.show()

# calculate R squared ( to determine how good is the model )
d1 = Y - Yhat
d2 = Y - Y.mean()
r2 = 1 - d1.dot(d1) / d2.dot(d2)

print "the r-squared", r2
