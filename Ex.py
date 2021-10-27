x = int(input("Enter the first number"))
y = int(input("Enter the second number"))
z = int(input("Enter the third number"))

if((x>y) and (x>z)):
    print("first number is a greatest number")
elif((y>x) and (y>z)):
    print("secound number is a greatest number") 
elif((z>x) and (z>y)):
    print("third number is a greatest number")
elif((x>y) and (x<z)):
    print("third number is a greatest number")
elif((y>x) and (y<z)):
    print("third number is a greatest number")
elif((x>z) and (x<y)):
    print("secound number is a greatest number")
elif((z>x) and (z<y)):
    print("secound number is a greatest number")
else:
    print("not defined")