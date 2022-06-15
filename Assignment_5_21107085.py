# Q1.
s1 = input("Hey user enter a sentence: ")
print(s1[::-1])

# Q2.
num_1 = int(input('Hey user enter upto what range you want to check the divisibility: '))
num_2 = int(input('Enter the number for which you want to check divisibility: '))
for i in range(1,(1+num_1)):
    if i%num_2 == 0:
        print(i)
    else:
        pass

# Q3.
side_1 = float(input("Enter side 1 of triangle: "))
side_2 = float(input("Enter side 2 of triangle: "))
side_3 = float(input("Enter side 3 of triangle: "))
if side_1+side_2>side_3 and side_3+side_2>side_1 and side_1+side_3>side_2:
    s = (side_1+side_2+side_3)/2
    # Heron's Formula; Area = (s(s-a)(s-b)(s-c))^(1/2) where a, b, c are sides of triangle
    Area = (s*(s-side_1)*(s-side_2)*(s-side_3))**(0.5)
    print(f'Area of the given triangle is {Area}')
else:
    print('User enter sides that can consitute a triangle')


# Q4.
star = '*'
for i in range(1,5):
    print(star*i)
for j in range(5,0,-1):
    print(star*j)

# Q5.
k = 65
n = int(input("Input the number of rows = "))
for i in range(n):
    for j in range(i+1):
        print(chr(k), end=" ")
        k = k + 1
    print()



# Q6.

lower_value = int(input ("Please, Enter the Lowest Range Value: "))  
upper_value = int(input ("Please, Enter the Upper Range Value: "))  
  
print ("The Prime Numbers in the range are: ")  
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for l in range (2, number):  
            if (number % l) == 0:  
                break  
        else:  
            print (number)  

# Q7.
a = 1
for m in range(1,500):
    if m%7 == 0:
        if m%11 == 0:
            print(m)
    else:
        pass
        


# Q8.
a = 1
l1 = []                     # List of negative numbers
l2 = []                     # List of positive numbers
l3 = []                     # List of even numbers
l4 = []                     # List of odd numbers
l5 = []                     # List of all numbers
dict = {}                   
repeat = 0
while a<=10:
    num = int(input('Enter a number: '))
    a  += 1
    if num<0:
        l1.append(num)
    if num>0:
        l2.append(num)
    if num%2 == 0:
        l3.append(num)
    if num%2 != 0:
        l4.append(num)
    l5.append(num)
for t in l5:
    dict[t] = l5.count(t)  # Adding key and values to dictionary

print(f'''
List of all negative numbers is = {l1}
List of all positive numbers is = {l2}
List of all even numbers is = {l3}
List of all odd numbers is = {l4}''')
for k in dict:
    print(f'Integer:{k} occurs {dict[k]} times')


# Q9
user_list = eval(input('Hey user enter a list of words: '))  # User will input a list of words
inp_dict = {}
for z in user_list:
    inp_dict[z] = user_list.count(z)   # Adding key and values to dictionary
for w in inp_dict:
    print(f'Word:{w} occurs {inp_dict[w]} times')



