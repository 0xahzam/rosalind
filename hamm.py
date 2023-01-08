#problem → https://rosalind.info/problems/hamm/
#solution

def hammingDistance(s,t):
    count = 0 
    for i in range(0,len(s)):
        if s[i]!=t[i]:
            count+=1
    
    return count

file = open("rosalind_hamm.txt")
data = file.readlines()
s = data[0].split('\n')[0]
t = data[1]

output = open("output_hamm.txt", "w+")
output.write(str(hammingDistance(s,t)))
output.close()