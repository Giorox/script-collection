def f(x):
    return x**3 - 2


if __name__ == '__main__':
    lowerBound = float(input("Enter the lower bound value of the interval: "))
    upperBound = float(input("Enter the upper bound value of the interval: "))
    tolerance = float(input("Enter desired tolerance: "))

    # Save initial values to left and right bounds
    leftValue = lowerBound
    rightValue = upperBound

    # Save values to be used when calculating tolerance
    previousEvaluated = 200000000000  # set a huge number so the initial tolerance condition isnt satisfied
    currentEvaluated = 0

    # Start iterating
    while (abs(currentEvaluated - previousEvaluated) / 2 > tolerance):
        # Calculate test value
        testValue = (leftValue + rightValue) / 2
        print(testValue)

        # Get F(testvalue)
        currentValue = f(testValue)

        # Save old currentvalue to previous value and save current value to current evaluation
        previousEvaluated = currentEvaluated
        currentEvaluated = currentValue

        # Verify next condition
        if currentValue < 0:
            leftValue = testValue
        else:
            rightValue = testValue

    print(f"The function approximation in the [{lowerBound}; {upperBound}] interval with a tolerance of {tolerance} is: {testValue}")
