def CalcScore(deck):
    numcards = len(deck)
    score = 0
    for i,card in enumerate(deck):
        score += (i+1)*deck[numcards-i-1]
    return score

def PlayNormal(deck1, deck2):
    player1_deck = deck1.copy()
    player2_deck = deck2.copy()
    while len(player1_deck) > 0 and len(player2_deck) > 0:
        player1_card = player1_deck.pop(0)
        player2_card = player2_deck.pop(0)
        if player1_card > player2_card:
            player1_deck += [player1_card]
            player1_deck += [player2_card]
        else:
            player2_deck += [player2_card]
            player2_deck += [player1_card]
    if len(player1_deck) > 0:
        return 1, CalcScore(player1_deck)
    else:
        return 2, CalcScore(player2_deck)

def PlayRecursive(deck1, deck2):
    player1_deck = deck1.copy()
    player2_deck = deck2.copy()
    player1_history = []
    player2_history = []
    player1_stack_matches_history = False
    player2_stack_matches_history = False
    while len(player1_deck) > 0 and len(player2_deck) > 0:
        # match with history
        player1_stack = ""
        for card in player1_deck:
            player1_stack += str(card)
        if player1_history.__contains__(player1_stack):
            player1_stack_matches_history = True
            break
        else:
            player1_history += [player1_stack]
        player2_stack = ""
        for card in player2_deck:
            player2_stack += str(card)
        if player2_history.__contains__(player2_stack):
            player2_stack_matches_history = True
            break
        else:
            player2_history += [player2_stack]

        player1_card = player1_deck.pop(0)
        player2_card = player2_deck.pop(0)

        #check number of cards
        if player1_card <= len(player1_deck) and player2_card <= len(player2_deck):
            game_outcome,_ = PlayRecursive(player1_deck[0:player1_card], player2_deck[0:player2_card])
            if game_outcome == 1:
                player1_deck += [player1_card]
                player1_deck += [player2_card]
            else:
                player2_deck += [player2_card]
                player2_deck += [player1_card]
            continue

        if player1_card > player2_card:
            player1_deck += [player1_card]
            player1_deck += [player2_card]
        else:
            player2_deck += [player2_card]
            player2_deck += [player1_card]

    if player1_stack_matches_history or player2_stack_matches_history:
        return 1,CalcScore(player1_deck)
    elif len(player1_deck)>0:
        return 1,CalcScore(player1_deck)
    elif len(player2_deck)>0:
        return 2,CalcScore(player2_deck)

file = open("input.txt")
lines = file.readlines()

player1_deck = []
player2_deck = []
playernum = 0
for line in lines:
    line = line.strip()
    if line == "Player 1:":
        playernum = 1
    elif line == "Player 2:":
        playernum = 2
    if line.isdigit():
        if playernum == 1:
            player1_deck += [int(line)]
        elif playernum == 2:
            player2_deck += [int(line)]

print(player1_deck)
print(player2_deck)

print(PlayRecursive(player1_deck,player2_deck))