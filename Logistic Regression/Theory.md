
# Logistic Regression
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Logistic regression is a statistical model used to analyze the relationship between a dependent variable and one or more independent variables. It is primarily used for binary classification problems where the output variable takes only two possible values (0 or 1).

The logistic regression model assumes a linear relationship between the independent variables and the log-odds of the dependent variable. The log-odds is the logarithm of the probability that the output variable is equal to 1 divided by the probability that it is equal to 0. The logistic function (also called sigmoid function) is used to map the log-odds to the range of [0,1] to obtain the predicted probability.

## Equations

The logistic regression model can be represented by the following equations:

Logistic Regression Equation

### **log[p(X) / (1-p(X))]  =  β0 + β1X1 + β2X2 + … + βpXp**

where:

Xj: The jth predictor variable
βj: The coefficient estimate for the jth predictor variable
The logistic function is defined as:

Logistic Function Equation

### **f(x)=L / [1+e^{-k(x-x0)}]**

where **x** is the log-odds. The predicted probability can be obtained by plugging the estimated coefficients and independent variables into the logistic regression equation and then applying the logistic function:


Key Information
1) Logistic regression is used for binary classification problems.
2) The output variable takes only two possible values (0 or 1).
3) The logistic function is used to map the log-odds to the range of [0,1] to obtain the predicted probability.
4) The logistic regression model assumes a linear relationship between the independent variables and the log-odds of the dependent variable.
5) The coefficients of the model are estimated using maximum likelihood estimation.
6) The quality of the model can be assessed using various metrics such as accuracy, precision, recall, F1-score, and ROC AUC.
