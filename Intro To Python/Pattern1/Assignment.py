# Number Pattern 1
n = int(input())

i=1
while i<=n:
    j=1
    #start_char = chr(ord('A') + i-1)
    while j<=i:
        #charP = chr(ord(start_char) + j -1)
        print(1,end="")
        j+=1
    print()
    i+=1


# Number Pattern 2
n = int(input())

print(1)
i=1
while i<=n-1:
    j=1
    while j<=i:
        if i==j:
            print(i,end="")
            print(i)
        else:
            print(i,end="")
            print((i-1)*'0',end="")
            print(i)
            break
        j+=1
    print()
    i+=1

# Number Pattern 3

n= int(input())
i=1
print(1)
while i<n:
    j=1
    while j<=i:
        if(i==j):
            print(i,end="")
            print(i)
        else:
            print(1,end="")
            print((i-1)*'2',end="")
            print(1)
            break
        j+=1
    # print()
    i+=1

# Number Pattern

n = int(input())
i=1
temp=n
while i<=n:
    j=1
    while j<=temp:
        print(j,end="")
        j+=1
    print()
    temp-=1
    i+=1


# Alpha Pattern

n = int(input())

i=1
while i<=n:
    j=1
    start_char = chr(ord('A') + i-1)
    while j<=i:
        # charP = chr(ord(start_char) + j -1)
        print(start_char,end="")
        j+=1
    print()
    i+=1