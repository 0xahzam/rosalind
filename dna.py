#problem → https://rosalind.info/problems/dna/
#solution

def nucleotide(dna):
    A = dna.count("A")
    C= dna.count("C")
    G = dna.count("G")
    T = dna.count("T")

    return("{} {} {} {}".format(A,C,G,T))


dna = open("rosalind_dna.txt")
res = str(nucleotide(dna.read()))
output = open("output_dna.txt","w+")
output.write(res)
output.close()






    