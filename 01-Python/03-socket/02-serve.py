
import socket

#

sk = socket.socket()

addredd = ('127.0.0.1', 8000)

sk.bind(addredd)

sk.listen(3)

print("waiting....")

conn = sk.accept()
print(conn)

