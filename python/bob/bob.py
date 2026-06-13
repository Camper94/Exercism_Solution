def response(hey_bob):
    str = hey_bob
    if str.endswith('?') and str.isupper()  : return "Calm down, I know what I'm doing!"
    if str.isupper()  : return "Whoa, chill out!"
    if str.endswith('?') or str.endswith('?   ') : return "Sure."
    if str == None or str == "" or str == "          " or str== "\n\r \t" or str =="\t\t\t\t\t\t\t\t\t\t": 
        return "Fine. Be that way!"
    elif str[-1]== " " : return "Whatever."
    return "Whatever."
