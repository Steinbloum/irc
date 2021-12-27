import socket

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "irc.root-me.org"
ircsock.connect((server, 6667))
channel = "#root-me_challenge"

def joinchan(chan): # join channel(s).  
    ircsock.send(bytes("JOIN "+ chan +"n", "UTF-8"))   
    ircmsg = ""  
    while ircmsg.find("End of /NAMES list.") == -1:      
        ircmsg = ircsock.recv(2048).decode("UTF-8")    
        ircmsg = ircmsg.strip('nr')    
        print(ircmsg)
def ping(): # respond to server Pings.  
    ircsock.send(bytes("PONG :pingisn", "UTF-8"))

def sendmsg(msg, target=channel): # sends messages to the target.  
    ircsock.send(bytes("PRIVMSG "+ target +" :"+ msg +"n", "UTF-8"))

def main():  
    joinchan(channel) 
    while 1:
        ircmsg = ircsock.recv(2048).decode("UTF-8")    
        ircmsg = ircmsg.strip('nr')    
        print(ircmsg)
        if ircmsg.find("PRIVMSG") != -1:      
            name = ircmsg.split('!',1)[0][1:]      
            message = ircmsg.split('PRIVMSG',1)[1].split(':',1)[1]
            print(name)
            if len(name) < 17:        
                # if message.find('Hi ' + botnick) != -1:          
                #     sendmsg("Hello " + name + "!")        
                #     if message[:5].find('.tell') != -1:          
                #     target = message.split(' ', 1)[1]          
                #     if target.find(' ') != -1:              
                #     message = target.split(' ', 1)[1]              
                #     target = target.split(' ')[0]          
                #     else:             
                #         target = name              
                #         message = "Could not parse. The message should be in the format of ‘.tell [target] [message]’ to work properly."          
                #         sendmsg(message, target)
                print('name less than 17')
        else :
            if ircmsg.find("PING :") != -1:  
                ping()


main()