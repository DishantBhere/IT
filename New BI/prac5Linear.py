#Linear Regression using Python

# Import required libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


x = np.array([151,174,138,186,128,136,179,163,152,131]).reshape(-1,1)


y = np.array([63,81,56,91,47,57,76,72,62,48])


model = LinearRegression()


model.fit(x,y)


predicted_weight = model.predict([[170]])

print("Predicted weight for height 170 cm:", predicted_weight[0])


plt.scatter(x,y,color='blue')
plt.plot(x, model.predict(x), color='red')

plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.title("Height vs Weight Linear Regression")

plt.show()
