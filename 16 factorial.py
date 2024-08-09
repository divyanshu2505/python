# num= 5
# fact=3
# if num<0:
#     print("sorry")
# elif num==0:
#     print("fact")
# else:
#     for i in range(1,num+1):
#         fact=fact*i
#     print(fact,num)

# solve by recursion
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
    
num= 7
result= factorial(num)
print("the factorial ",num,result)