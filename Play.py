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

