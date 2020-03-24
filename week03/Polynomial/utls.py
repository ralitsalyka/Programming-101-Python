

def find_coefficients(string):
	cons=[]
	cons_str=""
	i=0
	str_len=len(string)
	if string[0]=='x':
		cons_str='1'
	while i < str_len :
		if string[i]=='*' or string[i]=='x' :
			break
		else:
			cons_str=cons_str + string[i]
		i=i+1
	return cons_str


def power_find(string):
	power_str="1"
	power=[]
	str_len=len(string)
	i=0
	j=0
	while i<str_len-1:
		if string[i]=='x':

			if string[i+1]=='^':
				j=i+2
				power_str=""
				break
		i=i+1
	if j==0:
		j=str_len
	while j<str_len:
		power_str=power_str + string[j]
		j=j+1

	return power_str


def create_part_derive(string):
	str_len=len(string)

	if str_len==1:
		if string[0] in '123456789':
			newStr='0'
		elif string[0]=='x':
			newStr='1'
	else:
		cons_int=int(find_coefficients(string))
		power_int=int(power_find(string))


		cons_int=power_int*cons_int

		if power_int>0:
			power_int=power_int-1

		newStr=str(cons_int)

		if power_int==1:
			newStr=newStr+"x"
		elif power_int>1:
			newStr=newStr+"x^"+str(power_int)
	return newStr


def create_list_of_derive(string):
	all_string=""
	list_derives=[]
	str_len=len(string)
	i=0
	temp_str=""
	while i<str_len:
		if string[i]=='+':
			newStr=create_part_derive(temp_str)
			if newStr=='0':
				all_string=all_string+newStr
				list_derives.append(newStr)
			else:
				all_string=all_string+newStr+"+"
				list_derives.append(newStr)
			temp_str=""
		else:
			temp_str=temp_str+string[i]
		i=i+1
	if temp_str!='0':
		newStr=create_part_derive(temp_str)
		list_derives.append(newStr)
		if newStr!='0':
			all_string=all_string+newStr
		
	return list_derives



def main():
	pass
if __name__=='__main__':
	main()