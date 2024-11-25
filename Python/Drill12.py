#Calculate income tax for the given income by adhering to the rules below

#First $10,000	0
#Next $10,000	10
#The remaining	20


def main(salary):
    if salary <= 10000:
        print("income after tax is : " , salary)
    elif (salary > 10000 and salary < 20000):
        print("income after tax is : " , salary*0.9)
    else:
        print("income after tax is : " , salary*0.8)


main(15256)