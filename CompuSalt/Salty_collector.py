from chat_parser import strip, win_open, fighters, winner, tier_strip
from stat_tracker import get_stats, winner_loser
import json



def salty_collector(data):
    is_a_new_fight = False
    if strip(data) and win_open(strip(data)):
        stripped = strip(data)
        winner_openner = win_open(stripped)
        if '(exhibitions)' not in stripped:
            with open('salty_stats.json', 'r+') as salty:
                stats = json.load(salty)
            if 'Tier' in win_open(strip(data)) and not is_a_new_fight:
                is_a_new_fight = True
                combatants = fighters(winner_openner)
                fighter1, fighter2, tier = combatants[0], combatants[1] , tier_strip(winner_openner)
                stats1 = get_stats(fighter1, tier, stats)
                stats2 = get_stats(fighter2, tier, stats)
                print fighter1, stats1, fighter2, stats2
            if 'wins!' in winner_openner and is_a_new_fight:
                is_a_new_fight = False
                current_stats = winner_loser(fighter1, fighter2, stats1, stats2, winner(winner_openner))
                with open('salty_stats.json', 'r+') as salty:
                    stats = json.load(salty)
                    stats[tier][fighter1] = current_stats[0]
                    stats[tier][fighter2] = current_stats[1]
                    salty.seek[0]
                    json.dump(stats, salty, indent = 4)
                