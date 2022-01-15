# Code : Square Pattern

n = int(input())

i=0
while i<n:
    j=0
    while j<n:
        print(n,end="")
        j+=1
    print()
    i+=1

# Code : Triangular Star Pattern

n = int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        print("*",end="")
        j+=1
    print()
    i+=1


# Code : Triangle Number Pattern
n = int(input())

i=1
while i<=n:
    j=1
    p=i
    while j<=i:
        print(p,end="")
        j+=1
    print()
    i+=1


# Code : Reverse Number Pattern
n = int(input())
i=1
while i<=n:
    j=1
    p=i
    while j<=i:
        print(p,end="")
        p-=1
        j+=1
    print()
    i+=1



# Code : Character Pattern
n = int(input())

i=1
while i<=n:
    j=1
    start_char = chr(ord('A') + i-1)
    while j<=i:
        charP = chr(ord(start_char) + j -1)
        print(charP,end="")
        j+=1
    print()
    i+=1

# Code : Interesting Alphabets
n = int(input())

i=1
temp=n
while i<=n:
    j=1
    start_char = chr(ord('A') + temp-1)
    temp-=1
    while j<=i:
        charP = chr(ord(start_char) + j -1)
        print(charP,end="")
        j+=1
    print()
    i+=1