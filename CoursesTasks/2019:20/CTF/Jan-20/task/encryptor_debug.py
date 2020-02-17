from hashlib import md5
import string
import random
import time
import os
import tarfile
import datetime



BLOCK_SIZE = 256 # bytes
KEYS = dict()
CHOSEN_KEYS = [] # for key_log
KEYS_LEN = 64

alpha = string.ascii_letters + string.digits


def hex_int(num):
	return hex(num)[2:] if num >= 16 else '0'+hex(num)[2:] 

def random_string( length ):
	global alpha
	return ''.join( [ random.choice( alpha ) for _ in range(length) ] )


def random_hamma( length ):
	return [random.randint(0,255) for _ in range(length)]


def generate_keys():
	for i in range( KEYS_LEN ):
		hex_value = hex_int(i)
		# hex_value = hex(i)[2:] if i >= 16 else '0'+hex(i)[2:] 
		KEYS[ hex_value ] = random_hamma( BLOCK_SIZE )




def get_xored( block, key ):
	# key_bytes = key.encode()
	enc = bytes( map( lambda x: x[0]^x[1], zip( block, key ) ) )
	return enc




def encrypt( source_filename, enc_filename ):
	global CHOSEN_KEYS, KEYS
	
	file_size = os.stat( source_filename ).st_size
	
	padding = BLOCK_SIZE - ( file_size % BLOCK_SIZE )
	block_count = ( file_size + padding ) // BLOCK_SIZE
	
	with open( source_filename, 'rb' ) as inp, open( enc_filename, 'wb' ) as out:
		for _ in range( block_count ):
			
			block = inp.read( BLOCK_SIZE )
			if le3n( block ) != BLOCK_SIZE: 
				block += b'@' * padding
			
			index = hex_int(int(md5( block ).hexdigest()[:2],16) % KEYS_LEN)
			enc_block = get_xored( block, KEYS[ index ] )
			CHOSEN_KEYS.append( index )
			
			out.write( enc_block )



def pack_in_archive( enc_filename, timestamp ):
	
	# the easiest way to change date, trust me :D
	now = datetime.datetime.fromtimestamp( timestamp )
	formatted = datetime.datetime( now.year, now.month, now.day, 13, 37, 0, 0 )
	formatted_timestamp = int( formatted.timestamp() )
	
	with tarfile.open( 'task.tar.gz', "w:gz" ) as archiver:
		info = tarfile.TarInfo()
		info.name = enc_filename
		info.size = os.stat( enc_filename ).st_size
		info.mtime = formatted_timestamp
		archiver.addfile( info, open( enc_filename, 'rb' ) )




def make_key_file( filename ):
	with open(filename, 'w') as f:
		
		f.write('BLOCKSIZE:{}\n'.format(BLOCK_SIZE))
		f.write('[keys]\n')
		
		for key in KEYS:
			f.write( ' '.join(map(str,KEYS[key])) )
			f.write('\n')
		
		f.write('[choosen]\n')
		
		for i in range( len(CHOSEN_KEYS) ):
			f.write( str(i) + ' block: ' + CHOSEN_KEYS[i] + '\n' )



if __name__ == '__main__':
	timestamp = int( time.time() )
	random.seed( timestamp )
	generate_keys()
	
	source_filename = input('File to encrypt: ').strip()
	file_ext = source_filename.split('.')[1]
	enc_filename = random_string( 15 ) + '.{}.enc'.format(file_ext)
	encrypt( source_filename, enc_filename )
	pack_in_archive( enc_filename, timestamp )
	
	os.remove( enc_filename )
	make_key_file('enc_key.log')
