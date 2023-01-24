# problem → https://rosalind.info/problems/grph/
# solution

data = open("rosalind_grph.txt")
content = data.read().split('>')
nodes = []
node_num = []

for i in range(0, len(content)):
    node = ""
    parent = content[i].split('\n')

    node_num += [parent[0]]

    for k in parent:

        if k != parent[0]:
            node += k

    nodes += [node]


def overlapgrph(nodes, parent):
    output = open("grph_output.txt", "w+")

    for i in range(0, len(nodes)):
        prefix = nodes[i].split('\n')[0][-3::]

        for j in range(0, len(nodes)):
            if i != j:
                suffix = nodes[j].split('\n')[0][0:3]
                if prefix == suffix:

                    output.writelines("{} {} \n".format(parent[i], parent[j]))

    output.close()


overlapgrph(nodes, node_num)
