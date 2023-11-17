#dataframe
""" import pandas as pd

df = pd.DataFrame([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]])
print(df)
print("\n--------------------\n")

print(df[1])
print("\n--------------------\n")

print(df[1][1]) 
print("\n--------------------\n")
print(df[2][2]) 
 """
#dataframe 출력
""" import pandas as pd

data = {
    "x" : [10, 15, 20],
    "y" : [50, 55, 60],
    "z" : [100, 110, 120]
}

idx = ["x축", "y축", "z축"]

fr = pd.DataFrame(data, index=idx)

#print(fr)

#print(fr["x"])
#print(fr["z"])

#print(fr.x)
#print("\n--------------------\n")
#print(fr.y)

#print(fr.iloc[2])

print("\n--------------------\n")
print(fr.loc["y축"])

print("\n--------------------\n") """

#열추가
"""import pandas as pd
frs = pd.DataFrame(fr,columns=["x", "y", "z", "t"])
print(frs)

frs["t"] = [60, 120, 180]
print(frs)
print("\n-----------------------\n")

#행추가
frs.loc["t축"] = [100, 200, 300, 400]
print(frs)

#행수정
print("\n-----------------------\n")
frs.loc["t축"] = [500, 600, 700, 800]
print(frs)

#행 삭제
print("\n-----------------------\n")
#frs.drop("x", axis=1, inplace=True)
frs.drop("x", axis=1, inplace=False)
print(frs)

# 열 삭제
print("\n-----------------------\n")
frs.drop("x축", inplace=True)
print(frs) """

#컬럼추가 
""" import pandas as pd

dt = [[1,10,100],[2,20,200],[3,30,300]]
col = ["x","y","z"]
idx = ["x축","y축","z축"]
df = pd.DataFrame(data=dt,index=idx,columns=col)

print(df)
print(df["x"])
print(df["y"])
print("\n--------------------\n")
print(df.loc["x축"])
print(df.loc["y축"])

print(df["col1"])
print(df + 1)
print(df.div(100))
print(df / 100)
print("\n------------------------\n")
print(df.mul(100))
print(df * 100)

# 같은 인덱스끼리 연산
dt2  = [[0],[2],[3]]
df2 = pd.DataFrame(data=dt2,index=["x축","y축","z축"],columns=["y"])

print(dt2)
print(df.div(df2))
print(df.mul(df2))
print(df.div(df2, fill_value =1))
df.div(df2) """

#컬럼추가 2
import pandas as pd

dt = [[1,10,100],[2,20,200],[3,30,300]]
col = ["col1","col2","col3"]
idx = ["삼성","현대","LG"]


df = pd.DataFrame(data=dt,index=idx,columns=col)

print(df)
#print(df["col1"])
#print(df["y"])

print("\n--------------------\n")
print(df.loc["현대"])
#print(df.loc["y축"])

print(df["col1"])
print(df + 1)
print(df.div(100))
print(df / 100)
print("\n------------------------\n")
print(df.mul(100))
print(df * 100)

# 같은 인덱스끼리 연산
dt2  = [[0],[2],[3]]
df2 = pd.DataFrame(data=dt2,index=["삼성","현대","LG"],columns=["col2"])

print(dt2)
print(df.div(df2))
print(df.mul(df2))
print(df.div(df2, fill_value =1))
df.div(df2)