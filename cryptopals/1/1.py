import base64

def toBase64(hex_string):
    x = hex_string.decode('hex')
    return base64.b64encode(x)

print toBase64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')
