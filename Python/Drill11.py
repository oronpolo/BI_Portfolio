#Get each digit from a number in the reverse order.

def main(num):
    num = str(num)
    num_length = len(num)
    num2= []
    for i in range(num_length+1):
        if i == 0:
            continue
        j = -i
        num2.append(num[j])
        print()

    for i in range(len(num2)):
        print(num2[i],end =" ")

main(1234)

"""
number = 7536
print("Given number", number)
while number > 0:
    # get the last digit
    digit = number % 10
    # remove the last digit and repeat the loop
    number = number // 10
    print(digit, end=" ")
"""