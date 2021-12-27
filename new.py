import socket
import sys


irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "irc.root-me.org"  # settings
channel = "#root-me_challenge"
botnick = "rumpler"
botname = "Candy"


def joinchan(channel):
    irc.send(bytes("JOIN " + channel + "\n", "UTF-8"))
    ircmsg = ""
    while ircmsg.find("END of /NAMES list.") == -1:
        ircmsg = irc.recv(2048).decode("UTF-8")
        ircmsg = ircmsg.strip("\n\r")


# defines the socket
def joinserv(server):
    irc.connect((server, 6667))  # connects to the server
    irc.send(
        bytes(
            "USER " + botnick + " " + botnick + " " + botnick + "\n",
            "UTF-8",
        )
    )  # user authentication
    irc.send(bytes("NICK " + botnick + "\n", "UTF-8"))
    ircmsg = ""
    while ircmsg.find("MODE bbot") == -1:
        ircmsg = irc.recv(2048).decode("UTF-8")
        ircmsg = ircmsg.strip("\n\r")
        # print(ircmsg)


def sendmsg(msg, target=channel):
    irc.send(bytes("PRIVMSG" + target + " :" + msg + "\n", "UTF-8"))


def main():

    joinserv(server)
    joinchan(channel)
    sendmsg("!ep1", botname)
    while True:  # puts it in a loop
        ircmsg = irc.recv(2048).decode("UTF-8")
        ircmsg = ircmsg.strip("\r\n")
        print(ircmsg)
        if ircmsg.find("PRIVMSG") != -1:
            print(ircmsg)


main()
