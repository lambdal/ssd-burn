import argparse
import re

def parse(file_name, key_word):
	r = []
	with open(file_name) as search:
	    for line in search:
	        if re.search(key_word, line):
	        	l = line.split()
	        	r.append(float(l[2][1:-6]))
	return r

def main():
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('ssd_name', type=str,
	                    help='name of the ssd')

	args = parser.parse_args()
	
	ssd_name = args.ssd_name

	# seq write
	r = parse('data/' + args.ssd_name + '_seq_w.txt', "WRITE:")
	print("seq write: ")
	print(r)

	# seq read
	r = parse('data/' + args.ssd_name + '_seq_r.txt', "READ:")
	print("seq read: ")
	print(r)

	# random write
	r = parse('data/' + args.ssd_name + '_rand_w.txt', "WRITE:")
	print("random write: ")
	print(r)

	# random read
	r = parse('data/' + args.ssd_name + '_rand_r.txt', "READ:")
	print("random read: ")
	print(r)

if __name__ == '__main__':
	main()
