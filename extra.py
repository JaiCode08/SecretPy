import zlib

a = "this string needs compressing"
a = zlib.compress(a.encode())
print(a)