c0 = int(input("Enter a whole number > 0: "))
steps = 0
if c0 <= 0:
    c0 = int(input("That is not a whole number above 0. Enter a number > 0: "))
else:    
    while c0 > 1:
        if c0%2 == 0:
            c0 /= 2
            steps += 1
            int(c0)
            print(int(c0)) 
        elif c0%2 == 1:
            c0 = (3 * c0) + 1
            steps += 1
            int(c0)
            print(int(c0)) 
    if c0 == 1:
        print(int(c0), "steps =", steps)  