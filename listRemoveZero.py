#Given an array of integers, write an algorithm that brings all the 0 elements to the end of the array and returns the # of non-zero elements. 

int_list = [1,4,0,5,9,11,10,0,33,0,50,0]
zero_cnt = 0

total_cnt = len(int_list)

while 0 in int_list:
	zero_cnt += 1
	int_list.remove(0)


nonzero_cnt = total_cnt - zero_cnt
print 'non-zero cnt'
print nonzero_cnt

#append 0 for #zero_cnt times
for i in range(zero_cnt):
	int_list.append(0)

print 'final list'
print int_list
				

