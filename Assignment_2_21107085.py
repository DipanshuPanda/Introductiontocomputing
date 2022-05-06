'''Name- Dipanshu Panda
SID - 21107085
Branch- Mechanical'''
# Q1
stm = "Python is a case sensitive language." 
# a.
length = len(stm)
print(f"Length of the input strinh is {length}")
# b.
print(stm[::-1])
# c.
stm_1 = stm[10:26]
print(stm_1)
# d.
print(stm.replace("a case sensitive","object oriented"))
# e.
index = stm.find("a")
print(index)
# f.
print(stm.replace(" ",""))

# Q2
name = "Dipanshu Panda"
sid = 21107085
dept = "Mechanical"
cgpa = 9.9
print(f"Hey, {name} Here!\nMy SID is {sid}\nI am from {dept} department and my CGPA is {cgpa} ")

# Q3
a = 56 ; b = 10
print(a&b)
print(a|b)
print(a^b)
print(a<<2, b<<2)
print(a>>2, b>>4)

# Q4
User_stm = input("Hey user type a string of your choice:\n")
# Coonverting string to lower case
small = User_stm.lower()
if "name" in small:
    print("Yes")
else:
    print("No")

# Q5
s1 = int(input("User enter side 1 of the triangle: "))
s2 = int(input("User enter side 2 of the triangle: "))
s3 = int(input("User enter side 3 of the triangle: "))
cases = s1+s2>s3 and s3+s2>s1 and s1+s3>s1
# Using match case
match cases:
    case True:
        print("Yes")
    case False:
        print("No")


# Q6
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
# Using XOR function
n3 = bin(n1^n2)
n4 = n3.count('1')
print(n4)




 