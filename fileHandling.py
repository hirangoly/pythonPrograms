from os.path import exists

# ask user for file name
filename = raw_input('Which filename you want to open?')
print 'file name you asked for %r.' % filename
# open file
txt = open(filename)
print('file opened')

# read file
print('here is the content of file')
print txt.read()
# close file
txt.close()

raw_input()

# open file again
txt_again = open(filename, 'w')
print('file opened again')

# clear the file content
txt_again.truncate()

# ask user to type 3 lines
line1 = raw_input('write line1?')
line2 = raw_input('write line2?')
line3 = raw_input('write line3?')

# write those 3 lines to file
txt_again.write(line1+'\n')
txt_again.write(line2+'\n')
txt_again.write(line3+'\n')

# close file
txt_again.close()

# ask user to copy file from and To
infile = raw_input('file from?')
outfile = raw_input('file To?')
print "Copy file from %r to %r" % (infile, outfile)

txt_in = open(infile)

# write infile content to outfile
txt_out = open(outfile, 'w')
txt_out.write(txt_in.read())

# close file
txt_in.close()
txt_out.close()

# open output file if exists
if exists(outfile):
    txt_write = open(outfile)

txt_write.readline()
    
for line in txt_write:
    print line
