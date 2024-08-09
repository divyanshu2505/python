terms= 10
result= list(map(lambda x:2**x,range(terms)))
print("total",terms)
for i in range(terms):
    print(result[i])
    