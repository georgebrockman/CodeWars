def array_diff(a, b):
    """ Remove all of the values present in both a and b """
    # create a list to be returned
    toReturn = []
    # use a for loop to add to new list
    for num in a:
        toReturn.append(num)
        # use a for loop inside the first one to delete all instances of num in toReturn
        for num in b:
            if num in toReturn:
                toReturn.remove(num)

    return toReturn
