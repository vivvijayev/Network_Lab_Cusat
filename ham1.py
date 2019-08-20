def genHammingCode(databits):
	# GENERATE HAMMING CODE
	d=databits
	data=list(d)
	data.reverse()
	c,ch,j,r,h=0,0,0,0,[]

	while ((len(d)+r+1)>(pow(2,r))):
		r=r+1

	for i in range(0,(r+len(data))):
		p=(2**c)

		if(p==(i+1)):
		    h.append(0)
		    c=c+1

		else:
		    h.append(int(data[j]))
		    j=j+1

	for parity in range(0,(len(h))):
		ph=(2**ch)
		if(ph==(parity+1)):
		    startIndex=ph-1
		    i=startIndex
		    toXor=[]

		    while(i<len(h)):
		        block=h[i:i+ph]
		        toXor.extend(block)
		        i+=2*ph

		    for z in range(1,len(toXor)):
		        h[startIndex]=h[startIndex]^toXor[z]
		    ch+=1

	h.reverse()
	#print('Hamming code generated would be:- ', end="")
	#print(int(''.join(map(str, h))))
	
	return int(''.join(map(str, h)));
	
def checkHammingCode(hammingCode):
	# DETECT ERROR IN RECEIVED HAMMING CODE
	data=list(hammingCode)
	data.reverse()
	c,ch,j,r,error,h,parity_list,h_copy=0,0,0,0,0,[],[],[]

	for k in range(0,len(data)):
		p=(2**c)
		h.append(int(data[k]))
		h_copy.append(data[k])
		if(p==(k+1)):
			c=c+1
		    
	for parity in range(0,(len(h))):
		ph=(2**ch)
		if(ph==(parity+1)):
			startIndex=ph-1
			i=startIndex
			toXor=[]

			while(i<len(h)):
				block=h[i:i+ph]
				toXor.extend(block)
				i+=2*ph

			for z in range(1,len(toXor)):
				h[startIndex]=h[startIndex]^toXor[z]
			parity_list.append(h[parity])
			ch+=1
	parity_list.reverse()
	error=sum(int(parity_list) * (2 ** i) for i, parity_list in enumerate(parity_list[::-1]))

	if((error)==0):
		return 'There is no error in the hamming code received'

	elif((error)>=len(h_copy)):
		return 'Error cannot be detected'

	else:
		if(h_copy[error-1]=='0'):
	  		h_copy[error-1]='1'
			return 'Error is in'+str(error)+'bit'
		elif(h_copy[error-1]=='1'):
			h_copy[error-1]='0'
			h_copy.reverse()
			return 'Error is in '+str(error)+' bit'+' After correction hamming code is:- ' + str(int(''.join(map(str, h_copy))))
		else:
			return 'Option entered does not exist'
