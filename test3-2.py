""" x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)  
print(x is z)  
print(x is not y)  """

""" a = 5
b = 5

print(a is b)
print (a is not b)
 """
""" a = 3
b = 3.0

print(a == b)
print(a is b)
print(a is not b) """ 

""" # print (5 == 5.0)
# print (5 is 5.0) """

""" a = [3, 5, 1]
b = a

print (a is b)

a[0] = 2

print (a, b)

print (a is b) """


""" x= 2 ** 3 ** 2
print(x)

print (2 + 3 *4)
print (10 / 5/ 2)
print (2 ** 3 ** 2)
print (2 ** (3 **2))
print (10 % 3 % 2)
print (1+ 2 > 3 and 4 - 1 <2)
# a = not False and True
# a = not True or False and True
# a = 1 & 2 | 3 ^ 4
# a = 5 in [3, 4, 5] or 2 not in [1, 2, 3]
# a = 2 * -3 // 2
# a = 1 == 2 != 3
 """

""" x = 10

if x > 0:
    print("x is positive")

elif x < 0:
    print("x is negative")
    
else:
    print("x is zero") """
 
 #iF 짝수 홀수   
""" num = 23
if num % 2 == 0:
    print("짝수")
else:
    print("홀수") """
""" """ 
"""  # if 두수 비교 
x = 1 
y = 2  
if x == y:
    print ("같습니다")
else:
    print("다릅니다") 
 """
""" 
# if a or b  인지
char = "a"
if char == "a" or char == "b":
    print("'a' 또는 'b'입니다.")
else:
    print("'a' 또는 'b'가 아닙니다.") """

""" fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
     """

""" my_list = [[1,2,3], [4,5,6], [7,8,9]]

for row in my_list:
    for num in row:
        print(num)
  """
  
"""   # 0~9 까지 출력
for i in range(10):
    print(i) """

"""  # 문자열을 한글자씩 (for 낱말 출력)
for char in "phython":
   print(char) """
 
"""  """ # for 역순출력 (reversed)
 # fruits = ["apple", "banana", "cherry"]

""" for fruit in reversed(fruits):
    print(fruit) """
""" # for 역순 출력(sorted)     
for fruit in sorted(fruits, reverse=True):
    print(fruit)
    
# for 구구단

for i in range(1, 10):
    for j in range(1, 10):
    print(i, "x", j, "=", i*j) """
    
""" # for else 문

rng = [5, 8, 3, 1, 6]

for i in rng:
    print("element : ",i)
else :
    print("end process") """
    
""" for i in range(10):
    if i == 7:
        print("break")
        break
    elif i ==1:
        print("continue ", i)
        continue
    else:
        print("pass", i)
        pass
    print(i)   """  

""" # while 1~5 출력    
i = 1
while i <= 5:
    print(i)
    i += 1 """
         
""" # while 0~9 출력
i = 0
while i <= 9:
    print(i)
    i += 0 """

""" # while 문자열 낱말 출력
str_word = "python" 
idx = 0

while idx < len(str_word):
    print(str_word[idx])
    idx += 1 """
 
""" sum = 0
i = 1

while i <= 10:
     sum += i
     i += 1
     
print(sum) """

""" # 1-100까지의 짝수, 홀수 출력하기
i = 1

while i <= 100:
    if i % 2 == 0:
     print("짝수 : ", i)
    elif i % 2 == 1:
        print("홀수 : ", i)
    i += 1 """
    
# while 7의 배수만 출력
i = 1

while i <=100:
    if i % 7 == 0:
        print(i)
    i += 1
    
