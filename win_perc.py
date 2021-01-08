# win percentage function which calculates the percentage of games won. 
# Write your win_percentage function here:
def win_percentage(wins, losses):
	total_num_games = wins + losses
	ratio_wins = wins / total_num_games
	per_ratio = ratio_wins * 100.00
	return per_ratio
# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100