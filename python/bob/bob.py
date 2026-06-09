def response(hey_bob):
    str = hey_bob
    if str.endswith('?') and str.isupper()  : return "Calm down, I know what I'm doing!"
    if str.isupper()  : return "Whoa, chill out!"
    if str.endswith('?') : return "Sure."
    if str == None : return "Fine. Be that way!"
    elif str == "" : return "Whatever."
    return "Whatever."
