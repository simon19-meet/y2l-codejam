a=1
sum=0

while a<=1000:
    sum+=a**a
    a+=1
print(sum%10000000000)