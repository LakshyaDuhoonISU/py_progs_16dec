#wap for removing i-th character from a string
a=input("Enter a string: ")
b=int(input("Which index to remove: "))
c=a[:b]+a[b+1:]
print(c)
