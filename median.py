import random
import time

def medianOfMedians(a, k):
    if len(a) <= 5:
        return sorted(a)[k]

    medians = [sorted(a[i:i+5])[len(a[i:i+5])//2] for i in range(0, len(a), 5)]

    pivot = medianOfMedians(medians, len(medians)//2)

    low = [x for x in a if x < pivot]
    high = [x for x in a if x > pivot]
    pivots = [x for x in a if x == pivot]

    if k < len(low):
        return medianOfMedians(low, k)
    elif k < len(low) + len(pivots):
        return pivot
    else:
        return medianOfMedians(high, k - len(low) - len(pivots))


def randomized(a, k):
    if len(a) == 1:
        return a[0]

    pivot = random.choice(a)

    low = [x for x in a if x < pivot]
    high = [x for x in a if x > pivot]
    pivots = [x for x in a if x == pivot]

    if k < len(low):
        return randomized(low, k)
    elif k < len(low) + len(pivots):
        return pivot
    else:
        return randomized(high, k - len(low) - len(pivots))


# Test cases for comparison
def getTime(algorithm, array, k):
    start_time = time.time()
    result = algorithm(array, k)
    end_time = time.time()
    return result, end_time - start_time

# Generating test data for empirical analysis
def generateData(size, distribution):
    if distribution == "random":
        return random.sample(range(size * 10), size)
    elif distribution == "sorted":
        return list(range(size))
    elif distribution == "reverseSorted":
        return list(range(size, 0, -1))


# Main function for empirical analysis
def empiricalAnalysis():
    inputSizes = [1000, 5000, 10000, 20000]  # Different input sizes
    distributions = ["random", "sorted", "reverseSorted"]

    for size in inputSizes:
        print(f"\nArray Size: {size}")
        for dist in distributions:
            array = generateData(size, dist)
            k = len(array) // 2

            _, timeDeterministic = getTime(medianOfMedians, array, k)

            _, timeRandomized = getTime(randomized, array, k)

            print(f"Distribution: {dist}")
            print(f"Deterministic Selection Time: {timeDeterministic:.6f} seconds")
            print(f"Randomized Selection Time: {timeRandomized:.6f} seconds")


empiricalAnalysis()
