from os import name
from joblib import load

# Function to make predictions
def prediction(X_test, clf_object):

	# Predicton on test with giniIndex
	y_pred = clf_object.predict(X_test)
	print("Predicted values:")
	print(y_pred)
	return y_pred


def test(X):
    testing = load("clf_gini.joblib")
    y_pred_gini = prediction(X, testing)


if __name__ == "__main__":
    # [Urban_or_Rural, Vehicle Type, Sex of Driver, Age Band of Driver]
    test([[1, 3, 1, 4]])
