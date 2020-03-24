import sys

def sum_numbers():
	a=[]
	Sum=0
	with open(sys.argv[1],"r") as f:
		for line in f:
			for num in line.split():
				#Sum+=int(num)
				a.append(int(num))
	Sum=sum(a)
	return Sum

def main():
	print(sum_numbers())

if __name__=='__main__':
	main()