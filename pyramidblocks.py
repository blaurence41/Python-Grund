blocks = int(input("Enter the number of blocks: "))
height = 0
while blocks > 0:
    blocks -= height+1
    height += 1
    if blocks < 0:
        print("The height of the pyramid:", height-1)
        break
else:
    print("The height of the pyramid:", height)