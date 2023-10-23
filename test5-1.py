""" #datertime
from datetime import daterime as dt

#현재시간 출력
print(dt.now())

#특정 시간대의 현재 시간 출력
#from pytz import timezone
# tz = timezone('Asia/Seoul)
#tz = timezone('UTC')
#print("timezone: ", dt.now(tz))

#문자열을 날짜로 변환
date_string = '2021-7-8'
date_object = dt.strptime(date_string, '%Y-%m-%d')
print(date_object)

#날짜를 문자열로 변환
date_object = dt.now()
date_string = date_object.string('%Y-%m-%d')
print(date_string) """

""" import mod.utils as mu

dtnow = mu.get_dtnow()
print(dtnow)

#print(dt.now())
dtnow = mu.get_dtnow()
print(dtnow)

ret = mu.cvt_time2str("2023-09-25")
print(ret)

res = mu.cvt_str2time()
print(res)
 """
 
"""  # os 모듈 확인
import os

#현재 작업 디렉토리 출력
print(os.getcwd())

#디렉토리 변경
os.chdir('../')

#변경된 디렉토리 출력
print(os.getcwd())

#파일 목록 출력
print(os.listdir())

#디렉토리 삭제
os.mkdir('new_directory')
print(os.listdir())

#디렉토리 생성
os.mkdir('new_directiry')
print(os.listdir())
 """
""" import mod.utils as mu
import os

print(mu.get_curdir())

pname = "python"
mu.os_mkdir(pname)
print(os.listdir())

os.rmdir(pname)
print(os.listdir())  """

""" import sys

print(sys.version)
print(sys.argv)
 """
 
#5-1 데이터 구조- 알고리즘
#스택에 값 넣기
""" list = []
list.append (1)
list.append (2)
list.append (3)
list.append (4)
list.append (5)
#스택의 상태 확인
print(list) #[1,2,3]
#스택에서 값 빼기
top = list.pop()
print(top) #3
print(list)
print(len(list)) """

#큐 선입선출
#빈 큐 생성
""" queue = [] 

#큐에 값 넣기
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

#큐의 상태 확인
print(queue) # [1,2,3]

#큐에서 값 빼기
front = queue.pop(0)
print(front) #1
print(queue)
print(len(queue)) """

""" # enqueue / dequeue
qlist = []

def enqueue(qlist, data):
    qlist.append(data)
    
def dequeue(qlist):
    data = qlist[0]
    del qlist[0]
    return data

enqueue(qlist,1)
print(qlist)
enqueue(qlist,2)
print(qlist) 
enqueue(qlist,3)
print(qlist) 
dequeue(qlist)
print(qlist)
dequeue(qlist)
print(qlist) 
 """

#O(1)
arr = [1 ,2, 3, 4, 5] 

def ret_01(idx):
    return arr[idx]

print(ret_01(2))

#0(1) 시간
import time
arr = [1 ,2, 3, 4, 5] 

def ret_01(idx):
    return arr[idx]

start = time.time()
print(ret_01(2))
end = time.time()
print(f"{end - start : 5f} sec") 

# O(n)
""" import time
arr = [1, 2, 3, 4, 5]

def print_elements(arr):
    for elem in arr:
        print(elem)
        
start  = time.time()      
print_elements(arr)
end = time.time()
 
print(f"{end - start : 5f} sec") """

""" def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    print(left, right)
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

my_list = [1, 2, 3, 4, 5]

result = binary_search(my_list, 4)
if result != -1:
    print(f"요소가 {result}번째 인덱스에 있습니다.")
else:
    print("요소를 찾을 수 없습니다.")
 """
 
"""  #O(m2)
import time
def mul_for():
    for i in range(5) :
        for j in range(5) :
            print(i,j)
            
start = time.time()
mul_for()
end = time.time()
print(f"{end - start : 5f} sec") """

#버블정렬
""" def bubble_sort(arr):
    N = len(arr) #데이터의 갯수 : 5
    for i in range(N): #0,1,2,3,4
        #print(i,arr)
        for j in range(N-i-1): #4,3,2,1
            if arr[j] > arr[j+1]: #arr[4] arr[5]
               #print(arr[j+1], arrp-[j])
              arr[j], arr[j+1] = arr[j+1], arr[j]
            print(i, j , arr, arr[i], arr[j])
            
    return arr
lrr = [1, 9, 2, 7, 5]
print(bubble_sort(lrr)) #[-1, 0, 9, 11, 45] """

#퀵소트

""" def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2] #가운데 피넛으로 선택
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print("piv", pivot)
    print("left",left)
    print("mid",middle)
    print("rgt",right)
    
    return quick_sort(left) + middle + quick_sort(right)

my_list = [1, 9, 6, 4, 5, 7, 3, 2]
print(len(my_list))

sorted_list = quick_sort(my_list)

print(sorted_list) """

""" import requests
 
res = requests.get("https://www.google.co.kr/")
print(res)
print(res.contents)
 """
#numpy
""" import numpy as np

#1차배열 생성
a = np.array([1, 2, 3])
print(a)
 
#2차 3행 배열, 0으로 초기화
b = np.zeros([2,3])
print(b)

#2차 3행 배열, 1로 초기화
c = np.ones((2,3))
print(c)

d = np.array([1, 2, 3])
e = np.array([4, 5, 6])

#배열간 연산
f = d + e
g = d - e
h = d * e
i = d / e

print(f)
print(g)
print(h)
print(i)
 """

#pandas
""" import pandas as pd

data = {'Name': ['John', 'Jane', 'Mike', 'Sarah'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)
print(df['Age'].describe())
print(df.sort_values(by= 'Age', ascending=False))
print("===============")
print(df.sort_valuse(by='Age',ascemding=True))
print("===============")
print(df.sort_values(by='Name', ascending=True))
 """

""" #matplotlib

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 8, 6, 4, 2]

plt.plot(x, y)

plt.xlabel('time')
plt.ylabel('n')
plt.title('Epython')

plt.show()
 """