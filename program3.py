#wap to find uncommon words from two string
a=input("Enter a string: ")
b=input("Enter another string: ")
e=a.split()
for i in e:
    if i not in b:
        print(i)
c=b.split()
for i in c:
    if i not in a:
        print(i)