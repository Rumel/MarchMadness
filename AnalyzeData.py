#!/usr/bin/python
import sys

#array holding the categories that beat the other team
winningNumbers = []

#Function to compare two teams
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

# The tournament file is the first argument
# Should be in format of "1 2 1" indicating team 1 played team 2 and team 1 won
# The team file is a csv file. I used data from kenpom.com
tournamentFile = sys.argv[1]
teamFile = sys.argv[2]

#This goes through the teams file and adds each teams stats to the array
teamF = open(teamFile, 'r')
teams = []
lineCount = 0
for line in teamF:
	if(lineCount != 0 or lineCount != 1):
		t = line.split(',')
		teams.append(t)
	lineCount = lineCount + 1
teamF.close()

#Opens the tournament file and cycles through the games
tournF = open(tournamentFile, 'r')
for line in tournF:
	game = line.split(' ')
	if(game[2] == game[0]):
		findStats(teams[int(game[0])], teams[int(game[1])])
	else:
		findStats(teams[int(game[1])], teams[int(game[0])])

#counts the instance of a number to help find a correlation between winning in the tournament and stats		
for i in range(0, 22):
	#Skips printing 0 or 2 since they are never used
	if(i == 0 or i == 2):
			None
	else:
		print i, "," , winningNumbers.count(i)
