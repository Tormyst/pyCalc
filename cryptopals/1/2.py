def read_hex(hex_string):
    return hex_string.decode('hex')

def fixed_xor(buffer1, buffer2):
    resutls = ''
    for pair in zip(buffer1, buffer2):
        resutls += chr(ord(pair[0]) ^ ord(pair[1]))
    return resutls

x = read_hex('1c0111001f010100061a024b53535009181c')
y = read_hex('686974207468652062756c6c277320657965')
print fixed_xor(x,y).encode('hex')
