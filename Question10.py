N=int(input("Enter number of rows:"))
for i in range(N, 0, -1):   
    for j in range(1, 2*i):    
        print("*", end=" ")
    print()