import chat_parser as chat

def get_stats(fighter, tier, stats):
    '''
        taking the a fighter from the list returned by the fighters function
        and retrieving the stats from the json file (if they exist) or creating
        the stats (if they do not exist).
    '''
    if fighter in stats[tier]:
        return stats[tier][fighter]
    else:
        return {'wins': 0, 'loses': 0}
    
def winner_loser(fighter1, fighter2, stats1, stats2, winner):
    '''
        takes two fighters, and the stats from them (retrived with get_Stats)
        and the winner from the winner function and adjusts the stats accordingly.
    '''
    if winner == fighter1:
        stats1['wins'] += 1
        stats2['loses'] += 1
    elif winner == fighter2:
        stats1['loses'] += 1
        stats2['wins'] += 1
    
    return stats1, stats2