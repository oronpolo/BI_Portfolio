#Get an int value of base raises to the power of exponent
#Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp

def exponent(base, exp):
    result = base
    for i in range (1,exp):
        result *= base
    print(result)


exponent(3,3)
exponent(4,7)