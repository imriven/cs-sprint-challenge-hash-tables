def has_negatives(a):
    """
    YOUR CODE HERE
    """
    result = []
    p = {}
    n = {}
    for num in a:
        if num > 0:
            p[num] = True
        elif num < 0:
            n[abs(num)] = True
    for num in p.keys():
        if num in n.keys():
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
