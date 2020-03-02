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
	for i in range(64):
		hex_value = hex_int(i)
		# hex_value = hex(i)[2:] if i >= 16 else '0'+hex(i)[2:] 
		KEYS[ hex_value ] = random_hamma( BLOCK_SIZE )
		
def get_xored( block, key ):
	# key_bytes = key.encode()
	enc = bytes( map( lambda x: x[0] ^ x[1], zip( block, key ) ) )
	return enc


def encrypt( source_filename, enc_filename ):
	global CHOSEN_KEYS, KEYS
	
	# ! 256 possible combinations
	file_size = os.stat( source_filename ).st_size
	padding = 256 - ( file_size % 256 )

	block_count = ( file_size + padding ) // 256
	print(padding, block_count)
	
	#* padding ( 0 ~ 256 )

	with open( source_filename, 'rb' ) as inp, open( enc_filename, 'wb' ) as out:
		for _ in range( block_count ):
			
			block = inp.read( 256 )
			
			index = hex_int(int(md5( block ).hexdigest()[:2],16) % 64)
			print(md5( block ).hexdigest(), int(md5( block ).hexdigest()[:2],16) % 64, index)
			enc_block = get_xored( block, KEYS[ index ] )

			if len( block ) != 256: 
				block += b'@' * padding #* padding ( 0 ~ 256 )
			
			out.write( enc_block )


def decrypt(input_crypted_file, output_file):
	global CHOSEN_KEYS, KEYS


	# * For first block only, for now
	try:
		for i in range(130):
			for possible_index in KEYS:
				with open( input_crypted_file, 'rb' ) as inp, open( output_file+"_"+str(i)+"_"+possible_index, 'wb' ) as out:
					block = inp.read( 256 )
					
					decrypted_block = get_xored(block, KEYS[possible_index])
					out.write(decrypted_block)
	except:
		print("EXIT")

	'''
	for possible_padding in range(0, 256):		
		for possibe_block_count in range(50):
			try:
				with open( input_crypted_file, 'rb' ) as inp, open( output_file+"__"+str(possible_padding)+"__"+str(possibe_block_count), 'wb' ) as out:
					for i in range(possibe_block_count):
						block = inp.read(256)
						if len(block) != 256:
							block -= b'@' * possible_padding 

						index = hex_int(int(md5( block ).hexdigest()[:2],16) % 64)
						decrypted_block = get_xored(KEYS[ index ], block)

						out.write(decrypted_block)
			except:
				pass
	'''



def make_key_file( filename ):
	with open(filename, 'w') as f:
		
		f.write('BLOCKSIZE:{}\n'.format(256))
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

decrypt("R0Gw5iUw0a42BBK.doc.enc", "out/doc.doc")