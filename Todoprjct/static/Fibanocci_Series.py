
# num = 13
# n1, n2 = 0, 1
# print("Fibonacci Series:", n1, n2, end=" ")
# for i in range(2, num):
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3
#     print(n3, end=" ")
# print()
# #

def Fib(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return (Fib(n-1)+Fib(n-2))

n=int(input("Enter the Range of Number: "))
for n in range(0,n):
    print(Fib(n))


