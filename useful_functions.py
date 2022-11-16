def convert_dollars_to_float(x):
    something = [] #this list holds only the balance keys from the dictionary
    only_dollars = [] # this holds the values without the commas
    convert = [] # this holds the converted values 
    for a in x:
        a = a.strip('$')
        something.append(a)
    for b in something:
        b = b.replace(",","")
        only_dollars.append(b)
    for c in only_dollars:
        c = float(c)
        convert.append(c)
    return convert