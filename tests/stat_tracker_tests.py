from nose.tools import *
from CompuSalt.stat_tracker import get_stats, winner_loser

def test_get_stats():
    make_stats = get_stats('yamcha', 'B', {'A': {}, 'B': {}, 'C': {}, 'P': {}, 'X': {}})
    got_stats = get_stats('yamcha', 'B', {'A': {}, 'B': {'yamcha': {'wins': 1, 'loses': 0}}, 'C': {}, 'P': {}, 'X': {}})
    
    assert_equal(make_stats, {'wins': 0, 'loses': 0})
    assert_equal(got_stats, {'wins': 1, 'loses': 0})
    
def test_winner_loser():
    goku_wins = winner_loser('yamcha', 'goku', {'wins': 0, 'loses': 0}, {'wins': 0, 'loses': 0}, 'goku')
    
    assert_equal(goku_wins, ({'wins': 0, 'loses': 1}, {'wins': 1, 'loses': 0}))
    