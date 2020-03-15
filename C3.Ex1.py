text=input("textul este= ")
i=0
x=len(text)
while i<x:
    if text[i]==','or text[i]==' ':
        i=i+1
    else:
        print(text[i])
        i=i+1
    
    
