# Pair Programming Roman Numerals
#
# Jeffrey Smith & Lovell Williams (coworkers)
#

# Jeffrey's part
def integer_to_roman(input):
    roman = ""
    number = input
    while (number > 0):
        if (number - 1000 > 0):
            roman += "M"
            number -= 1000
        elif (number - 500 > 0):
            roman += "D"
            number -= 500
        elif (number - 100 > 0):
            roman += "C"
            number -= 100
        elif (number - 50 > 0):
            roman += "L"
            number -= 50
        elif (number - 10 > 0):
            roman += "X"
            number -= 10
        elif (number - 5 > 0):
            roman += "V"
            number -= 5
        elif (number - 1 >= 0):
            roman += "I"
            number -= 1
    return roman

roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# Lovell's part
def roman_to_integers(roman):
    num = 0
    for x in range(len(roman)):
        num += roman_dict[roman[x]]
    return num

def main():
    print(integer_to_roman(1234))

    print("\n")

    print(roman_to_integers("MDCLXVII"))
    
main()
