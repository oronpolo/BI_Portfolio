#Print the Sum of a Current Number and a Previous number
def main():
    
    number = 10
    current_num = 0
    previuse_num = 0
    while (current_num < number):
        print("Current Number " ,current_num, "Previous Number ", previuse_num, "Sum: ", current_num + previuse_num )
        #print(current_num + previuse_num)
        previuse_num = current_num
        current_num += 1

main()

"""
print("Printing current and previous number and their sum in a range(10)")
previous_num = 0

# loop from 1 to 10
for i in range(1, 11):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
    # modify previous number
    # set it to the current number
    previous_num = i
"""