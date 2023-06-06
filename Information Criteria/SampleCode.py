import pandas as pd
import statsmodels.api as sm

# Load the dataset and define predictor variables
data = pd.read_csv("sales_data.csv")
X = data[["feature1", "feature2", "feature3"]]
y = data["sales"]

# Define candidate models
model1 = sm.OLS(y, sm.add_constant(X[["feature1"]]))
model2 = sm.OLS(y, sm.add_constant(X[["feature1", "feature2"]]))
model3 = sm.OLS(y, sm.add_constant(X[["feature1", "feature2", "feature3"]]))

# Fit each model and calculate AIC
AICs = [model.fit().aic for model in [model1, model2, model3]]

# Select the model with the lowest AIC
best_model = AICs.index(min(AICs)) + 1

print("Best Model (AIC):", best_model)
