# array
# number x = sum of 2 nums in array

A = [1,5,2,7,4,9,0]
x = 7

for num in A:
	if num <= x and (x - num) in A:
		print num, x-num 
		