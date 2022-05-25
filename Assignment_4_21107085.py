'''Name- Dipanshu Panda
SID - 21107085
Branch- Mechanical'''
# Q1.
while True:
    Marks = int(input("Enter your marks: "))
    if Marks<25:
        print('Grade obtained is:F')
    elif 25<=Marks<45:
        print('Grade obtained is:E')
    elif 45<=Marks<50:
        print('Grade obtained is:D')
    elif 50<=Marks<60:
        print('Grade obtained is:C')
    elif 60<=Marks<80:
        print('Grade obtained is:B')
    else:
        print('Grade obtained is:A')
    e = input('exit?(y/n)')
    if e == 'y':
        break
    else:
        pass


# Q2.
year = int(input("Enter a year: "))
if year%4 == 0:
    print("The year you entered is a leap year")
elif year%100 ==0  and year%400 ==0:
    print("The year you entered is a leap year")
else:
    print("The year you entered is not a leap year")


# Q3.
print("Lets solve!!!")
import random
a = 1
while a<11:
    num_1 = random.randint(0,9)
    num_2 = random.randint(0,9)
    child_input = int(input(f"Question.{a}: {num_1}X{num_2} = "))
    product = num_1*num_2
    if product == child_input:
        print("Congratulations you are correct")
    else:
        print(f"Sorry child the correct answer is {product}")
    a+=1


# Q4.
for i in range(1,200):
    if i%5==2:
        if i%6==3:
            if i%7==2:
                print(i,'is the possible number of candys')
