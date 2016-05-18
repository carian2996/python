# Write a program to read through the mbox-short.txt and figure out who has 
# the sent the greatest number of mail messages. The program looks for 'From ' 
# lines and takes the second word of those lines as the person who sent the 
# mail. The program creates a Python dictionary that maps the sender's mail 
# address to a count of the number of times they appear in the file. After 
# the dictionary is produced, the program reads through the dictionary using 
# a maximum loop to find the most prolific committer.

name = raw_input("Enter file: ")
handle = open(name)

emails = []

for line in handle:
	line = line.rstrip()
	if not line.startswith("From "): continue
	line = line.split()
	emails.append(line[1])

count = dict()

for person in emails:
	count[person] = count.get(person, 0) + 1

maxcount = None
sendest = None

for email, n in count.items():
	if maxcount is None or n > maxcount:
		maxcount = n
		sendest = email

print sendest, maxcount