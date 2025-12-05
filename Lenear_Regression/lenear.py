import numpy as np
class LinearRegression:
    def fit(self, X, y):
        X=np.array(X)
        y=np.array(y)

        X_mean = np.mean(X, axis=0)
        y_mean = np.mean(y)


        num = ((X-X_mean)*(y - y_mean)).sum(axis=0)
        den = ((X - X_mean)**2).sum(axis=0)


        self.weights = num / den
        self.bias = y_mean - np.dot(self.weights, X_mean)   


    def predict(self, X):        
        X=np.array(X)
        y_predicted = np.dot(X, self.weights) + self.bias
        return y_predicted