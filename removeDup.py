# remove duplicate itmes from list but keep 1

dup_lst = [1,4,5,3,1,2,7,6,5]

print dup_lst

# this remove duplicate and sort as well
non_dup_lst = set(dup_lst)

print non_dup_lst

empty_lst = []

for item in dup_lst:
	if item not in empty_lst:
		empty_lst.append(item)

print empty_lst

print sorted(empty_lst)
