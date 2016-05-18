# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)

total = 0
freq = 0

for line in fh:
	line = line.rstrip()
	if not line.startswith("X-DSPAM-Confidence:"): continue
	line = line.split()
	num = float(line[1])
	total = total + num
	freq = freq + 1
avg = total / freq
print "Average spam confidence:", avg