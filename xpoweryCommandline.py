# command line application - x to the power of y, include verbose
import argparse

parser = argparse.ArgumentParser(description='command line application for X to the power of y')
parser.add_argument('x', help='int value x', type=int)
parser.add_argument('y', help='int value y', type=int)
parser.add_argument('-v', '--verbose', help='output verbosity', action='store_true')
args = parser.parse_args()
output = args.x ** args.y
if args.verbose:
	print str(args.x) + ' to the power of ' + str(args.y) + ' is ' + str(output)
	print '{}**{} == {}'.format(args.x,args.y,output)	
else:
	print output
