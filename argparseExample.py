# Covers positional argument, optional argument, action, choices, default, verbosity, echo, type, help, description, mutually exclusive group

import argparse

parser = argparse.ArgumentParser(description='basics of command line application')
parser.add_argument('echo', help='echo string you use here')
#arg = parser.parse_args()

group = parser.add_mutually_exclusive_group()
group.add_argument('-v', '--verbosity', help='verbosity here', action='store_true')
group.add_argument('-q', '--quiet', help='simple display', action='store_true')
parser.add_argument('--square', help='square the number', type=int, choices=[0,1,2], default=2)
args = parser.parse_args()
if not args.square:
	print 'please use args.square'
if args.echo:
	print args.echo
if args.verbosity:
	print 'The square of ' + str(args.square) + ' is ' + str(args.square**2)
elif args.quiet:
	print args.square**2
