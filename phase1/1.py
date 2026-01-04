#y = mx + c    lenear regression equation
#m = slope (model.coef_) scopef the line | Slope = effect of input on output
#c = intercept (model.intercept_) bias |Intercept = base value when input is 0


import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error, r2_score
import matplotlib.pyplot as plt

x= np.array([[10],[20],[30],[40],[50]])
y=np.array([200,400,600,800,1000])

# e=np.array(x).shape
# print(e)
# k=np.array(x).__len__()
# print(k)
# print(np.array(y).mean()) 

# Splitting the dataset into training and testing sets
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.3,random_state=42)
# print(x_train,x_test,y_train,y_test)

# Creating and training the Linear Regression model
model=LinearRegression()
model.fit(x_train,y_train)

# Making predictions and evaluating the model
# print("Slope (model.coef_):", model.coef_)
# print("Intercept (model.intercept_):", model.intercept_)

predictions=model.predict(x_test)
new_predictions=model.predict(np.array([[60],[70]]))
# print(predictions)
# print(new_predictions)


mae=mean_absolute_error(y_test,predictions)
mse=mean_squared_error(y_test,predictions)
r2=r2_score(y_test,predictions)
print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)
print("R^2 Score:", r2) 


#Case	             Training Error   Validation Error	Problem
#High Bias	                High	    High	     Underfitting
#High  Variance	            Low	        High	      Overfitting
#Low Bias + Low Variance	Low	        Low	          Best model
#Low Variance + High Bias	High	    High	      Too simple model

#Training error high
#Test error high
#➡️ High bias


# Training error low
# Test error low
# ➡️ Low bias