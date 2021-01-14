import base64

def get_file(path):
    return open(path,"rb").read()


def base32_encode(data):
    return base64.b32encode(data).decode("utf-8")

def base32_decode(data):
    return base64.b32decode(data)
