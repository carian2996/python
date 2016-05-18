fname = raw_input("Enter file name: ")
fh = open(fname)

lista = []

for line in fh:
    line = line.rstrip()
    line = line.split()
    for word in line:
        if word in lista:
            continue
        lista.append(word)
lista.sort()
print lista