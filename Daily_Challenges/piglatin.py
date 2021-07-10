def pig_it(text):
    """ Return each word in the string with its first letter removed and added to the end with ay """
    # create an empty list to append the new words to
    toReturn = []
    # create a list of the different words to iterate through
    words = text.split()
    # iterate through the list using a for loop
    for word in words:
        # check if the letters are in the alphabet
        if word.isalpha():
            # if True, follow pig latin rules
            toReturn.append(f'{word[1:]+word[0]}ay')
        else:
            # else append the non-alphabet character as is
            toReturn.append(word)
    # join the Pig words in the list back together and return as a single string
    return " ".join(toReturn)
