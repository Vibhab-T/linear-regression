import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import math
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error


df = pd.read_csv("ecommerce.csv")

'''
EDA = Exploratory Data Analysis, to give you a general idea of what is going on with the data, what it says. 

sns.jointplot(x="Time on App", y="Yearly Amount Spent", data=df, alpha=0.5)
plt.show()

sns.jointplot(x="Length of Membership", y="Yearly Amount Spent", data=df, alpha=0.5)  #more correlation 
plt.show()

sns.pairplot(df, kind="scatter", plot_kws={'alpha': 0.4})
plt.show()

sns.lmplot(x="Length of Membership", y="Yearly Amount Spent", data=df, scatter_kws={"alpha": 0.5}) ##creates a best fit line
plt.show()

LINEAR REGRESSION = y = B0 + B1x
b1 = m = gradient
b0 =  c = y intercept

for  multiple variables

y = b0 + b1x1 + b2x2 + b3x3 + b4x4 + .... bnxn

'''

x = df[["Avg. Session Length", "Time on App", "Time on Website", "Length of Membership"]] #predictors, features
y = df["Yearly Amount Spent"]  #label

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)


linear_model = LinearRegression()

linear_model.fit(x_train, y_train) #uses least square method to find the best fit line 

predictions = linear_model.predict(x_test)  #returns an array of y values based on the input x_test values. can be used to compare with actual data. 

sns.scatterplot(x=predictions, y=y_test)
plt.xlabel("Predictions")
plt.title("Prediction Vs Actual Value")
plt.show()

print("Mean abssolute error: ", mean_absolute_error(y_test, predictions))
print("Mean Squared Error: ", mean_squared_error(y_test, predictions))
print("Root Mean Squared RMS error: ", math.sqrt(mean_squared_error(y_test, predictions)))



#residual analysis 
#distance between model prediction and actual value 
#linear regression assumes that when making predictions using a linear model, the residuals must be random.
#if it is not random, the model might be biased somewhere. 


residuals = y_test - predictions 
sns.displot(residuals, kde=True)
plt.title("Residuals' Distribution")
plt.show()


