import codecs
import zlib
import base64

msg = "eJwrdYoqr8o2dA0OMKgCABxjBDE="
# def decode(msg):
#     decode = zlib.decompress(msg)
#     print(decode)
# decode(msg)

def decode64(msg):
    msg = msg.decode('ascii')
    print(msg)
    return(msg)

def uncompress_string(msg):
    unc_str = zlib.decompress(base64.b64decode(msg))
    print(unc_str)
    print(type(unc_str))
    return unc_str

uncompress_string(msg)
decode64(uncompress_string(msg))