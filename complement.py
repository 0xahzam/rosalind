# problem → https://rosalind.info/problems/revc/
# solution

def compliment(dna):

    new = ""

    for i in dna:
        if i == "A":
            new += "T"
        if i == "T":
            new += "A"
        if i == "G":
            new += "C"
        if i == "C":
            new += "G"

    return new

dna = open("rosalind_revc.txt")
res = str(compliment(dna.read()[::-1]))
output = open("output_compliment.txt","w+")
output.write(res)
output.close()



