#problem → https://rosalind.info/problems/rna/
#solution

def transcribe(dna):
    rna = str(dna).replace("T","U")

    return rna


dna = open("rosalind_rna.txt")
res = str(transcribe(dna.read()))
output = open("output_rna.txt","w+")
output.write(res)
output.close()
    