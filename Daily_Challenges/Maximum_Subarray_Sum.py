def max_sequence(arr):
    """ Return the maximum value of a continuous substring """
    # create two variables one for maximum and the other for current substring maximum
    maximum = 0
    local_maximum = 0
    # iterate through the string
    for num in arr:
        # update local maximum by adding the next consecutive number
        if local_maximum > 0:
            local_maximum += num
            # if only negative numbers set value to 0
            if local_maximum < 0:
                local_maximum = 0
            # if local maximum is greater than current maximum -> update
            elif local_maximum > maximum:
                maximum = local_maximum
        # continue adding the next num in sequence
        elif num > 0:
            local_maximum += num
    # return the maximum
    return maximum
