def is_prime(num):
    factor = 2
    while factor <= num//2:
        x = num % factor
        #print(num, factor)
        if x == 0:
            return False
        else:
            factor +=1
            continue
    if factor > num//2:
        return True

        
for i in range(1, 100000):
	if is_prime(i + 1):
			print(i + 1, end=" ")

#print(is_prime(7398))
