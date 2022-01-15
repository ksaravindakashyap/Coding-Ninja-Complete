# Check Number
n = int(input())

if(n>0):
    print("Positive")
elif(n==0):
    print("Zero")
else:
    print("Negative")

# Sum of n Numbers
n = int(input())
sum=0
i=0
while(i<=n):
    sum+=i
    i+=1
print(sum)

# Sum of Even Numbers

n = int(input())
sum=0
for i in range(1,n+1):
    if(i%2==0):
        sum+=i

print(sum)



# Fahrenheit to Celsius

s = int(input())
e = int(input())
w = int(input())
temp=0

while s <= e:
    temp = int(((s-32)*(5/9)))
    print(s,"\t",temp)
    s+=w