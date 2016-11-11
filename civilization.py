import random
import sys

# python civilization.py "Martin Alex Rainbow" 3
if sys.argv[1] == '--help':
    print 'First argument is the name of the players, between quotes. Second argument is the number of civilization ' \
          'per players.'
    print 'Example : python civilization.py "Martin Alex Max" 3'
    sys.exit(2)

if len(sys.argv) != 3 :
    print 'Expected number of parameters : 2. '
    print 'Use --help for more information.'
    sys.exit(2)



players = sys.argv[1].split()
playerNumber = int(len(players))
choiceNumber = int(sys.argv[2])

print "Number of players in the game : " + str(playerNumber)
print "Number of possible civ per player : " + str(choiceNumber)

civList = ["America",
           "Arabia",
           "Aztec",
           "Brazil",
           "China",
           "Egypt",
           "England",
           "France",
           "Germany",
           "Greece",
           "India",
           "Japan",
           "Kongo",
           "Norway",
           "Rome",
           "Russia",
           "Scythia",
           "Spain",
           "Sumeria"]

sampleNumber = playerNumber * choiceNumber
if sampleNumber > len(civList):
    print "Not enough civ available. Decrease the number of players and/or the number of choice per player."

civSelection = random.sample(civList, sampleNumber)


for i in range(playerNumber):
    print "-------- Player " + players[i] + " --------"
    for j in range(choiceNumber):
        civSelected = civSelection[i * choiceNumber + j]
        print civSelected

