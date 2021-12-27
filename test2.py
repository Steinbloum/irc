import socket, re, subprocess, os, time, threading, sys

# Some basic variables used to configure the bot        
server = "irc.root-me.org" # Server
channel = "#root-me_challenge" # Channel
botnick = "Bahobotboy" # Your bots nick
password = ""
lines = 0
#regexes = [".*"]
#combined = "(" + ")|(".join(regexes) + ")"
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667)) # Here we connect to the server using the port 6667
ircsock.send(bytes("USER "+ botnick +" "+ botnick +" "+ botnick + " " + botnick + "\n", "UTF-8")) # user authentication
ircsock.send(bytes("NICK "+ botnick +"\n", "UTF-8")) # assign the nick to the bot

def ping(): # respond to server Pings.
  ircsock.send(bytes("PONG :pingis\n", "UTF-8"))

def sendmsg(msg): # sends messages to the channel.
  ircsock.send(bytes("PRIVMSG "+ channel +" :"+ msg +"\n", "UTF-8"))

def joinchan(chan): # join channel(s).
  ircsock.send(bytes("JOIN "+ chan +"\n", "UTF-8"))

def whisper(msg, user): # whisper a user 
  ircsock.send(bytes("PRIVMSG " + user + ' :' + msg.strip('\n\r') + '\n', "UTF-8"))

def main():
  # start by joining the channel. --TO DO: allow joining list of channels
  joinchan(channel)
  print("we joined")
  # open the chat log file if it exists and delete it to start fresh.
  while 1: 
    # clear ircmsg value every time
    ircmsg = ""
    # set ircmsg to new data received from server
    ircmsg = ircsock.recv(2048)
    ircmsg= ircmsg.decode("UTF-8", 'ignore')
    # remove any line breaks
    ircmsg = ircmsg.strip('\n\r') 
    # print received message to stdout (mostly for debugging).
    print(ircmsg) 
    # repsond to pings so server doesn't think we've disconnected
    if ircmsg.find("PING :") != -1: 
      ping()
    # look for PRIVMSG lines as these are messages in the channel or sent to the bot
    if ircmsg.find("PRIVMSG") != -1:
      # save user name into name variable
      name = ircmsg.split('!',1)[0][1:]
      print('name: ' + name)
      # get the message to look for commands
      message = ircmsg.split('PRIVMSG',1)[1].split(':',1)[1]
      print(message)
main()