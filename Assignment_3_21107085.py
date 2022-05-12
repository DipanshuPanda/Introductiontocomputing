'''Name- Dipanshu Panda
SID - 21107085
Branch- Mechanical'''
# # Q1.
# print("Q1.")
# num1 = int(input("Hey user enter a number: "))
# binary1 = bin(num1)[2:]
# print(f"The binary equivalent of the number you entred is {binary1}")

# # Q2.
# print("Q2.")
# User_input_1= input("Hey user you want to \n(a)carry a single operation on bunch of numbers \n(b)or do you have an expression to solve\nplease press the required key: ")
# if "a" in User_input_1:
#     User_input_2= input("Hey user enter the corresponding key for operation you want to perform\nYou can choose the following operations:\n(1)addition\n(2)subtraction\n(3)multiplication\n(4)division\n(5)trignometric fucn. ")
#     if "1" in User_input_2:
#         n1 = float(input("Enter your number, it may be a an integer or a decimal: "))
#         n2 = float(input("Enter another number: "))
#         a = 0
#         n3 = 0
#         while a<1:
#             n4 = float(input("Enter another number:\nElse press (0) to obtain final value "))
#             n3 += n4 
#             if n4==0.0:
#                 a += 1
#             print(n1+n2+n3)
#             sum = n1+n2+n3
#             print('The final value is stored as sum for future use')
#     if "2" in User_input_2:
#         n1 = float(input("Enter your number, it may be a an integer or a decimal: "))
#         n2 = float(input("Enter another number: "))
#         a = 0
#         n3 = 0
#         while a<1:
#             n4 = float(input("Enter another number:\nElse press (0) to obtain final value "))
#             n3 -= n4 
#             if n4==0.0:
#                 a += 1
#             print(n1-n2+n3)
#             sub = n1-n2+n3
#             print('The final value is stored as sub for future use')
#     if "3" in User_input_2:
#         n1 = float(input("Enter your number, it may be a an integer or a decimal: "))
#         n2 = float(input("Enter another number: "))
#         a = 0
#         n3 = 1
#         while a<1:
#             n4 = float(input("Enter another number:\nElse press (1) to obtain final value "))
#             n3 *= n4 
#             if n4==1.0:
#                 a += 1
#             print(n1*n2*n3)
#             mul = n1*n2*n3
#             print('The final value is stored as mul for future use')
#     if "4" in User_input_2:
#         n1 = float(input("Enter your number, it may be a an integer or a decimal: "))
#         n2 = float(input("Enter another number: "))
#         a = 0
#         n3 = 1
#         while a<1:
#             n4 = float(input("Enter another number:\nElse press (1) to obtain final value "))
#             n3 /= n4 
#             if n4==1.0:
#                 a += 1
#             print((n1/n2)*n3)
#             div = (n1/n2)*n3
#             print('The final value is stored as div for future use')
#     if "5" in User_input_2:
#         import math
#         from math import degrees
#         trig_fucn = input("Enter your trignometric function\nsin or cosec\ncos or sec\ntan or cot\nsin^-1\ncos^-1\ntan^-1")
#         if 'sin'or'cos'or'tan'or'cosec'or'sec'or'cot' in trig_fucn:
#             pi = 22/7
#             deg = float(input("Hey user enter your angle in radians:\nin this format -->pi/no."))
#             deg = math.degrees(deg)
#             if "sin" or "cosec" in trig_fucn:
#                 if "sin" in trig_fucn:
#                     print(math.sin(deg))
#                 if "cosect" in trig_fucn:
#                     print(1/(math.sin(deg)))
#             if "cos" or "sec" in trig_fucn:
#                 if "cos" in trig_fucn:
#                     print(math.cos(deg))
#                 if "sec" in trig_fucn:
#                     print(1/(math.cos(deg)))
#             if "tan" or "cot" in trig_fucn:
#                 if "tan" in trig_fucn:
#                     print(math.tan(deg))
#                 if "cot" in trig_fucn:
#                     print(1/(math.tan(deg)))
#         if 'sin^-1'or'cos^-1'or'tan^-1' in trig_fucn:
#             if "sin^-1" in trig_fucn:
#                 num_1 = float(input("Hey user enter the number whose arcsine you want to find"))
#                 print(math.asin(num_1))
#             if "cos^-1" in trig_fucn:
#                 num_2 = float(input("Hey user enter the number whose arcsine you want to find"))
#                 print(math.acos(num_2))
#             if "tan^-1" in trig_fucn:
#                 num_3 = float(input("Hey user enter the number whose arcsine you want to find"))
#                 print(math.atan(num_3))
             
# if "b" in User_input_1:
#     User_input_3= input("Hey user enter your expression: ") 
#     print(User_input_3,'=',eval(User_input_3))

# # Q3.
# import math
# print("Q3.")
# #a.
# i = int(input("Enter an integer"))
# print('a.',(i+(i+1))*(i+2))
# #b.
# print('b.',i/2*(i-1))
# #c.
# r = float(input('enter radius'))
# print('c.',4*math.pi*r*r)
# #d.
# alpha = float(input('Enter angle 1 in radians:'))
# beta = float(input('Enter angle 2 in radians:'))
# print('d.',math.sqrt((r*math.cos(alpha)**2) + (r*math.sin(beta)**2)))
# #e.
# x1 = int(input('Enter x coordinate of first point:'))
# y1 = int(input('Enter y coordinate of first point:'))
# x2 = int(input('Enter x coordinate of second point:'))
# y2 = int(input('Enter y coordinate of second point:'))
# print('e.',(y2-y1)/(x2-x1))

# Q4.
print("Q4.")
print('a.')
for i in range(5):
    print(i)
print('b.')
for i in range(3,10):
    print(i)
print('c.')
for i in range(4,13,3):
    print(i)
print('d.')
for i in range(15,5,-2):
    print(i)
print('e.')
for i in range(5,3):
    print(i)

# Q5.
# print("Q5.")
# C = int(input('Enter number of carbon atoms in molecule:'))
# H = int(input('Enter number of hydrogen atoms in molecule:'))
# O = int(input('Enter number of oxygen atoms in molecule:'))
# comb_mol_weight = H*1.00794 + C*12.0107 + O*15.9994
# print(f'The molecular weight of the compound is {comb_mol_weight}')
