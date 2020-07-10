def intersection(arrays):
    """
    YOUR CODE HERE
    """
    intersect = {}

    for item in sorted(arrays, key=len)[0]:
        intersect[item] = 1
    for arr in sorted(arrays, key=len)[1:]:
        for item in arr:
            if item in intersect.keys():
                intersect[item] += 1
    result = [k for k, v in intersect.items() if v == len(arrays)]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
