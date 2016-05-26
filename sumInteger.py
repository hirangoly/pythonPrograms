# input: given integer, target number
# output: return 2 number those are sum of target

num = [9,7,2,6,5,2,0] 
target = 4

i = 0

# using double loop O[Nsquare]
for x in num:
	num1 = num[i+1:]
	if target-x in num1:
		y = num1.index(target-x)
		print 'double loop solution'
		print num[i], num1[y]
	i+=1


num = [9,7,2,6,5,2,0] 
target = 9
num1_dict={}

i = 0
# using single loop O[N]
for x in num:
	if target-x in num1_dict:
		print 'single loop solution'
		print x, target-x
	num1_dict[x] = i
	i+=1


num = [0,2,2,5,6,7,9]
target = 9
num1_dict={}

i = 0
j = len(num) - 1
# using single loop O[N log N]
while (i<j):
	sum_num = num[i] + num[j]
	if sum_num > target:
		j-=1
	elif sum_num < target:
		i+=1
	else:
		print 'binary solution'
		print num[i], num[j]
		i+=1
		j-=1

