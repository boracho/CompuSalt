import chat_parser as chat

def get_stats(fighter, tier, stats):
    if fighter in stats[tier]:
        return stats[tier][fighter]
    else:
        return {'wins': 0, 'loses': 0}
    
def winner_loser(fighter1, fighter2, stats1, stats2, winner):
    if winner == fighter1:
        stats1['wins'] += 1
        stats2['loses'] += 1
    elif winner == fighter2:
        stats1['loses'] += 1
        stats2['wins'] += 1
    
    return stats1, stats2