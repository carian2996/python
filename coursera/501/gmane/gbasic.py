import sqlite3
import time
import urllib
import zlib

# ========== Top ? messages sent for people and organizations ==========
howmany = int(raw_input("How many to dump? "))

# ========== Connection to the database ==========
conn = sqlite3.connect('index.sqlite')
conn.text_factory = str
cur = conn.cursor()

# ========== Select the data to analyze ==========
cur.execute('''SELECT Messages.id, sender FROM Messages
    JOIN Senders ON Messages.sender_id = Senders.id''')

# ========== Make a count table for senders (people and organizations) ==========
sendcounts = dict()
sendorgs = dict()
for message in cur:
    sender = message[1]
    sendcounts[sender] = sendcounts.get(sender,0) + 1
    pieces = sender.split("@")
    if len(pieces) != 2 : continue
    dns = pieces[1]
    sendorgs[dns] = sendorgs.get(dns,0) + 1

# ========== Top ? for senders ==========
print ''
print 'Top', howmany, 'Email list participants'

x = sorted(sendcounts, key=sendcounts.get, reverse=True)
for k in x[:howmany]:
    print k, sendcounts[k]
    if sendcounts[k] < 10 : break

# ========== Top ? for organizations ==========
print ''
print 'Top',howmany,'Email list organizations'

x = sorted(sendorgs, key=sendorgs.get, reverse=True)
for k in x[:howmany]:
    print k, sendorgs[k]
    if sendorgs[k] < 10 : break
