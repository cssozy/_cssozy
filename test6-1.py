#삼각형 출력
#02 직각삼각형
""" for i in range(1,6):
    print("*" * i)
     """
#01 역직각삼각형
""" for i in range(5, 0, -1):
    print("*" * i) """
    
#03 이등변삼각형
""" for i in range(1,6):
    spaces = " " * (6 - i) #앞에 있는 공백
    stars = "*" * (2 * i -1)
    print(spaces + stars)
     """
#04 다이아몬드 -> range를 1-6까지 정의를 하고 역순으로 한번 더 하기
for i in range(1,6):
    spaces = " " * (6 - i) #앞에 있는 공백
    stars = "*" * (2 * i -1)
    print(spaces + stars) #// 이등변삼각형
for i in range(6, 0 ,-1):
    spaces = " " * (6 - i)
    stars = "*" * (2 * i -1)
    print(spaces + stars) 
    
#5x5 출력
#01 - 정상출력
""" num = 0 
line = []
for i in range(5):
    for j in range(5):
        num += 1
        line.append(num)
    print(line)
    line = [] """
#02 - 세로출력
""" num = 0
line = []
for i in range(1,6):
    for j in range(1,6):
        num = ((j-1) * 5) + i #시작이 1이여야 하므로 +i, +5가 차이 나야하므로 *5
        line.append(num)
    print(line)
    line = [] """
#03 - 역출력
""" num = 26
line = []
for i in range(5):
    for j in range(5):
        num -= 1
        line.append(num)
    print(line)
    line = []
 """
 #가위바위보 게임
""" import random
def get_computer_choice():
    choices = ['1' ,'2','3']
    return random.choice(choices)

def determine_winner(user_choice):
    pcnum = get_computer_choice()
    print(user_choice, pcnum)
    
    if user_choice == pcnum :
        print('무승부')
        return
    elif (""
        (user_choice == '1' and pcnum == '3') or
        (user_choice == '2' and pcnum == '1') or
        (user_choice == '3' and pcnum == '2')
    ):
        print("승")
        return
    else:
        print('패')
        return
    
print("1 : 가위")
print("2 : 바위")
print("3: 보")
print("1~3 숫자를 입력하세요!")
chnum = input()
#pcnum = get_computer_choice()
    
determine_winner(chnum)
      """

#파일처리
#파일생성
#file = open("temp,txt", "w")
""" file = open("temp.txt", "w")
file.close()
file = open("temp.txt", "r")
file.close()
file = open("temp.txt", "a")
file.close()
file = open("temp.txt", "r+")
file.close() """

#파일쓰기
"""file = open("temp.txt", "w")

file.write("hello")
file.write("world")

file.close() """
#0 ~ 100까지 라인별로 파일 출력
"""f ile = open("temp.txt", "w")

for i in range(100) :
    file.write(f"{i}\n")

file.close()

#“c:/User/Catholic/temp.txt” 경로에 파일 생성
file = open("c:\\User\\Catholic\\temp.txt","w")
for i in range(100) :
    file.write(f"{i}\\n")
    
file.close()

#추가쓰기
f = open("c:\\User\\Catholic\\temp.txt" , "a"\n)

f.write("hello\n")
f.write("wolrd")

file.close()
 """
#파일읽기
""" file = open("temp.txt","r")
res = file.read()
print(res)

file.close() """
#다른경로 파일 읽기
""" f = open("c:\\User\\Catholic\\temp.txt" , "r")
res = f.read()
print(res)
f.close()
 """
#readline 한라인씩 읽기
#f = open("temp.txt" , "r")
""" f = open("temp.txt" , "r")
res = f.readlines()
print(res) 

f.close() 
 """
#readline 읽기
""" f = open("temp.txt", "r")
line = f.readlines()
for l in line :
    print(1)

f.close() """
#file object
""" f = open("temp.txt", "r")
for line in f : 
    print(line)
    
f.close() """

