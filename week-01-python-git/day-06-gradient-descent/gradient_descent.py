x = 3
y = 10
w = 2
b = 0

prediction = w * x + b
loss = (y - prediction) ** 2

print("Prediction:", prediction)
print("Loss:", loss)

learning_rate = 0.1

for i in range(100):
    prediction = w * x + b
    loss = (y - prediction) ** 2

    gradient = -2 * x * (y - prediction)
    w = w - learning_rate * gradient

print("Final weight:", w)
print("Final prediction:", w * x + b)
print("Final loss:", (y - (w * x + b)) ** 2)