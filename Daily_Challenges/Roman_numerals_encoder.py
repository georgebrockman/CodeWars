# create a mapping of roman numeral values
roman_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def solution(n):
    """ Returns integer as a string in Roman Numeral form """
    # set variable roman equal to an empty string
    roman = ''
    # use a while loop to make sure n is greater than zero
    while n > 0:
        # loop through the roman_map
        for i, r in roman_map:
            # use another while loop
            while n >= i:
                # add the roman numeral to the string
                roman += r
                # minus the index from the input integer
                n -= i
    # return roman numerals
    return roman
