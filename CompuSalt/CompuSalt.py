import socket
import re
from Salty_collector import salty_collector
from chat_parser import strip, win_open, fighters, winner, tier_strip
from stat_tracker import get_stats, winner_loser
import json
import os.path

#creates salty_stats.json if it doesn't already exist
stats_template = {'A': {}, 'B': {}, 'C': {}, 'P': {},
                'S': {}, 'X': {}}
if not os.path.exists('salty_stats.json'):
    with open('salty_stats.json', 'w') as salty:
        json.dump(stats_template, salty, indent = 4)

bot_owner = raw_input("Owner of this Bot: ")
nick = raw_input("Bot Username: ")
channel = "#saltybet"
server = "irc.twitch.tv"
password = raw_input('Bot Password: ')
irc = socket.socket()
irc.connect((server, 6667))
is_a_new_fight = False


irc.send("PASS " + password + "\r\n")
irc.send("USER " + nick + " 0 * :" + bot_owner + "\r\n")
irc.send("NICK " + nick + "\r\n")
irc.send("JOIN " + channel + "\r\n")

while True:
    try:
        data = irc.recv(1204)
        if data.find("PING") != -1:
            irc.send(data.replace("PING", "PONG"))
        if '(exhibitions)' not in data:
            if strip(data) and win_open(strip(data)):
                stripped = strip(data)
                winner_openner = win_open(stripped)
                with open('salty_stats.json', 'r+') as salty:
                    stats = json.load(salty)
                if 'Tier' in win_open(strip(data)) and not is_a_new_fight:
                    is_a_new_fight = True
                    combatants = fighters(winner_openner)
                    fighter1, fighter2, tier = combatants[0], combatants[1] , tier_strip(winner_openner)
                    stats1 = get_stats(fighter1, tier, stats)
                    stats2 = get_stats(fighter2, tier, stats)
                    #print fighter1, stats1, fighter2, stats2
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