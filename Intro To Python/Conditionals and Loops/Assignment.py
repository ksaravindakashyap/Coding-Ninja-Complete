#  Calculator

while(1):
    n = int(input())
    if(n == 1):
        a = int(input())
        b = int(input())
        print(a+b)
    elif n == 2:
        a = int(input())
        b = int(input())
        print(a-b)
    elif n == 3:
        a = int(input())
        b = int(input())
        print(a*b)
    elif n == 4:
        a = int(input())
        b = int(input())
        print(a//b)
    elif n == 5:
        a = int(input())
        b = int(input())
        print(a%b)
    elif n == 6:
        exit()
    else:
        print("Invalid Operation")

# Reverse of a number

N = int(input())
temp = str(N)
answer = temp[::-1]
answer =  int(answer)
print(answer)


# Palindrome number

def checkPalindrome(num):
        temp1 = str(num)
        temp2 = temp1[::-1]
        if(temp1 == temp2):
            return True
        else:
            return False
    
	
		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')


# Sum of even & odd

n=int(input())
sumEven=0
sumOdd=0
while(n!=0):
    temp = n%10
    if(temp%2 == 0):
        sumEven+=temp
    else:
        sumOdd+=temp
    n=n//10
print(sumEven," ",sumOdd)


# Nth Fibonacci Number

n = int(input())

def fibonacci(n):
    f = [0,1]
    for i in range(2,n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]

print(fibonacci(n))