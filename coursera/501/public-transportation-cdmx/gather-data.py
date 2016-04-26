from zipfile import ZipFile
from urllib import urlretrieve
from tempfile import mktemp
from time import sleep

urlZip = raw_input('Enter zip url or enter: ')
if ( len(urlZip) < 1 ) : urlZip = 'http://s3.amazonaws.com/setravi/df_gtfs.zip'

tempDir = 'data/cdmx_gtfs'

try:
	tempFile = mktemp('.zip') # Create a temporary file to allocate the zip file
	print 'The temporal file was created'
except:
	print "The temporal file wasn't created"

try:
	print 'Retrieving files from:', urlZip
	sleep(1)
	name, headers = urlretrieve(urlZip, tempFile) # Return a tuple (filename, headers)
except:
	print 'Unable to retrieve files'

print 'Unzipping file into:', tempDir
dataZip = ZipFile(tempFile) # Read a zip file
dataZip.extractall(tempDir) # Extract all file into tempDir
dataZip.close()

print 'Files were downloaded'