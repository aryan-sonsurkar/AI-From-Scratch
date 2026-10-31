l = [1,2,3,4,5]

cop = [5,7,9,11,13]

w = 0.0
b = 0.0
learning_rate = 0.01

for i in range(1000):
    dw = 0
    db = 0
    for j in range(len(l)):
        prediction = w * l[j] + b
        loss = prediction - cop[j]
        dw = dw + 2 * l[j] * loss
        db = db + 2 * loss
    dw = dw / len(l)
    db = db / len(l)
    w = w - learning_rate * dw
    b = b - learning_rate * db

print("Final Weight : ",w)
print("Final Bias : ",b)

for j in range(len(l)): 
    prediction = w * l[j] + b 
    print("Input:", l[j], "| Actual:", cop[j], "| Predicted:", prediction)