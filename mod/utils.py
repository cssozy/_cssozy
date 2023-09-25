import math
import random
from datetime import datetime as dt


def mt_sqrt(x) :
      return math.sqrt(x)

def mt_sinpi() :
    return math.sin(math.pi / 2)

def mt_elog() :
    return math.log(math.e)

def mt_exp(x) :
   return math.exp(x)

def mt_pi() :
    return math.pi

def rd_int(x,y) :
    return random.randint(x,y)

def rd_list(this) :
    return random.choice(this)

def rd_rd() :
    return random.random()

def rd_nmvar() :
    return random.normalvariate(0,1)

def get_dtnow() :
    return dt.now()

def cvt_time2str(objtime) : 
     return dt.strptime(objtime,"%Y-%m-%d")
 
def cvt_str2time(strtime) :
     return dt.strftime("%Y-%m-%d")
  
  
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
print(date_string)
