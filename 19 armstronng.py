num= int(input("enter a no:"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+= digit**3
    temp//=10
    
if num==sum:
    print(num)
else:
    print(num)