def read_hex(hex_string):
    return hex_string.decode('hex')

def repeate_string(str, str_len):
    return (str * ((str_len/len(str))+1))[:str_len]

def fixed_xor(buffer1, buffer2):
    resutls = ''
    for pair in zip(buffer1, buffer2):
        resutls += chr(ord(pair[0]) ^ ord(pair[1]))
    return resutls

def repeated_xor(buffer1, buffer2):
    if(len(buffer1) < len(buffer2)):
        return repeated_xor(buffer2, buffer1)
    return fixed_xor(buffer1, repeate_string(buffer2, len(buffer1)))


p_text = bytes('Burning \'em, if you ain\'t quick and nimble\nI go crazy when I hear a cymbal')
key = 'ICE'
print repeated_xor(p_text,key).encode('hex')
