#reverse sentence input= 'This is Me' output='Me is This'
#use reverse function
in_str = 'This is Me'
split_list = in_str.split(' ')
print split_list
split_list.reverse()
out_str=''

for item in split_list:
	out_str += item + ' '

print out_str
