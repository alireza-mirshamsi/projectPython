# kg = int(input("Enter kg: "))
# g = kg * 1000
# print("g = ", g, 'g')

# masahat mosalas
# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
# s = 1/2 * x * y
# print("s :", s)

# calculator
# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
# print(x, '+', y, "=", x+y)
# print(x, '-', y, "=", x-y)
# print(x, '*', y, "=", x*y)
# print(x, '/', y, "=", x/y)

# جدا کردن ارقام
# x = int(input("Enter x: "))
# temp = x % 10
# print(temp)
# temp = x % 100
# print(temp)


# d = int(input("Enter d: "))
# r = d * (3.14/180)
# print("R = ", r)

# مساحت دایره
# r = int(input("Enter r: "))
# temp = 3.14 * r**2
# print(temp)

# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
# z = int(input("Enter z: "))

# sum_ = x+y+z
# temp = sum_/3
# print("avg : ", round(temp, 2))

# -- String --
# x = "C:\Download\\new"
# y = """
# alireza
# mirshamsi
# """
# print(x)

# print(x+" hello")
# print(y*2)

# [0,1,2,3,4,5]
# [-5,-4,-3,-2,-1]

# s = "alireza mirshamsi"
# print(s[5], s[-1], "\n")
# print(s[2:5])
# print(s[0:5:2])
# print(s[::-1])

# s = "Alireza Mirshamsi"
# print(s.upper())
# print(s.lower())
# print(s.count("a"))
# print(s.startswith("r"))
# print(s.find("a"))
# print(s.find("a"))
# print(s.isalnum())
# print(s.isnumeric())  # آیا همشون عدد است یا نه

# l = ['A', 'B', 'C', '8']
# print(s.join(l))

# h = "alireza, mirshamsi, 1377"
# print(h.split(','))
# print(h.replace("alireza", "mohammad"))
# print(h.strip('a'))  # حروف اول را حذف میکند
# print(s.capitalize())

# print(ord('*'))
# print("char: \u2Dbb")
# print("ali reza dot\rreza")

# x = 5
# y = 7.545
# h = {'x': 5, 'y': 8, 'z': 2.66}
# print("x is {0}\ny is {2}\nz is {1}".format(5, y, 5+7))

# x = "reza"
# f = 4.65
# print(F"x is {x}\ny is {f}")
# print(F"x is {x.replace('a','-')}")

# x = 5
# print(f"{x:-<15}{x:-<15}5\n{x:-<15}{x:-<15}5\n")

# s = "reza is bad boy"
# c = input("enter a char: ")
# print(s.count(c))

# s = input("enter string: ")
# s = s.rstrip()
# i = s.rfind(" ")
# print(s)
# print(s[i+1:])

# s1 = input("enter string1: ")
# s2 = input("enter string2: ")
# print(s2 in s1)

# s = input("enter string: ")
# print(s.replace(" ", "").replace("\t", ""))

# phone = input("Enter your phone: ")
# print(phone.lstrip("0"))

# ------ tamrin 1 -----
# s = input("Enter string: ")
# sentences = s.count(".")+s.count("?")
# characters = len(s)
# print("sentences: ",sentences)
# words = s.count(" ")+1
# print("word: ", words)
# print("characters", characters)

# ------ tamrin 2 -----
# ch = input("Enter your char: ")
# print(ord(ch))

# ------ tamrin 3 -----
# phone = input("Enter your number: ")
# print(phone.isnumeric())
# print(phone.isdigit())
# print(phone.isdecimal())

# ---- list ----
# name = ["reza", "ali",1,1+3j]
# number = list("1234")
# s = "a l i r e z a"
# ch = s.split(" ")
# print(name, type(name))
# print(number,type(number))
# print(ch, type(ch))

# l1 = [1,2,3]
# l2 = [1,2,3]
# # l2=l1
# l2=l1[:] # or l2 = l1.copy()

# shallow copy => l2 = l1.copy()
# Deep copy    => l2 = copy.deepcopy(l1)

# l2[0]=0
# print(l1)
# print(l2)

# x = [1,2,['a',[2.2,1.1],'b']]
# print(x[2][1])

# l = [1,2,3,4,5,6]
# l[2:5] = ['a','b','c']
# a, b, *c = [1,2,3,4,5,6]
# print(l)
# print(a)

# ---- tuple ----
#  تاپل ها غیر قابل تغییر هستند
# x = (1,2,3,"reza",[1,2],(3,4))
# print(x)

# ---- dictionary ----
# keys => مقادیر غیرقابل تغییر
# values => مقادیر قابل تغییر
# d = {"a":1, "b": 2}
# f = {(1,2,3):1,"b":2}
# print(d["a"])
# print(f[(1,2,3)])
# print(d.keys())
# print(d.values())
# print(f.keys())
# print(f.values())
# print(d.items())

# d = {"a":1, "b": 2,"x":5}
# del d["a"]
# x = d["b"]
# print(sorted(d.keys()))
# print(d)
# y = dict([("a",25),("b",30)])
# print(y)
# k = {
#     "169": {"name": "alireza", "age": 25},
#     "172": {"name": "hasan", "age": 22},
# }
# l = ["a","b","c"]
# v = [1,2,3]
# i = dict(zip(l,v))
# print(i)

# ---- Collection ----
# s = {1,2,5,9}
# t = (1,2)
# t = t + (5,)
# print(s)
# s.add(6)
# # print(t)
# i = input("name : ")
# s.add(i)
# print(s)
# k = set("alireza mirshamsi")
# print(k)

# p = {15,5,6,8}
# q = {14,12,8,9}
# print(p-q)
# print(p | q)
# print(p & q)
# print(p ^ q) # (p | q) - (p & q)
# print(p.difference(q))
# print(p.union(q))
# print(p.intersection(q))
# print(p.issuperset(q)) # p > q
# print(p.issubset(q))

# -----  practice  -----
# marks = []
# name = input("name: ")
# marks.append(name)
# fizik = float(input("nomre fizik: "))
# marks.append(fizik)
# riazi = float(input("nomre riazi: "))
# marks.append(riazi)
# adabiat = float(input("nomre adabiat: "))
# marks.append(adabiat)
# avg = (marks[1] + marks[2] + marks[3]) / 3
# print(avg)

# --------- 2 ----------
# phone = input("Enter: ")
# digit_list = list(phone)
# print(digit_list)

# --------- 3 ----------
# marks = {}
# name = input("name: ")
# m = float(input("nomre: "))
# marks[name] = m

# name2 = input("name: ")
# m2 = float(input("nomre: "))
# marks[name2] = m2
# print(marks)

# --------- 3 ----------
# s = input("Enter string:")
# l = set(s)
# print("len:", len(l))
# print("character: ", l)

# --------- 4 ----------
# dictionary = {}
# meanings = []
# key = input("Enter keyword: ")
# m = input("meaning: ").split(",")
# dictionary[key] = m

# key = input("Enter keyword: ")
# m = input("meaning: ").split(",")
# dictionary[key] = m
# print(dictionary)

# word = input("Enter keyword: ")
# print("meaning: ", dictionary.get(word))

# --------- 5 ----------
# phone1 = ["0921", "0903", "0914"]
# phone2 = ["0917", "0919", "0914"]
# s = list(set(phone1 + phone2))
# print(s)

# ------ boolean & noneType
# s = None
# print(type(s))
# None, False, (), {}, [], "", شی صفر => False mibashad

# x = input("x,y,z: ").split(",")
# print("-"*30)
# print("x=",x)

# ---- if -----
# mark = int(input("Enter number:"))
# if mark > 12:
#     print("pass")
# else:
#     print("rejected15")

# ----- practice 1 ------
# x = int(input("Enter x: "))
# if x%2==0 and x%5==0:
#     print("yes")
# else:
#     print("no")

# l = [1,2,3,4]
# print(min(l, default=0))

# ---- loop ------
# n = 0
# while n < 100:
#     if(n % 2 == 0):
#         print(n,"\n")
#     n += 1

# row = 1
# while row <= 5:
#     print("*"*row)
#     row += 1

# n = int(input("Enter number: "))
# i=1
# while n>=i:
#     if n % i == 0:
#         print(i)
#     i += 1

# --- fibo ---
# i = 1
# a,b = 0, 1
# while i <= 20:
#     print(a)
#     a,b = b, a+b
#     i += 1

# n = float(input("n: "))
# m = n
# while True:
#     s = input("Do you continue? ")
#     if s.lower() == "no":
#         break
#     n = float(input("n: "))
#     if n < m:
#         m = n

# print(m, "is smallest number!")

# n = int(input("n: "))
# i=2
# if n > 1:
#     while i < n:
#         if n % i == 0:
#             print(n, "is not a prime number!")
#             break
#         i += 1
#     else:
#         print(n, " is a prime number!")
# else:
#     print("is not prime number!")

# i=1
# while i <= 10:
#     j=1
#     while j <= 10:
#         print("\t", j)
#         j += 1
#     print(i)
#     i += 1

# l = ["reza", "neda", "sahel", "ali"]
# i = 0
# while i < len(l):
#     print(l[i])
#     i += 1

i=1
while i <= 10:
    j = 1
    while j <= 10:
        print(i*j, end="\t")
        j += 1
    print()
    i += 1
