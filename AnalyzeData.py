#!/usr/bin/python
import sys

#array holding the categories that beat the other team
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
	return

tournamentFile = sys.argv[1]
teamFile = sys.argv[2]

teamF = open(teamFile, 'r')
teams = []
lineCount = 0
for line in teamF:
	if(lineCount != 0 or lineCount != 1):
		t = line.split(',')
		teams.append(t)
	lineCount = lineCount + 1
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
