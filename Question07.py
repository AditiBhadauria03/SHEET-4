n=int(input("Enter number of rows:"))
for i in range(1, n + 1):
    if i == 1 or i == n:
        print("* " * 5)  
    else:
        print("* *")  