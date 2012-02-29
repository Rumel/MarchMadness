#!/usr/bin/python
import sys

winningNumbers = []

def findStats(team1, team2):
	for i in range(0, 22):
		if(i == 0 or i == 2):
			None
		else:
			if(team1[i] >= team2[i]):
				winningNumbers.append(i)
			else:
				None
	
	if(team1[16] >= team2[18]):
		winningNumbers.append(22)
	if(team1[6] <= team2[8]):
		winningNumbers.append(23)
	return

tournamentFile = sys.argv[1]
teamFile = sys.argv[2]

teamF = open(teamFile, 'r')
teams = []
for line in teamF:
	t = line.split(',')
	teams.append(t)
	
teamF.close()

tournF = open(tournamentFile, 'r')
for line in tournF:
	game = line.split(' ')
	if(game[2] == game[0]):
		findStats(teams[int(game[0])], teams[int(game[1])])
	else:
		findStats(teams[int(game[1])], teams[int(game[0])])
	
for i in range(0, 24):
	print i, "," , winningNumbers.count(i)