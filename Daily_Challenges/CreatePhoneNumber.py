def create_phone_number(n):
    """ Return array in a string format of a phone number"""
    f = "".join(map(str, n[0:3]) )
    s = "".join(map(str, n[3:6]) )
    t = "".join(map(str, n[6:10]) )
    return "("+f+") "+ s +"-"+t
