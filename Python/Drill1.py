#the sum and multiply result of two numbers
def main():
    
    while(True):
        print("please enter a number:\n")
        num1 = get_user_input()
        if(type(num1)==str or type(num1)==bool):
            print("please enter a NUMERIC value\n")
        else:
            break

    while(True):
        print("please enter a number:\n")
        num2 = get_user_input()
        if(type(num2)==str or type(num2)==bool):
            print("please enter a NUMERIC value\n")
        else:
            break

    print("the numbers multiplication result are:", multiple(num1, num2), "\n")
    print("the numbers sum result are:", num1+num2, "\n")

def get_user_input():
#get input from user and return verible with the value and the correct type
    user_input = input()
    try:
        val = int(user_input)
        return val
    except ValueError:
        try:
            val =  float(user_input)
            return val
        except ValueError:
            try:
                val =  bool(user_input)
                return val
            except ValueError:
                val = str(user_input)
                return val

def multiple(num1, num2):
    return num1*num2


main()