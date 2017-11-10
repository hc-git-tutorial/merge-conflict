def uppercase(a_string):
    return a_string.upper()

def reverse(a_string):
    out_string = ""
    for char in a_string:
        out_string = char + out_string
    return out_string

def uppercase_reverse(a_string):
    return uppercase(reverse(a_string))
