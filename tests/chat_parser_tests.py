from nose.tools import *
from CompuSalt.chat_parser import strip, win_open, fighters, winner, tier_strip

def strip_test():
    parser = strip(':waifu4u!waifu4u@waifu4u.tmi.twitch.tv PRIVMSG #saltybet :Bets are OPEN for yamcha vs goku! (B Tier) (matchmaking) www.saltybet.com')
    
    assert_equal(parser, 'Bets are OPEN for yamcha vs goku! (B Tier) (matchmaking) www.saltybet.com')
    
def win_open_test():
    open = win_open('Bets are OPEN for yamcha vs goku! (B Tier) (matchmaking) www.saltybet.com')
    winner = win_open('yamcha wins! Payouts to Team Blue. 39 more matches until the next tournament!')
    
    assert_equal(open, 'yamcha vs goku! (B Tier)')
    assert_equal(winner, 'yamcha wins!')

def fighter_test():
    fighter_list = fighters('yamcha vs goku! (B Tier)')
    
    assert_equal(fighter_list, ['yamcha', 'goku'])
    
def winner_test():
    fight_winner = winner('yamcha wins!')
    
    assert_equal(fight_winner, 'yamcha')

def tier_strip_test():
    tier = tier_strip('Bets are OPEN for yamcha vs goku! (B Tier) (matchmaking) www.saltybet.com')
    
    assert_equal(tier, 'B')