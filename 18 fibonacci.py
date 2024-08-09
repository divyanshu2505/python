nterms= int(input("how many times"))
n1,n2=0,1
count =0
if nterms<=0:
    print("negative")
elif nterms==1:
    print(nterms)
    print(n1)
else:
    print("fibonacci")
    while count<nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        count+=1
        