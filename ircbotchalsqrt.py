import sys
import socket
import math
server = 'irc.root-me.org'
port = 6667
channel='#root-me_challenge'
nick = 'Bahobot'
bot = 'Candy'


irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def joinchan(channel):
    irc.send(bytes("JOIN "+ channel +"\n", "UTF-8"))
    ircmsg = ""
    while ircmsg.find("End of /NAMES list.") == -1:
        ircmsg = irc.recv(2048).decode("UTF-8")
        ircmsg = ircmsg.strip('\n\r')
        print(ircmsg)



def joinserv(server):
    irc.connect((server, 6667))
    irc.send(bytes("USER "+ nick +" "+ nick +" "+ nick + " " + nick+"\n", "UTF-8"))
    irc.send(bytes("NICK "+ nick +"\n", "UTF-8"))
    ircmsg = ""
    while ircmsg.find('MODE Bahobot') == -1:
        ircmsg = irc.recv(2048).decode("UTF-8")
        ircmsg = ircmsg.strip('\n\r')
        print(ircmsg)

def sendmsg(msg, target = channel):
    irc.send(bytes("PRIVMSG " + target + " :"+ msg +"\n", "UTF-8"))
    # irc.send("PRIVMSG nickserv :iNOOPE\r\n")    #auth
def main():
    joinserv(server)
    joinchan(channel)
    sendmsg('!ep1', bot)
    while True:
        ircmsg = irc.recv(2048).decode("UTF-8")
        ircmsg = ircmsg.strip("\r\n")
        print(ircmsg)
        if ircmsg.find("PRIVMSG") != -1:
            print(ircmsg)
            msg1 = ircmsg.split(" ")
            number1 =  int(msg1[3][1:])
            number2 = int(msg1[5])
            answer = round(math.sqrt(number1) * number2, 2)
            sendmsg('!ep1 -rep {}'.format(answer), bot)




main()
#VALIDATED