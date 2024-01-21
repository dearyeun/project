################################################################### 2024.01.14
# a=[1,2.5,"a",True,[1,2]]
# b=[[[]]]
# print(a)

# len(a[4])

# a={'test':'python'}
# print(a)
# print(a['test'])
# a['list']=[1,5.5]
# print(a)
# print(a['list'])

# test=[1,2,2,5,1,6,7,6,0,0,2,2]
# temp=list(set(test))
# print(test)
# print(temp)

# temp란 변수에 숫자를 입력받아서 짝수면 "짝수입니다." 홀수면 "홀수입니다."를 출력하시오
# temp =int(input())
# if temp %2==0:
#     print("짝수입니다")
# else:
#     print("홓수입니다")


# import datetime as d
# curr1=d.datetime.now()
# temp=[0]*10000000
# print("length = ",len(temp))
# for i in range(len(temp)):
#     pass
# curr2=d.datetime.now()

# print(curr1)
# print(curr2)
################################################################### 2024.01.14

# a=1
# b='0'
# c="abc"

# print(a,b+'0',c,3,sep=',', end=";\n")
# print(a,b+'0',c,3)

# # print 옵션 = sep, end

# a=list(map(int,input().split(",")))
# print(a)


# nums=[5,8,7,5,65,7,41,5]
# res=0
# # for i in range(len(nums)):
# #     res+=nums[i]

# for i in nums:
#     res+=i

# print(res/len(nums))

# for i in range(10,-1,-1):


# 숫자들을 콤마(,) 기준으로 입력받아
# 모든 원소들의 곱을 출력하시오
# 12,54,82,56,8


# nums = list(map(int,input().split(','))) 
# res=1
# for i in nums:
#     res*=i
# print(res)

# temp=[]
# print(temp)
# temp.append(2)
# print(temp)
# temp.append(1)
# print(temp)
# temp.append(8)
# print(temp)
# # temp.pop(0)
# # print(temp)
# temp.append(7)
# print(temp)
# temp.append(10)
# print(temp)
# # temp.sort()
# # print(temp)
# # temp.sort(reverse=True)
# # print(temp)
# temp=sorted(temp,key=lambda x:(x[1][2],-x[0],x[2]))
# print(temp)
# temp=sorted(temp,key=lambda x:-x)
# print(temp)

# temp=0
# while True:

#     if temp%3==0:
#         break

<<<<<<< HEAD
#     temp=+1


##########################숙제##################

#1단계

#(1)

# print("Hello World!")

#(2)

# a , b = map(int,input().split())
# print(a+b)

#(3)

# a , b = map(int,input().split())
# print(a-b)

#(4)
# a , b = map(int,input().split())
# print(a*b)

#(5)
# a , b = map(int,input().split())
# print(a/b)
