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
	for i in range(KEYS_LEN):
		hex_value = hex_int(i)
		# hex_value = hex(i)[2:] if i >= 16 else '0'+hex(i)[2:] 
		KEYS[ hex_value ] = random_hamma( BLOCK_SIZE )
		print("---", hex_value, i, "::::", *list(map(hex_int, KEYS[hex_value])))

def get_xored( block, key ):
	# key_bytes = key.encode()
	enc = bytes( map( lambda x: x[0]^x[1], zip( block, key ) ) )
	return enc


def encrypt( source_filename, enc_filename ):
	global CHOSEN_KEYS, KEYS
	
	file_size = os.stat( source_filename ).st_size
	padding = BLOCK_SIZE - ( file_size % BLOCK_SIZE ) # 256 possible bruteforce
	block_count = ( file_size + padding ) // BLOCK_SIZE
	
	with open( source_filename, 'rb' ) as inp, open( enc_filename, 'wb' ) as out:
		for _ in range( block_count ):
			
			block = inp.read( BLOCK_SIZE )
			if len( block ) != BLOCK_SIZE: 
				block += b'@' * padding
			
			index = hex_int(int(md5( block ).hexdigest()[:2],16) % KEYS_LEN)
			enc_block = get_xored( block, KEYS[ index ] )
			CHOSEN_KEYS.append( index )
			
			out.write( enc_block )


def decrypt( source_filename, denc_filename ):
	global CHOSEN_KEYS, KEYS
	
	file_size = os.stat(source_filename).st_size
	
	padding = BLOCK_SIZE - ( file_size % BLOCK_SIZE )
	block_count = ( file_size + padding ) // BLOCK_SIZE
	

	with open( source_filename, 'rb' ) as inp, open( denc_filename, 'wb' ) as out:
		for _ in range( block_count ):
			
			block = inp.read( BLOCK_SIZE )
			if len( block ) != BLOCK_SIZE: 
				block += b'@' * padding
			
			index = hex_int(int(md5( block ).hexdigest()[:2],16) % KEYS_LEN)
			enc_block = get_xored( block, KEYS[ index ] )
			CHOSEN_KEYS.append( index )
			
			out.write( enc_block )







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


timestamp = 1504026002
random.seed( timestamp )
print("Generating keys....")
generate_keys()
	
random_string( 15 )

decrypt("R0Gw5iUw0a42BBK.test_file.py.enc", "1.decrypted.py")
decrypt("decrypting_script.py", "1.decrypted.py")
