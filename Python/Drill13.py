#Print multiplication table from 1 to 10

def main():
    for i in range (1,11):
        for j in range (1,11):
            if(len(str(i*j)) > 1):
                print(i*j , end = " ")
            else:
                print(i*j , end = "  ")
        print()
    

main()