def tournamentWinner(competitions, results):
    round = 0
    score = {}
    competition_winner = None
    max_score = 0
    for competition in competitions:
        # get the particular round's winner 0 - awayTeam, 1 - homeTeam
        winner = results[round]
        # since arrays are indexed by 0 and the winniing team denotion is opposite of how the teams show up in [homeTeam, awayTeam]
        winner_index = int(not winner)
        winning_team = competition[winner_index]
        # set winner count in hashtable
        current_score = score.setdefault(winning_team, 0)
        score[winning_team] += 1
        # keep track of competition winner
        if score[winning_team] > max_score:
            max_score = score[winning_team] 
            competition_winner = winning_team
        round += 1

    return competition_winner
        
