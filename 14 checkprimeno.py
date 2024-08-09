# num =25
# flag= False
# if num ==1:
#     print(num)
# elif num>1:
#     for i in range(2,num):
#         if(num%i) == 0:
#             flag=True
#             break
# if flag:
#     print("prime",num)
# else:
#     print("not prime",num)
    
    
num=407
if num==1:
    print(num)
elif num>1:
    for i in range(2,num):
        if(num%i)==0:
            print(num,"is not prime")
            print(i,num)
            break
        else:
            print(num,"is a prime no")
else:
    print(num)
    