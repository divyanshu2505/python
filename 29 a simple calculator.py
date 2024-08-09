def add(x,y):
    return x+y
def substract(x,y):
    return x-y

def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print("select operation")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")

while True:
    choice = input("1,2,3,4")

    if choice in ('1','2','3','4'):
        try:
            num1= float(input("first"))
            num2= float(input("second"))
        except ValueError:
            print("invalid input Please enter a no")          
            continue

        if choice=='1':
            print (num1,"+",num2,"=",add(num1,num2))
        elif choice =='2':
            print(num1,"-",num2,"=",substract(num1,num2))
        elif choice =='3':
            print(num1,"*",num2,"=",multiply(num1,num2))
        elif choice =='4':
            print(num1,"/",num2,"=",divide(num1,num2))
            
        next_calculation = input("yes/no")
        
        if next_calculation=="no":
            break
    else:
        print("invalid Input")
        