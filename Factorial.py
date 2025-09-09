


def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i

    return f
        




n=int(input("Enter the number whose factorial is to be find?:"))
fact(n)
print(fact(n))
