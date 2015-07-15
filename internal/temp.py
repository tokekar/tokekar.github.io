import argparse

def printout(args):
	print args.header
	print args.outdir

def main():
	parser = argparse.ArgumentParser('Pub Generator')
	parser.add_argument('header', help='path to the header.part.html file', type=str)
	parser.add_argument('outdir', help='path to the output directory', type=str)
	args = parser.parse_args()
	printout(args)


if __name__ == "__main__":
    main()
