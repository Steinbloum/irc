import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "irc.libera.chat"
PORT = 6667
NICK = "Baohbot"

s.connect((HOST, PORT))

nick_data = "NICK " + NICK + "\r\n"
s.send(nick_data.encode())

username_data = "USER Baoh Baoh Baoh : Baoh \r\n"
s.send(username_data.encode())

s.send("JOIN #test-chan \r\n".encode())

while True:
    result = s.recv(1024).decode("UTF-8")
    print(result)

    if result[0:4] == "PING":
        pong = s.send(("PONG" + result[4:] + "\r\n").encode())
        print(pong)
        time.sleep(5)

    if len(result) == 0:
        break
