import random
players = ["messi","rolnaldo","ronaldinyo","daghair"]

teamA = []
teamB = []

while len(players) > 0 :  
    
    playersA = random.choice(players)
    
    teamA.append(playersA)
    
    players.remove(playersA)
    

    
    
    playersB = random.choice(players)
    teamB.append(playersB)
    players.remove(playersB)
    
    
    
    print('TEAMA' ,teamA)
    print('TEAMB' ,teamB)