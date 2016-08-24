import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v","--verbose",help="increase output verbosity",type=int)
parser.add_argument("-s","--square",help="square of the input", type=int)
args = parser.parse_args()
ans = args.square**2
if args.verbose==1:
	print "verbosity turned on, square of {} is {}.".format(args.square,ans)
elif args.verbose==2:
	print "{}^2 = {}".format(args.square,ans)
else:
	print ans
#testing: python test.py -v -s number