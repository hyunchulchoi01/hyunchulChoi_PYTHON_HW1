#!/usr/bin/env python
# coding: utf-8

# In[1]:


## 함수 선언 부분 ##
def add_data(friend) :
    
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend
    
    
def insert_data(position,friend) :
    
    if position < 0 or position > len(katok) :
        print("데이터를 추가할 범위를 벗어났습니다.")
        return
    
    katok.append(None)
    kLen =  len(katok)
    
    for i in range(kLen-1,position,-1) :
        katok[i] = katok[i-1]
        katok[i-1] = None
        
    katok[position] = friend
    
def delete_data(position) :
    
    if position < 0 or position+1 > len(katok) :
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return
    
    kLen = len(katok)
    katok[position] = None #데이터 삭제
    
    for i in range(position+1, kLen) :
        katok[i-1] = katok[i]
        katok[i] = None
        
    del(katok[kLen-1]) # 배열의 맨 마지막 위치 삭제
    
##전역 변수 선언 부분 ##
katok = []
select = -1

##메인 코드 부분##
if __name__=="__main__" :
    
    while (select !=3) :
        
        select = int(input("선택하세요(1:추가, 2:삭제, 3:종료)-->"))
        
        if(select==1) :
            data = input("추가할 데이터-->")
            add_data(data)
            katok.sort()
            print(katok)
        elif (select == 2) :
            pos = int(input("삭제할 위치-->"))-1
            delete_data(pos)
            print(katok)
        elif (select ==3) :
            print(katok)
            exit
        else :
            print("1~3 중 하나를 입력하세요.")
            continue


# In[ ]:




