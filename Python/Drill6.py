#Display numbers divisible by 5

num_list = [10,12,15,17,20]
length = len(num_list)

for i in range(length):
    if (num_list[i] % 5 == 0):
        print(num_list[i])