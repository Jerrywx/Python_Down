import socket

def handle_request(client):

    buf = client.recv(1024)
    print(buf)

    client.send("HTTP/1.1 200 OK\r\n\r\n".encode("utf8"))
    # client.send("<h1 style='color:red'>Hello World!</h1>".encode("utf8"))
    client.send("<h1 style='color:red'>Hello World!</h1>".encode("utf8"))

def main():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8001))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()

if __name__ == '__main__':

    main()