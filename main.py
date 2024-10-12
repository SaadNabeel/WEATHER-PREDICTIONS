
weather = (1, 0, 0, 0, 1, 1, 0)


rainy = 0
sunny = 0


for day in weather:
    if day == 1:
        rainy += 1
    else:
        sunny += 1


print("Number of rainy days:", rainy)
print("Number of sunny days:", sunny)


if rainy > sunny:
    print("Prediction: It is likely to be rainy.")
elif sunny > rainy:
    print("Prediction: It is likely to be sunny.")
else:
    print("Prediction: The weather is unpredictable, equal rainy and sunny days.")
