# From http://www.data-compression.com/english.html
freqs = {
    'a': 0.0651738,
    'b': 0.0124248,
    'c': 0.0217339,
    'd': 0.0349835,
    'e': 0.1041442,
    'f': 0.0197881,
    'g': 0.0158610,
    'h': 0.0492888,
    'i': 0.0558094,
    'j': 0.0009033,
    'k': 0.0050529,
    'l': 0.0331490,
    'm': 0.0202124,
    'n': 0.0564513,
    'o': 0.0596302,
    'p': 0.0137645,
    'q': 0.0008606,
    'r': 0.0497563,
    's': 0.0515760,
    't': 0.0729357,
    'u': 0.0225134,
    'v': 0.0082903,
    'w': 0.0171272,
    'x': 0.0013692,
    'y': 0.0145984,
    'z': 0.0007836,
    ' ': 0.1918182
}

def score(s):
    score = 0
    for i in s:
        c = i.lower()
        if c in freqs:
            score += freqs[c]
    return score

def repeate_string(str, str_len):
    return (str * ((str_len/len(str))+1))[:str_len]

def repeated_xor(buffer1, buffer2):
    if(len(buffer1) < len(buffer2)):
        return repeated_xor(buffer2, buffer1)
    return fixed_xor(buffer1, repeate_string(buffer2, len(buffer1)))

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

def hamming(x, y):
    """Calculates the bitwise difference between two strings"""
    return sum([ bin(ord(pair[0]) ^ ord(pair[1])).count('1') for pair in zip(x, y)])

def key_ham(x, key_size, group_count):
    kg = key_size * group_count
    return hamming(x[:kg],x[kg:kg*2])/float(key_size)

# Test of hamming function.
# print hamming('this is a test', 'wokka wokka!!!')

strings = open('6.txt', 'r')
cypher_text = strings.read().decode('base64')

# Find key size
min_key = 2
max_key = 45

best_s = 0

scores = [(key_size,key_ham(cypher_text, key_size, 20)) for key_size in range(min_key, max_key + 1)]
scores.sort(key=lambda x: x[1])

for key_pair in scores[:4]:
    key_size = key_pair[0]
    sets = [cypher_text[l::key_size] for l in range(key_size)]
    key = ''
    for x in sets:
        bestScore = 0
        for i in range(0,256):
            sol = single_xor(x, chr(i))
            s = score(sol)
            if(s > bestScore):
                bestScore = s
                bestKey = chr(i)
        key += bestKey
    clear_text = repeated_xor(cypher_text, key)
    s = score(clear_text)
    if(s > best_s):
        best_clear = clear_text
        best_s = s
        best_k = key

print "%d letter key: %s, with a score of %f" % (len(best_k), best_k, best_s)
print best_clear
