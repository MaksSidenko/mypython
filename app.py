# a = [1, 4, 2, 7, 6, 20,10,3,8, 54 ]
# a.sort()
# a = a[0:100:3]

# print(a)



# def factr(a):
#     t=1
#     for i in range(1, a+1):
#         t=i*t   
#     print(t)
#     if t == 120:
#         return t*2
#     else:
#         return t*3
# q = factr(4)    
# print(q)


# fun(n)

# n=5
# def fact(n):
#     if(n==1 or n==0):
#         return 1
#     else: return n*fact(n-1)

# print("The factorial of ",n," is: ",fact(n))



# a = ["ваня", "петя", "олег", "андрей"]
# x = input()
# m = len(x)
# if x in a:
#     print("Добро пожаловать")
# elif not m<5:
#     print("привет друг")
# else:
#     print("bye")    



# while True:
#     x = input()
#     if x == "bye": 
#         break
#     m=0    
#     for i in x: 
#         if i in 'AaEeYyUuIiOo':
#             m +=1
#     print(m)

# name1 = "Паша"
# height1 = 1.60
# weight1 = 65

# name2 = "Даша"
# height2 = 1.70
# weight2 = 65

# name3 = "Яша" 
# height3 = 1.80
# weight3 = 100

# def bmi_index(name, height, weight):
#     bmi = weight / (height**2)
#     print(bmi)
#     if bmi<25:
#         return name  + " is not overweight"
#     else:
#         return name + " is overweight" 
    
        
# result1 = bmi_index(name1, height1, weight1)
# result2 = bmi_index(name2, height2, weight2)
# result3 = bmi_index(name3, height3, weight3)

# print(result1)
# print(result2)
# print(result3)

# def conv(miles):
#     km = miles/1.6
#     return km

# print(conv(40))

# import sys

# def palindrom(n):
#     m = sys.maxsize
#     for k in range(n+1, m):
#         if str(k) == str(k)[::-1]:
#             return k

# print(palindrom(54145))

# import sys

# def pol(n):
#     m = sys.maxsize
#     for i in range(n+1, m):
#         if str(i) == str(i)[::-1]:
#             return i

# print(pol(12345673456))    


# def sum(n): 
#     a = str(n)
#     b = len(a)
#     x=0
#     for i in a:
#         x=int(i)+x
#     return x

# print(sum(5252328342))     

# easy way to solve problem
# inp_digit = list(map(int, input(":")))
# print(inp_digit)
# print(sum(inp_digit))

# import math

# def rabbits(с, r): 
#     x = math.ceil(r/с)
#     return x

# print(rabbits(5, 11))


# x = list(map(int, input(":")))
# print(x)

# y = list(map(int, input(":").split()))
# print(y)

# print("ответ: ", eval(input("Что нужно посчитать? ")))


# def twosum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             sum = nums[i]+nums[j]
#             if sum == target:
#                 return [i, j]        

# print(twosum([1,3,4,4, 10],8))


# def twosum(nums, t):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i]+nums[j]  == t:
#                 return [i, j] 

# print(twosum([1,2,3,4,5,6,7,8,9], 12))



#leetcode 1 v1

# def twosum(nums, t):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i]+nums[j]==t:
#                return [i, j] 

# print(twosum([1,2,3,4,5,6,7,8,9], 5))

# class Robot:
#     def introduce_self(self):
#         print("mine name is "+self.name)


# r1 = Robot()
# r1.name = 'Том'
# r1.color = 'red'
# r1.weight = '59'

# r2 = Robot()
# r2.name = 'Aндрей'
# r2.color = 'green'
# r2.weight ='14'

# r1.introduce_self()


# class Person:
#     people_count =0

#     def __init__(self, name, surname, date ):
#         self.name = name   
#         self.surname = surname
#         self.date = date
#         Person.people_count = Person.people_count + 1
    

#     def some_fun(self):
#         print(self.name+" "+ self.surname)           


# p1 = Person("Elon", "Musk", 1970)
# p2 = Person("lili", "Musk", 2005)
# p3 = Person("lili", "Mus", 2005)

# print(p1.some_num)
# print(Robot.some_num)

# Robot.some_fun(p1)

# p2.some_fun()

# print(Person.people_count)


# class Circle:
#     PI = 3.14

#     def __init__(self, radius):
#         self.radius = radius

#     def per(self):
#         return self.radius * 2 *Circle.PI

#     def square(self):
#         return Circle.PI* self.radius**2


# c1 =  Circle(5)

# print(c1.per())
# print(c1.square())


# class Transport:
#     def __init__(self, passanger_car, truck):
#         self.passanger_car = passanger_car
#         self.truck = truck
#         print("transport item created")
    
#     def conn(self):
#         print(self.passanger_car+" "+self.truck)

# class Transport1(Transport):
#     pass

# class Transport2(Transport):
#     pass

# t1 = Transport2("MODEL 3","MODEL 4")

# t1.conn()


# print(sum([1,2,3,4,5,6,7,8,9,10],17))


# def sum(nums, target):
#     for i in range(len(nums)):
#         if target - nums[i]


# a  = {1: 'a', 2: 'b', 3: 'c'}

# print(a[1])


# book = dict()
# book[1] = 'a'
# book[2] = 'b'
# book[3] = 'c'
# book[4] = 'd'

# for key, val in book.items():
#     print(key, val)



# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i]+nums[j]==target:
#                 return [i, j]

# print(twoSum([1,2,3,4,5],7))



# complementMap ={}

# def twoSum(nums, target):
#     for i in range(len(nums)):
#         num = nums[i]
#         complement = target - num 
#         if num in complementMap:
#             return[complementMap[num],i]
#         else:
#             complementMap[complement] = i  

# print(twoSum([1,2,3,4,5],7))



# def twoSum(nums, target):
#     h = {}
#     for i, num in enumerate(nums): # 0:3  1:6  2:10
#         n = target - num #13 10 6
#         if n not in h:
#             h[num] = i #3:0 6:1 10:2
#         else:
#             return [n, num]

# print(twoSum([3,6,10,11],16))            














