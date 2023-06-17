# import os
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# os.environ['PATH'] += r"C:\Selenium"

# driver = webdriver.Chrome()
# driver.get("https://www.pexels.com/photo/sea-flight-dawn-sunset-16884742/")
# driver.implicitly_wait(2000)
# btton=driver.find_element(By.CLASS_NAME,"dropdown_wrapper__0W_Kf")
# btton.click()
# driver.quit()
'''for i in range (1,10):
    print(i,".\n")'''
#print(17%3)
# bill=input(float())
# tip=float(bill)*(20.0/100.0)
# print(tip)
# mybool = True
# print(mybool)
# True

# print(2==3)
# False
# print("hello"=="hello")
# True
# w=float(input())
# h=float(input())
# bmi=float(w/h**2)
# if bmi<18.5:
#     print("Underweight")
# elif bmi>=18.5 and bmi<25:
#     print("Normal")
# elif bmi>=25 and bmi<30:
#     print("Overweight")
# else:
#     print("Obesity")
# N=int(input())
# N=N+1
# total=0
# for N in range (1,N):
#     total+=N
# print(total)
#print("14" + "km")
# x = [2, 4]

# x += [6, 8]
# #x=[2,4,6,8]
# print(x[2]//x[0]) 
# x = [42, 8, 7, 1, 0, 124, 8897, 555, 3, 67, 99]
# summ=0
# for i in range(0,len(x)):
#     summ=summ+x[i]
# print(summ)
# numbers = [1, 2, 3]
# total = 0
# for n in numbers:
#     total = total + n
# print(total)
# a = int(input())
# b = int(input())
# lis=[]
# for i in range(a,b):
#     lis.append(i,)
#     i+=1
# print(lis)
# x = [2, 4, 5, 7, 4]

# y = x.index(4)

# print(y)
# nums = [1, 3, 5, 2, 4]

# res = min(nums) + max(nums)

# print(res)
# nums = [2,4,8,9,5]
# nums.insert(1,3) #[1,2,3,4,8,5]
# nums.remove(9)
# nums.insert(0, nums.count(8))
# print(nums[3])
#print("{0}{1}{0}".format("abra", "cad"))
# str="{c}, {b}, {a}".format(a=5, b=9, c=7)

# print(str)

# msg = input()
# for x in range(0,len(msg),1):
#     if(msg[x]=='#'):
#         msg=msg.replace(msg[x],' ')
# print(msg)
# txt = "hello"

# print(max(txt))
# def my_func():
#       print("spam")
      
# print("spam")
# print("spam")

# def welcome():
#        name=input()
#        print("Welcome,",name)

# welcome()


# def exclamation(word):
#       print(word + "!")

# exclamation("spam")
# exclamation("eggs")
# exclamation("python")

# def sum(x):
    
#     res = 0

#     for i in range(x):

#         res+=i

#     return res

    

# print(sum(4))

# def print_nums(x):
    
#   for i in range(x):

#     print(i)

#     return

# print_nums(10)

# def func(x):
    
#   res = 0

#   for i in range(x):

#      res += i

#   return res

# print(func(3))

# n = [2, 4, 6, 8]
# res = 1
# for x in n[1:3]:
#   res *= x

# print(res)
# ages = {"Dave": 24, "Mary": 42, "John": 58}
# print(ages["John"])
# print(ages["Mary"])
# print(ages)

# car = {
#     'brand':'BMW',
#     'year': 2018,
#     'color': 'red',
#     'mileage': 15000
# }
# x=input()
# if x in car:
#     print(car[x])
# nums = {
#     1: "one",
#     2: "two",
#     3: "three",
# }
# print(1 in nums)
# print("three" in nums)
# print(4 not in nums)

# data = {
#     'Singapore': 1,
#     'Ireland': 6,
#     'United Kingdom': 7,
#     'Germany': 27,
#     'Armenia': 34,
#     'United States': 17,
#     'Canada': 9,
#     'Italy': 74
# }
# x=input()
# if x in data:
#     print(data.get(x))
# else:
#     print("Not found")

# contacts =(
#     'James', 42,
#     'Amy', 24,
#     'John', 31,
#     'Amanda', 63,
#     'Bob', 18)

# x=input()
# if x in contacts:
#   i=contacts.index(x)
#   print(x,"is",contacts[i+1])
  
# def calc(x):
#     #your code goes here
#     pp=x*4
#     aa=x*x
  
#     tup=(pp,aa)
#     return tup
    

# side = int(input())
# p, a = calc(side)

# print("Perimeter: " + str(p))
# print("Area: " + str(a))
# def test(func, arg):
#       return func(func(arg))

# def mult(x):
#   return x * x

# print(test(mult, 2))
# def my_func(f, arg):
#       return f(arg)

# my_func(lambda x: 2*x*x, 5)
#!/bin/python

# def avg(*x):
#     return sum(x)/len(x)
     
# def numCells(grid):
#     # Write your code here
#     x=len(grid)
#     y=len(grid[0])
#     cell=0
#     red_flag=1
#     for i in range(x):
#         for k in range(y):
#             current_element=grid[i][k]
#             for ii in range(max(0,i-1),min(x,i+2)):
#                 for kk in range(max(0,k-1),min(y,k+2)):
#                     if (ii,kk) != (i,k) and current_element <=grid[ii][kk]:
#                         red_flag=0
#                         break
#                 if red_flag==0:
#                     break
#                 else:
#                     cell+=1
#     return cell

# def find_dominant_cells(grid):
#     rows = len(grid)
#     cols = len(grid[0])
#     dominant_cells = []

#     for i in range(rows):
#         for j in range(cols):
#             cell = grid[i][j]
#             is_dominant = True

#             # Check top neighbor
#             if i > 0 and cell <= grid[i-1][j]:
#                 is_dominant = False

#             # Check bottom neighbor
#             if i < rows-1 and cell <= grid[i+1][j]:
#                 is_dominant = False

#             # Check left neighbor
#             if j > 0 and cell <= grid[i][j-1]:
#                 is_dominant = False

#             # Check right neighbor
#             if j < cols-1 and cell <= grid[i][j+1]:
#                 is_dominant = False

#             # Check top-left neighbor
#             if i > 0 and j > 0 and cell <= grid[i-1][j-1]:
#                 is_dominant = False

#             # Check top-right neighbor
#             if i > 0 and j < cols-1 and cell <= grid[i-1][j+1]:
#                 is_dominant = False

#             # Check bottom-left neighbor
#             if i < rows-1 and j > 0 and cell <= grid[i+1][j-1]:
#                 is_dominant = False

#             # Check bottom-right neighbor
#             if i < rows-1 and j < cols-1 and cell <= grid[i+1][j+1]:
#                 is_dominant = False

#             # Add dominant cell to the result list
#             if is_dominant:
#                 dominant_cells.append(cell)

#     return len(dominant_cells)
# grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# dominant_cells = find_dominant_cells(grid)
# print(dominant_cells)


# if __name__ == '__main__':
#     n = int(input().strip())

#     if n%2==0 and n in range(2,5):
#         print("Not Weird")
#     elif n%2!=0:
#         print("Weird")
#     elif n%2==0 and n in range(6,20):
#         print("Weird")
#     elif n%2==0 and n>20:
#         print("Not Weird")


#can you adjust this code to know if this a leap year or not and covering all cases
# def is_leap(year):
#     leap = False

#     # Write your logic here
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 leap = True
#             else:
#                 leap = False
#         else:
#             leap = True
#     else:
#         leap = False

#     return leap

# year = int(input())
# print(is_leap(year))

'''You are given a string s consisting only of digits 0-9, commas ,, and dots .

Your task is to complete the regex_pattern defined below, which will be used to re.split() all of the , and . symbols in s .

It’s guaranteed that every comma and every dot in s is preceeded and followed by a digit.'''
# regex_pattern = r"[,.]"	# Do not delete 'r'.

# import re
# print("\n".join(re.split(regex_pattern, input())))
# def find_max(nums):
#     max_num = float("-inf") # smaller than all other numbers
#     for num in nums:
#         if num > max_num:
#           # (Fill in the missing line here)
#     return max_num


'''The yield statement is used to define a generator,
replacing the return of a function to provide 
a result to its caller without destroying local variables.
-----------------------------------------------------------
In short, generators allow you to declare 
a function that behaves like an iterator,
i.e. it can be used in a for loop.
'''
# def countdown():
#     i=5
#     while i > 0:
#         yield i
#         i -= 1

# for i in countdown():
#     print(i)

# def numbers(x):
#       for i in range(x):
#         if i % 2 == 0:
#             yield i

# print(list(numbers(11)))



# def isPrime(x):
#     if x < 2:
#         return False
#     elif x == 2:
#         return True  
#     for n in range(2, x):
#         if x % n ==0:
#             return False
#     return True
# def primeGenerator(a, b):
#     #your code goes here
#     for i in range(a,b):
#         if isPrime(i):
#             yield i
# f = int(input())
# t = int(input())
# print(list(primeGenerator(f, t)))

# def make_word():
#     word = ""
#     for ch in "spam":
#         word +=ch
#         yield word

# print(list(make_word()))
######################################
