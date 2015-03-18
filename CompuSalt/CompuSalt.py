import socket
import re
from chat_parser import strip, win_open, fighters, winner, tier_strip
from stat_tracker import get_stats, winner_loser
import json
import os.path



bot_owner = raw_input("Owner of this Bot: ")
nick = raw_input("Bot Username: ")
channel = "#saltybet"
server = "irc.twitch.tv"
password = raw_input('Bot Password: ')

#this is so we don't have to type the IRC suffix over
irc_line_end = '\r\n'

#this bool value is for if we activate the bot in the middle of a match and haven't retrieved the relavent
#info to send to our salty stats file.  Will hopefully catch a few possible errors. 
is_a_new_fight = False

#creates salty_stats.json if it doesn't already exist
stats_template = {'A': {}, 'B': {}, 'C': {}, 'P': {},
                'S': {}, 'X': {}}
if not os.path.exists('salty_stats.json'):
    with open('salty_stats.json', 'w') as salty:
        json.dump(stats_template, salty, indent = 4)

#opening our socket to the IRC server
irc = socket.socket()
irc.connect((server, 6667))


#connecting to the irc server using our password and bot username.
irc.send("PASS %s  %s" % (password, irc_line_end))
irc.send("USER %s %s %s %s" % (nick, " 0 * :", bot_owner, irc_line_end))
irc.send("NICK %s %s" % (nick, irc_line_end))
irc.send("JOIN %s %s" % (channel, irc_line_end))

#our main loop.  some of this logic needs to be moved into a function or group of functions.  A little confusing as is. 
while True:
    try:
        #receiving our data from the IRC server.
        data = irc.recv(1204)
        #pinging the IRC server when we get the approriate message.
        if data.find("PING") != -1:
            irc.send(data.replace("PING", "PONG"))
            
        #we don't want to record exhib matches, because individual team members are not announced.  and also veku.
        if '(exhibitions)' not in data:
            #we don't want to do anything to our message if the strip and win_open functions return None.
            if strip(data) and win_open(strip(data)):
                stripped = strip(data)
                winner_openner = win_open(stripped)
                
                with open('salty_stats.json', 'r+') as salty:
                    stats = json.load(salty)
                
                #this looks for our Opener announcement.  Could use improvement, as 'Tier' appears in messages that aren't the
                #announcement of a new match.
                if 'Tier' in win_open(strip(data)) and not is_a_new_fight:
                    is_a_new_fight = True
                    combatants = fighters(winner_openner)
                    
                    fighter1, fighter2, tier = combatants[0], combatants[1] , tier_strip(winner_openner)
                    stats1 = get_stats(fighter1, tier, stats)
                    stats2 = get_stats(fighter2, tier, stats)
                
                
                if 'wins!' in winner_openner and is_a_new_fight:
                    is_a_new_fight = False
                    current_stats = winner_loser(fighter1, fighter2, stats1, stats2, winner(winner_openner))
                    
                    with open('salty_stats.json', 'r+') as salty:
                        stats = json.load(salty)
                        stats[tier][fighter1] = current_stats[0]
                        stats[tier][fighter2] = current_stats[1]
                        salty.seek(0)
                        json.dump(stats, salty, indent = 4)
        
    
    except socket.error:
        print 'There has been an Error!  Make sure your info is right'
        break