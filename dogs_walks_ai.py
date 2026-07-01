from dogs_simple import walks, temps, temperatureToWalksRelatipnships

print("temperatureToWalksRelatipnships", temperatureToWalksRelatipnships)

# slope = [n*Σ(xy) - Σx*Σy] / [n*Σ(x²) - (Σx)²]

nDays = len(temperatureToWalksRelatipnships) #n
sumOfRelationshipProduct = sum(t*w for t,w in temperatureToWalksRelatipnships) # Σ(xy)
sumOfWalks = sum(walks) #Σy
sumOfTemps = sum(temps) #Σx
sumOfSquares = sum(t**2 for t in temps) # Σ(x²) = "Spread of individual temps"
squareOfSumTemp = (sum(temps))**2 # (Σx)² "Square of average temperature"
slope = (nDays*sumOfRelationshipProduct-sumOfWalks*sumOfTemps) / \
    (nDays*sumOfSquares - squareOfSumTemp)

print("Slope:", slope)

# Means for calculating intercept: b = y_mean - m * x_mean
meanTemp = sumOfTemps / nDays
meanWalks = sumOfWalks / nDays
intercept = meanWalks - slope * meanTemp

print("Slope:", slope)
print("Intercept:", intercept)

while True:
    try:
        temperature = float(input("Please enter the temperature: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

# Intercept: b = y_mean - m * x_mean
predicted_walks = intercept + slope * temperature
print(f"Predicted walks for {temperature}°C: {predicted_walks}")
