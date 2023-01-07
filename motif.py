# problem → https://rosalind.info/problems/subs/
# solution

def motif(data):
    s = str(data[0].split('\n')[0])
    t = str(data[1].split(' ')[0])
    l = sum(len(x) for x in t.split())
    les = ""
    testdata = []
    for i in range(0, len(s)-1):
        test = s[i:i+l]
        if len(test) == l:
            testdata += [test]

    for i in range(0,len(testdata)-1):
        if testdata[i].strip()==t.strip():
            les  += str(i+1) + " "

    return les  


file = open("rosalind_subs.txt")
data = file.readlines()


output = open("output_subs.txt", "w+")
output.write(motif(data))
output.close()
