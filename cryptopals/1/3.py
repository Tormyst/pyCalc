def read_hex(hex_string):
    return hex_string.decode('hex')

def fixed_xor(buffer1, buffer2):
    resutls = ''
    for pair in zip(buffer1, buffer2):
        resutls += chr(ord(pair[0]) ^ ord(pair[1]))
    return resutls

def single_xor(buffer, letter):
    results = ''
    for l in buffer:
        results += chr(ord(l) ^ ord(letter))
    return results

x = read_hex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
for i in range(0,255):
    error = 0
    sol = single_xor(x, chr(i))
    for l in sol:
        if(ord(l) < 31 or ord(l) > 123):
            error = 1
            break
    if error == 0:
        print(sol)
        break
