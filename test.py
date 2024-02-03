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

#   <<<<<<< HEAD
#     temp=+1


# 저장 용량의 단위
# 1 bit
# 8bit = 1byte
# 1000byte = 1Kbyte
# 1000Kbyte = 1Mbyte
# 1000Mbyte = 1Gbyte
# 1000Gbyte = 1Tbyte
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

#(6)
# a , b = map(int,input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)

#(7)
# a = input()
# print(a+"??!")

#(8)
# a = int(input())
# print(a-543)

#(9)
# a , b, c = map(int,input().split())
# print((a+b)%c)
# print(((a%c)+(b%c))%c)
# print((a*b)%c)
# print(((a%c)*(b%c))%c)

#(10)
# a= int(input())
# b= int(input())
# res = a*b
# while b>0:
#    print(a*(b%10))
#    b=b//10
# print(res)

#(11)
# a, b, c = map(int,input().split())
# print(a+b+c)

#(12)
# print("\\    /\\")
# print(" )  ( ')") 
# print("(  /  )")
# print(" \\(__)|")

#(13)
# print("|\\_/|")
# print("|q p|   /}")
# print("( 0 )\"\"\"\\")
# print("|\"^\"`    |")
# print("||_/=\\\\__|")
#(14)
# a , b = map(int,input().split())
# if a > b:
#    print(">")
# elif a < b:
#    print("<")
# else :
#    print("==")

#(15)
# score = int(input())
# if 100>= score >= 90:
#    print("A")
# elif score >= 80:
#    print("B")
# elif score >= 70:
#    print("C")
# elif score >= 60:
#    print("D")
# else :
#    print("F")

#(16)
# year = int(input())
# if year%4==0 and year%100!=0:
#    print("1")
# elif year%400==0:
#   print("1")
# else :
#    print("0")

#(17)
# x = int(input())
# y = int(input())
# if x>0 and y>0 :
#    print("1")
# elif x<0 and y>0:
#    print("2")
# elif x<0 and y<0:
#    print("3")
# else :
#    print("4")

#(18) 알람시계(2884)
# h, m = map(int,input().split())
# if m>=45:
#     print(h, m-45)
# else:
#     if h==0:
#         print(h+23, m+15)
#     else:
#         print(h-1, m+15) 
#(19)오븐시계(2525)
# a, b = map(int,input().split())
# c = int(input())
# h=0
# m=0
# h=c//60
# m=c%60
# a= a+h
# b= b+m
# if b>=60:
#     a=a+1
#     b=b-60
# if a>=24:
#     a=a-24
# print(a, b)
#(20)
# a, b, c = map(int,input().split())
# if a==b==c:
#    print(10000+a*1000)
# elif a==b:
#   print(1000+a*100)
# elif b==c:
#    print(1000+b*100)
# elif a==c:
#    print(1000+a*100)
# elif a>b>c or a>c>b:
#    print(a*100)
# elif b>c>a or b>a>c:
#    print(b*100)
# else :
#    print(c*100)

#(21) 구구단(2739)
# n = int(input())
# for i in range(1,10,1):
#    print(n,'*',i,'=',n*i)

#(22) a+B-3(10950)
# t = int(input())
# for i in range(t):
#    a, b = map(int, input().split())
#    print(a+b)

#(23)
# n = int(input())
# res=0
# for i in range(n+1):
#     res = res+i
# print(res)

#############복습#######
# (10926)
# a = input()
# print(a+"??!")

#(2588)
# a = int(input())
# b = int(input())
# res=a*b
# while b>0:
#     print(a*(b%10))
#     b = b//10
# print(res)

#(10171)
# print("\\    /\\")
# print(" )  ( \')")
# print("(  /  )")
# print(" \\(__)|")

#(10172)
# print("|\\_/|")
# print("|q p|   /}")
# print("( 0 )\"\"\"\\")
# print("|\"^\"`    |")
# print("||_/=\\__ |")

#(2884)
# h, m = map(int,input().split())
# if m>=45:
#     print(h, m-45)
# else:
#     if h==0:
#         print(h+23, m+15)
#     else:
#         print(h-1, m+15)

#(2525)
# a, b = map(int, input().split())
# c = int(input())
# h = 0
# m = 0
# h = c//60
# m = c%60
# a = a+h
# b = b+m
# if b>=60:
#     a = a+1
#     b = b-60
# if a>=24:
#     a=a-24
# print(a, b)

#(2739)
# n = int(input())
# for i in range(1, 10):
#     print(n, "*", i, "=", n*i)

#(8393)
# n = int(input())
# res = 0
# for i in range(n+1):
#     res= res+i
# print(res)

