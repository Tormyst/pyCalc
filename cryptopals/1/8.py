strings = open('8.txt', 'r')

best_guess = 81

for cipher_text in strings:
    hash_map = {}
    for block in [cipher_text[i:i+4] for i in range(0, len(cipher_text), 4)]:
        if not (block in hash_map):
            hash_map[block] = 0
        hash_map[block] += 1
    if len(hash_map) < best_guess:
        best_guess = len(hash_map)
        best_sol = cipher_text
        best_map = hash_map

print best_guess
print best_sol
print best_map
