flag = 'some string'
key = 'k'
output = ''
for character in flag:
	output += str(hex(ord(character) ^ ord(key)))[2:] + ' '
	key = character
print(output)

flag = '&...ñÁq!.Ã...0.3.:.1¹A³.a¢ÃÁ...0>..:<.¹A.'
key = 'k'
output = ''
for character in flag:
	output += str(hex(ord(character) ^ ord(key))) + ' '
	key = character
print(output)