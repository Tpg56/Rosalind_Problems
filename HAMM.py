def reed():
	g = input("Enter the file name")
	fiel = open(g, 'r')
	s = fiel.readline()
	t = fiel.readline() 
	return (s,t)
def HAMM(s, t):
	x = len(s)
	dist = 0
	for i in range(0, x):
		if s[i] != t[i]:
			dist = dist + 1 
	return dist 
s = "GGATACCTTACTCTCGTTAAACGCCCCCACGGGACGCTGACGCCCGTGACGCCATGTTCTACTACCTCACGCCGCAAGCCCAAGGGGAAGTGACGCGCAACGAGAAGTAACCCTTCACACGGGAGTAAATACTCTCTCTAGGTGTCCCGGCGGACAATATTTCGAGGACAATGCTTCATAGGGAAGTGCACCATGCAACGCCCCTTAAGGGCGTGCAAACCAAAGGCTGCTTGCTGACATACTACAGCCCTGTTAGTATAGGAGACTACGCTGTATAAACTCACGATTAAGAGTAACCACTCGTTGGGGCAGCGGCCTGAACCCGTAAATTCTGCACCCATTCCGGAGGAGTAGTAAGACGGCTATAGAAAGGTTAAAATTATGCATACCATTCTGGAGTACTCCTCTTTGGTAGGACTATAGTTCGATATGCGATCCCCCTGAGTGCGGTGGTGGTAGTCTGCATTAGTATCTCCGACCTAGCGCACATTGGCTGGGCACCCGCCAAGGCCGTCCAGACATGTAGACTCCGATCGGCATTGAGAAGGCGTAGTAACCACATCCTTTTGAAAAACGTCCGGGCAGTTGTTAATTTTCACGAATTCCCGATTGCTAGCCGTACACTAACCTGGACCCGTGGTTCTACCGAAACAGCATCCCGTTGCTCACCTCCTAAGTAACTCGAACTTAATATCGGTGGGGTCGGCGTTTTATGCAATATGATCCGAGTTGTGGAGAAGGGCTCTGCCCTCCGTCGGTCCAACCCTGGGAATTTTCGGAATAAAATCTTGCGACTCCATTAGGAATTAGCAACTGTCCACCTTTTCCTAACCAGATAATCGTGCACTGACCGATTACGGGGACACGTCACTTACTTGAAAGTCGGGAGTTCTGTGGCCGCCAGGGCCCAATAAGCCT "
t = "GGATGTCTTCCACACATGAAATCGTTCCGGGCGGAATGGAAGCCATTGCCGACGCGTTGAACATCACAACCCCGCACGCATAGGGGCGAACGGCTGACCACTGGTCCGTCCTGATGACTCGTGAAAAGCTACTTTCTCTAGGACTCCCGGAGGCACTTATGTCGGAGGCAGCTGTTCTATCTTAGGAACGACGAAAAACGAGCATTAAAGGGCTGGGTGCCTGTAGGGTCGCTTGTACATCCCACAGCCCCGTTTTCATATAATACTGGAGTTTGAAAAATTACGCTTAAGGCCAAGCATTCGTAGGGCAATAGACGAGGAATGACAGACCCAAGCCGAAGTCGAGATGATTTGTAGGCGGGATTGTGGACTCGCGACAAAGACCATACATTAGTGGAGAATCACTGGTTCTCATGAAAGGGCGTTGATTGGCGATTTGCGAAGGTCACAATGGACACTTCAGCGGATATATCACCGCCATAAGGGTACAAAGATGGGCAATCACGAGCGAAATTAATTCATGGAAACTCCGCTAGGCAATGCCTACGTATAGAACATATTTCGTCTTACCTAGGGGCCTCTCCCTCCACAAGTATGGGGAATTCCCTACTTACTGGCGTTCACTAGTCTGGCCGCCACCCTCTACGGGACCATCTGCAAGTTGGTCACCGATAATGTTTCTGATAACTAATATAGGGCGGGTCCACCTTTTTTAAATTATGATAACCATAGTTGGGAATCCGTCTGCCCGCCGTCCATCTGACCTTTGAAATGCTGCGAGCACCATGATGTGTCTCGCGAACGAATGATCACCATTCAAAGTCTAACTCAGCAGTTGATGGCGCATTTGCTGAATGGGACTTCCGTTCCTCTCTGGGACCTAAGCGTAAGCGGGCTCAGCTCTAATCCGATAAGCAG " 
print (HAMM(s, t))	
