for i in range(1,101,1):
	
	num = i // 10
	if i%7 == 0 or i - num *10 == 7 or num == 7:
		continue
	print(i) 
