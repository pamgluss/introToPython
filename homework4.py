ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
teens = ["", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
zgroup = ["", "Hundred", "Thousand", "Million"]

def subthousand(number):
    if number < 10:
        return ones[number]
    elif number > 10 and number < 20:
        return teens[number]
    elif number >= 20 and number < 100:
        numberasstring = str(number)
        return tens.numberasstring[0] + ones.numberasstring[1]
    else:
        answer = ""
        numberasstring = str(number)
        return ones.numberasstring[0] + zgroup[1] + tens.numberasstring[1] + ones.numberasstring[2]


def overthousand(number):
    digits = splitbythousands(number)
    print(digits)


def splitbythousands(number):
    m = number
    triples = []
    while m > 0:
        catch = divmod(m, 1000)
        m = catch[0]
        triples.append(catch[1])
    return triples

def spell(number):
    n = number.lstrip('-')
    if n.isnumeric():
        if len(n) > 10:
            return "Number is too long!"
        elif n is 0:
            return "Zero"
        else:
            n = int(n)
            if n < 1000:
                return subthousand(n)
            elif n > 1000:
                return overthousand(n)
    else:
        return "Type in a number."

spell("179")
