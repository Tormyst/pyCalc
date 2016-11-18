from Crypto.Cipher import AES

strings = open('7.txt', 'r')
cypher_text = strings.read().decode('base64')

decryption_suite = AES.new('YELLOW SUBMARINE', AES.MODE_ECB)
print decryption_suite.decrypt(cypher_text)
