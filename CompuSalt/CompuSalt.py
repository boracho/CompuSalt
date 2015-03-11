import socket
import re
from chat_parser import strip, win_open

bot_owner = raw_input("Owner of this Bot: ")
nick = raw_input("Bot Username: ")
channel = "#saltybet"
server = "irc.twitch.tv"
password = raw_input('Bot Password: ')
irc = socket.socket()
irc.connect((server, 6667))

irc.send("PASS " + password + "\r\n")
irc.send("USER " + nick + " 0 * :" + bot_owner + "\r\n")
irc.send("NICK " + nick + "\r\n")
irc.send("JOIN " + channel + "\r\n")

while True:
    try:
        data = irc.recv(1204)
    
    
        if data.find("PING") != -1:
            irc.send(data.replace("PING", "PONG"))
    
    except socket.error:
        print 'There has been an Error!  Make sure your info is right'