import re

regex = re.compile(':waifu4u!waifu4u@waifu4u.tmi.twitch.tv PRIVMSG #saltybet :')
open = re.compile('Bets are OPEN for ')
win = re.compile('wins!')

#stripping the cruft from our chat string 
def strip(chat):
    '''strips out the IRC info from the message'''
    match = re.search(regex.pattern, chat)
    if match:
        msg = chat[match.end():]
        return msg
#if our chat string/message is announcing a match or declaring a winner, strip the cruft and return only the important bits        
def win_open(message):
    '''this will decide whether the message is announcing a winner or the start of
        a new match and strip out the relevant info as necessary
    '''
    openner = re.search(open.pattern, message)
    winner = re.search(win.pattern, message)
    tier = re.search('Tier', message)
    
    if openner:
            geg = openner.end()
            return message[geg:tier.end()+1]
    if winner:
            return message[:winner.end()]

#returns a list with our two fighters
def fighters(message):
    '''getting the individual fighters from a match announcnement and returning them as a list'''
    vs = message.find('vs')
    exclaim = message.find('!')
    
    fight_1 = message[:vs-1]
    fight_2 = message[vs+3:exclaim]
    
    return [fight_1, fight_2]

#returns the winner of the fight
def winner(message):
    '''getting the winner from a match end announcement'''
    return message[:message.find('wins')-1]

#returns the tier of the current match
def tier_strip(message):
    '''getting the tier from the match announcement'''
    return message[message.find('Tier')-2:message.find('Tier')-1]