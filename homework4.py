# These are the lists of english words we're going to use.
ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
teens = {11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
zgroup = ["Hundred", "Thousand", "Million"]

# This first function takes in numbers that are less than 100
# This will be handy for figuring out specific tens and tees in the tens and ones places
def subhundred(number):
    # If the number is less than 10, it needs to read from the ones list.
    if number < 10:
        return ones[number]
    # The teens are tricky, so I made it a dictionary instead of a list.
    elif number > 10 and number < 20:
        return teens[number]
    # The tens are easy since 1 -> 10 when indexing and so forth.
    elif number >= 20 and number < 100:
        # Here I had to make the integer a string so that I could index it.
        numberasstring = str(number)

        # I broke up the string into 10's and 1's places
        tensplace = int(numberasstring[0])
        onesplace = int(numberasstring[1])

        # So now that the tens place is separated, you can look for it in the tensplace list, same with the ones place.
        return tens[tensplace] + " " + ones[onesplace]

# This function is for numbers less than 1000 (so still in the hundreds)
# The parameters it takes is number (the value to be spelled out) and znum, which indicates whether it is in the hundred, thousands or millions.
def subthousand(number, znum):
    # I realized it's possible to have 1 thousand or 10 thousand, so we had to plan for missing indices.
    if number < 100:
        # Since the number can be evaluated by an old function, I just called the subhundred function.
        answer = subhundred(number) + " " + zgroup[znum]
    else:
        numberasstring = str(number)
        hundredsplace = int(numberasstring[0])
        tensplace = int(numberasstring[1:])
        # this is broken and does NOT support "one hundred thousand" - oops, gotta get on that
        answer = ones[hundredsplace] + " " + zgroup[znum] + " " + subhundred(tensplace)

    return answer

# the purpose of this function is to handle all numbers over a thousand. After a thousand, you can reuse old functions.
# so all this function does is compile the results of the other functions in a way that makes sense.
def overthousand(number):
    digits = splitbythousands(number)
    answer = ""
    # For testing purposes.
    print(digits)
    #Digits[2] (if it exists) will be 1,000,000 - 999,999,999
    if len(digits) > 2:
        answer += subthousand(digits[2], 2)

    #digits[1] will be 1000-999,999
    if len(digits) > 1:
        answer += subthousand(digits[1], 1)

    # digits[0] is going to be 0 - 999
    answer += subthousand(digits[0], 0)
    return answer

# This is a helper function for overthousand.
# All it does is split up the input into triples - to get the hundreds, thousands and millions separated.
def splitbythousands(number):
    m = number
    triples = []
    while m > 0:
        catch = divmod(m, 1000)
        m = catch[0]
        triples.append(catch[1])
    return triples

# Here is the main function! It detects the size of the number and whether it falls within our doable parameters
def spell(number):
    # Checks to make sure an input has been made
    if number:
        # Removes the negative sign and checks to see if input is numeric (not a word or mixture of letters)
        n = number.lstrip('-')
        if n.isnumeric():
            # If the number is too big, we won't try it.
            if len(n) > 10:
                return "Number is too long!"
            # If the number is zero, return zero instead of running any other code.
            elif n is 0:
                return "Zero"
            else:
                #Turn the number into an integer so we can compare it to 100 and 1000.
                n = int(n)
                if n < 100:
                    return subhundred(n)
                elif n >= 100 and n < 1000:
                    return subthousand(n, 0)
                else:
                    return overthousand(n)
        else:
            return "Type in a number."
    else:
        return "Type in a number."

print(spell("12234409"))