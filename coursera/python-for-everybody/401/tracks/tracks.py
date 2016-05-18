# coding=utf-8
# Ian Castillo Rosales
# This application will read an iTunes export file in XML and produce a properly normalized database with this structure
# 07/01/2015

# Paqueterias para manejar archivos XML y para conectarse a una base en SQLite
import xml.etree.ElementTree as et
import sqlite3

conn = sqlite3.connect('trackIandb.sqlite')
cur = conn.cursor() # Se genera un cursor para poder enviar consultas a la base

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Track;

-- Se crean las tablas necesarias para contener los datos

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')


file_name = raw_input('Enter file name: ')
if ( len(file_name) < 1 ) : print 'You must enter a valid file name'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>

# Parsea el texto de un key deseado. Busca primero el key que se desea.
# Se regresa el valor que contiene como texto
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key : found = True
    return None

stuff = et.parse(file_name)
all = stuff.findall('dict/dict/dict') # Busca todos los elementos que sean diccionarios a un tercer nivel
print 'This file contains:', len(all), "dictionaries"

for entry in all:
    # Solo se busca en aquellos elementos que sean tracks
    if (lookup(entry, 'Track ID') is None ) : continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    genre = lookup(entry, 'Genre')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    # Evitamos los valores vaciones en nuestra base
    if name is None or artist is None or album is None or genre is None:
        continue

    # Inserta los datos en la base

    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )


    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES ( ? )''', ( genre, ) )
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, len, rating, count, genre_id)
        VALUES ( ?, ?, ?, ?, ?, ? )''',
        ( name, album_id, length, rating, count, genre_id ) )

conn.commit()

