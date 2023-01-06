# problem → https://rosalind.info/problems/gc/
# solution

def gc_content(data):
    G = data.count("G")
    C = data.count("C")
    percentage = ((G+C)/int(len(data))) * 100

    return percentage


data = open("rosalind_gc.txt")
content = data.read()
content = content.split(">")
enhanced = content[1::]

ases = (enhanced[0].split('\n'))



final_parent = []
final_gc = []

for i in enhanced:
    enh2 = i.split("\n")
    length_dna = len(enh2)
    dna = ""
    for i in range(1,length_dna):
        dna += enh2[i]
    parent = enh2[0]
    gc = gc_content(dna)
    final_parent += [parent]
    final_gc += [gc]

res = max(final_gc)
where = ''

for i in range(len(final_gc)):
    if final_gc[i] == res:
        where=i

where = int(where)

data_max = final_parent[where]
gc_max = final_gc[where]

main = """{}
{}""".format(data_max,gc_max)


output = open("output_gc.txt","w+")
output.write(main)
output.close()

