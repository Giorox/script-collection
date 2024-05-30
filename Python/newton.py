def f(x):
    return x**3 - 2


def df(x):
    return 3 * (x**2)


if __name__ == '__main__':
    initialValue = float(input("Enter the initial value: "))
    tolerance = float(input("Enter the desired tolerance: "))

    # Save values to be used when calculating tolerance
    previousEvaluated = 200000000000  # set a huge number so the initial tolerance condition isnt satisfied
    currentEvaluated = 0

    # Save the initial value to be used in further iterations
    iterValue = initialValue

    # Start iterating
    while (abs(currentEvaluated - previousEvaluated) > tolerance):
        # Calculate test value
        testValue = iterValue - f(iterValue) / df(iterValue)
        print(testValue)

        # Get F(testvalue)
        currentValue = f(testValue)

        # Save old currentvalue to previous value and save current value to current evaluation
        previousEvaluated = currentEvaluated
        currentEvaluated = currentValue

        # Set condition
        iterValue = testValue
