def likes(names):
    """
    Returns a string with who has liked the post, if more than three only two names are returned with a number of others
    """
    # most restrictive condition always comes first
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return "%s likes this" % names[0]
    elif len(names) == 2:
        return "%s and %s like this" % (names[0], names[1])
    elif len(names) == 3:
        return "%s, %s and %s like this" % (names[0], names[1], names[2])
    else:
        # remove two off total length to get total value of other likers
        return "%s, %s and %s others like this" % (names[0], names[1], len(names)-2)
