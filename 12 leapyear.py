year =2000
if(year%400==0)and (year%100==0):
    print("leap yar",year)
elif(year%4 ==0)and(year%100!=0):
    print(year)
else:
    print("not",year)