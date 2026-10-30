x = 3
y = 13
w = 0.2
b = 0.0
learning_rate = 0.01

for i in range(100):
    prediction = w * x + b
    loss = (y - prediction) ** 2
    dw = -2 * x * (y - prediction)
    db = -2 * (y - prediction)
    w = w - learning_rate * dw
    b = b - learning_rate * db

print("Final Weight : ",w)
print("Bias : ",b)
print("Prediction : ",prediction)
print("Loss : ",loss)