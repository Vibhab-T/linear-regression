Used scikit's linear regression model.

The leastsq.py file is a simple implementation of the least square method. not used in the main code anywhere.

Process:

1. Imported all the neccassary libraries and modules.

2. Created a data frame using the pandas libraries.

3. From the data frame: seperated our x and y.
   x: features, predictors
   y: label

   this was done by train_test_split() from sklearn.model_selection

4. Scikit was used to init a linear regression model.

   linear_model = LinearRegression()
   here all the necesary things for a linear regression model is created by the library.

5. the training data was given to the linear model.

   linear_model.fit(x_train, y_train)

   here, the fit method uses the least square method to calcualte coefficients for each x. it also creats a best fit line to use for predictions.

6. the test x was given to predict y.

   predictions = linear_model.predict(x_test)

7. this 'predictions' was then compared to the actual data. y_test.

8. seaborn scatterplot and matplotlib was used to compare and display the analysis.

   sns.scatterplot(x="predictions", y="y_test")
   plt.show()

9. residual analysis was done.

   residual = difference between the prediction and the actual value.
   residuals = predictions - y_test

   when using a linear regression model, the residuals must be randomly distributed. they should have a normal distribution.
   If not randomly distributed, the model or training data might be biased.

   this distribution was again checked using sns and plt.

   sns.displot(residuals, kde="True") kde shows the curve.
