# Ian Castillo Rosales
# 07/10/2016

# This little script can show you, how much you are compatible with Dr. Chuck (in a music sense) or other people!

# INPUT
# library_1 = An iTunes library (XML file) with your data music stored in it.
# library_2 = Your best friend iTunes library (XML file) with his/her data music stored in it.

# OUTPUT
# rate = Percentage of compatibility. The simplest way to have a rate of compatibility is compare your
# favorites music genres with your friend.

# EXAMPLE
# If your friend listen: Rock, Salsa, Punk, Pop, Soul
# And you listen: Rock, Punk, Groovy
# The rockompatibility would be the number of genres that both listen: Rock and Punk, i.e., 2
# Divided by the number of genres that your friend listen, 5
# rockombatibility : 2/5

import xml.etree.ElementTree as et

def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key : found = True
    return None

def top_genres (lib):
    stuff = et.parse(lib)
    all = stuff.findall('dict/dict/dict')

    genres_list = dict()
    for entry in all:

        if (lookup(entry, 'Track ID') is None ): continue
        genre = lookup(entry, 'Genre')
        if genre is None: continue

        if genre in genres_list:
            genres_list[genre] += 1
        else:
            genres_list[genre] = 1

    # genres_sorted = sorted(((v, k) for k, v in genres_list.items()), reverse = True)
    return genres_list

lib_1 = raw_input('Enter file with the library to compare: ')
lib_2 = raw_input('Enter file with your music library: ')

gl_1 = top_genres(lib_1)
gl_2 = top_genres(lib_2)

num = 0.0
genre_match = []
for genre in gl_2.keys():
    if genre in gl_1.keys():
        num += 1
        genre_match.append(genre)

print 'Your rockompatibility with your friend is:', num/len(gl_1)
print
print 'These are the genres that both listen: '
for genre in genre_match: print genre