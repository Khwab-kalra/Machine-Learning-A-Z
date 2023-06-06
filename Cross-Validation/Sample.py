from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

# Load the dataset and define features and target variables
X, y = load_dataset()

# Create a linear regression model
model = LinearRegression()

# Perform 5-fold cross-validation and evaluate the model using mean squared error
scores = cross_val_score(model, X, y, cv=5, scoring='neg_mean_squared_error')

# Convert the negative mean squared error to positive
mean_squared_error = -scores.mean()

print(f"Average Mean Squared Error: {mean_squared_error}")
