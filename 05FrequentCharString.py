#wap to find the least frequent character in the string
a=input("Enter a string: ")
lcount=2
min=""
for i in a:
    count=0
    for j in a:
        if i==j:
            count+=1
    if count<=lcount:
        lcount=count
        min=i
print(min)
