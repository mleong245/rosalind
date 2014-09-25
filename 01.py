def nucleotideCounter(DNAstring):
	# rosalind_DNA
	aCount = 0
	cCount = 0
	gCount = 0
	tCount = 0
	for i in range(len(DNAstring)):
		if DNAstring[i] == 'A':
			aCount += 1
		elif DNAstring[i] == 'C':
			cCount += 1
		elif DNAstring[i] == 'G':
			gCount += 1
		elif DNAstring[i] == 'T':
			tCount += 1
		else:
			pass
	# return aCount, cCount, gCount, tCount
	print(aCount, cCount, gCount, tCount)


def rnaTranscriber(RNAstring):
	# rosalind_RNA
	transcribed = RNAstring.replace('T', 'U')
	return transcribed


def reverseComplement(DNAstring):
	# rosalind_REVC
	reversed = DNAstring[::-1]
	for i in range(len(reversed)):
		if reversed[i] == 'A':
			reversed = reversed[:i] + 'T' + reversed[i+1:]
		elif reversed[i] == 'T':
			reversed = reversed[:i] + 'A' + reversed[i+1:]
		elif reversed[i] == 'C':
			reversed = reversed[:i] + 'G' + reversed[i+1:]
		elif reversed[i] == 'G':
			reversed = reversed[:i] + 'C' + reversed[i+1:]
		else:
			pass
	return reversed


def rabbits(n, k):
	# rosalind_FIB
	if n == 0:
		return 0
	if n == 1:
		return 1
	if n == 2:
		return 1
	return rabbits(n - 1, k) + k*rabbits(n - 2, k)


def hamming(DNA1, DNA2):
	# rosalind_HAMM
	count = 0
	for i in range(len(DNA1)):
		if DNA1[i] != DNA2[i]:
			count += 1
	return count