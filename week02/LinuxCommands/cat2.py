import sys

def cat2():
	'''
	with open(sys.argv[1],"r") as f:
		print(f.read())

	with open(sys.argv[2],"r") as f:
		print(f.read())
	'''
for i in range(1, len(sys.argv)):
	with open(sys.argv[i],"r") as f:
		print(f.read())


def main():
	cat2()

if __name__=='__main__':
	main()