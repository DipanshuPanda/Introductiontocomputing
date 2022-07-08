'''Name- Dipanshu Panda
SID - 21107085
Branch- Mechanical'''
# Q1
num1 = int(input("User enter a number to check wether it is perfect or not: "))
list_div = []
for i in range(1,num1+1):
    if num1%i == 0:
        if num1 == i:
            pass
        else:
            list_div.append(i)
total_div = len(list_div)
div_sum = 0
for j in range(0,total_div):
    div_sum += list_div[j]
if div_sum == num1 and ((div_sum+num1)/2) == num1:
    print(f'Yes {num1} is a perfect number')
else:
    print(f'No {num1} is not a perfect number')

# Q2
string1 = input('Hey user enter a word,phrase or a sequence: ')
string1 = string1.replace(' ','')
string2 = string1[::-1]
if string1 == string2:
    print('Yes!! it is a palindrome')
else:
    print('No!! it is not a palindrome')

# Q3
n = 5
for i in range(1,n+1):
    for j in range(0,n-i+1):
        print(' ',end='')
    a = 1
    for j in range(1, i+1):
        print(' ',a,sep = '', end= '')
        a = a*(i-j)//j
    print()

# Q4
def pangram(str):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	for char in alphabet:
		if char not in str.lower():
			return False

	return True
	
string = 'The quick brown fox jumps over the lazy dog'
if(pangram(string) == True):
	print("Yes")
else:
	print("No")

# Q5
s1 = input("Enter a hyphen(-)separated sequence of words: ")
a = s1.split("-")  # Forms a list with words seperated by hyphen
b = sorted(a)  # Sorts the words in list alphabatically
c = "-".join(b) # Stores a string of each word in list by joining them with hyphen
print(c)

# Q6
def student_data(student_id, **extra_info):  # ** Helps in iterable keyword arguement for function
     print(f'Student ID: {student_id}')
     if 'student_name' in extra_info:
        print(f"Student Name:{extra_info['student_name']}")
     if 'student_name' and 'student_class' in extra_info:
        print(f"Student Name:{extra_info['student_name']}")
        print(f"Student Class:{extra_info['student_class']}")

student_data(student_id='21107221', student_name='Tommy')

student_data(student_id='21107823', student_name='Harry', student_class ='10')

# Q7
class Student:
    pass
Dipanshu = Student()
Dipanshu.name = "Dipanshu"
print(Dipanshu)
print(Dipanshu.name)

class Marks:
    pass
mark = Marks()
mark.a = 75
mark.b = 70
print(mark)
print(mark.a)
print(mark.b)

print("class Student:",type(Student),"class Marks:",type(Marks))

# Q8
class Zero:
    def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

print(Zero().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))

# Q9
class Brackets:
   def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

print(Brackets().is_valid_parenthese("(){}[]"))
print(Brackets().is_valid_parenthese("()[{]}("))
print(Brackets().is_valid_parenthese("()"))
