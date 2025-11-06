def rps(p1, p2):
    #your code here
    beats = {"rock":"scissors", "paper":"rock", "scissors":"paper"}
    
    if p1 == p2:
        return "Draw!"
    elif beats[p1] == p2:
        return "Player 1 won!"
    elif beats[p2] == p1:
        return "Player 2 won!"