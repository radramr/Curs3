a=input("a=")
b=input("b=")

a=int(a)
b=int(b)


myList={}

while a<b:
    myList[a]=a
    a=a+1



for item in myList:
    print("Lista ", item)


