def first_non_repeating_letter(string):
    """ Return the first letter that is non repeating in the correct case """
    # create a list variable to return
    toReturn = []
    # use a forloop to iterate through the input string
    for letter in string:
        # convert the string to a single case, upper or lower and check for counts of only one
        if string.upper().count(letter.upper()) == 1:
            # add those with only one count to the toReturn variable
            toReturn.append(letter)
    # if there are no elements in the toReturn list, return an empty string
    if len(toReturn) == 0:
        return ''
    # return the first element of the list
    return toReturn[0]
