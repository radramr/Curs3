x=input("x=")
inv=0
x=int(x)

while x!=0:
    inv=inv*10+x%10
    x=x//10

print(inv)
