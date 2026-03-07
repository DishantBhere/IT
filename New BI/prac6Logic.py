#Logistic Regression using Python

# Import required libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


data = load_iris()


X = data.data
y = data.target


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = LogisticRegression(max_iter=200)


model.fit(X_train, y_train)


print("\nEnter flower details:")
sl = float(input("Sepal Length (cm): "))
sw = float(input("Sepal Width (cm): "))
pl = float(input("Petal Length (cm): "))
pw = float(input("Petal Width (cm): "))


user_data = [[sl, sw, pl, pw]]
prediction = model.predict(user_data)


flower_name = data.target_names[prediction[0]]

print("\nPredicted Flower Type:", flower_name)
