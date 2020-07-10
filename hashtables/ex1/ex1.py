def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    h = {}
    
    for i, weight in enumerate(weights):
        if weight in h.keys():
            h[weight].append(i)
        else:
            h[weight] = [i]
    
    for k, v in h.items():
        found = h.get(limit - k)
        if found:
            if found[0] == h[k][0]:
                secondary = h[k][1]
            else:
                secondary = h[k][0]
            return (max(found[0], secondary), min(found[0], secondary))

    return None
