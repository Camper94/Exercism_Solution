def response(hey_bob):
    str = hey_bob.strip()
    if not str: return "Fine. Be that way!"
    if str[-1] == "?" and str.isupper()  : return "Calm down, I know what I'm doing!"
    if str[-1] == "?": return "Sure."
    if str.isupper()  : return "Whoa, chill out!"
    return "Whatever."
