#Check Palindrome Number

def main(num1):
    num_str = str(num1)
    num1_length = len(num_str)
    num2 = ""

    for i in range(num1_length+1):
        if(i==0):
            continue
        j = -(i)
        num2 += num_str[j]
    
    num2 = int(num2)
    if num1 == num2:
        print("Palindrome")
    else:
        print("not Palindrome")      

main(221)