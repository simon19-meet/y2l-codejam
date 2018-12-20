sum=2
a=3
flag=True
while a<1000000:
    flag=True
    if a%2!=0:
        for i in range(2,a/2 +1):
            if a%i==0:
                flag=False
                break
    if a%2!=0 and flag:
        sum+=a
print(sum)