import socket

sock = socket.socket()
sock.bind(('', 6969))

sock.listen(100500)

while True:
    conn, address = sock.accept()
    while True:
        data = ""
        while True:
            s = conn.recv(1)
            if s == "\n":
                break
            else:
                data += s
        print(data)
