def squared_error(predicted, actual):
    error = predicted - actual
    return error ** 2


def mean_squared_error(predictions, actuals):
    errors = []

    for predicted, actual in zip(predictions, actuals):
        errors.append(squared_error(predicted, actual))

    return sum(errors) / len(errors)


actual_prices = [30, 30, 30]
predicted_prices = [25, 29, 40]

loss = mean_squared_error(predicted_prices, actual_prices)

print("Actual prices:", actual_prices)
print("Predicted prices:", predicted_prices)
print("Mean Squared Error:", loss)