import random

def create_deck():
    deck = []
    for i in range(7):
        for j in range(i, 7):
            deck.append((i, j))
    random.shuffle(deck)
    return deck

def play_game():
    deck = create_deck()
    player_hand = deck[:7]
    computer_hand = deck[7:14]
    boneyard = deck[14:]

    board = []
    while True:
        print("Board is now:", board)
        print("Your hand:", player_hand)
        playable_tiles = [tile for tile in player_hand if board == [] or tile[0] in board[-1] or tile[1] in board[-1]]
        if playable_tiles == []:
            print("You can't play. Drawing from boneyard.")
            if len(boneyard) > 0:
                player_hand.append(boneyard.pop(0))
            else:
                print("Boneyard is empty. Computer wins!")
                break
        else:
            print("Playable tiles:", playable_tiles)
            played_tile = input("Enter tile to play (e.g. 2-5) or pass (p): ")
            if played_tile.lower() == 'p':
                if len(boneyard) > 0:
                    player_hand.append(boneyard.pop(0))
                    print("You drew a tile from the boneyard.")
                else:
                    print("Boneyard is empty. Computer's turn.")
                computer_played = False
            else:
                played_tile = tuple(map(int, played_tile.split("-")))
                if played_tile in playable_tiles:
                    player_hand.remove(played_tile)
                    board.append(played_tile)
                    print("You played:", played_tile)
                    if len(player_hand) == 0:
                        print("You won!")
                        break
                    computer_played = True
                else:
                    print("Invalid tile. Try again.")
                    computer_played = False
            if computer_played:
                print("Computer's turn.")
                computer_playable_tiles = [tile for tile in computer_hand if board[-1][1] in tile or board[0][0] in tile]
                if len(computer_playable_tiles) == 0:
                    if len(boneyard) > 0:
                        computer_hand.append(boneyard.pop(0))
                        print("Computer drew a tile from the boneyard.")
                    else:
                        print("Boneyard is empty. Your turn.")
                        continue
                else:
                    computer_played_tile = random.choice(computer_playable_tiles)
                    computer_hand.remove(computer_played_tile)
                    board.append(computer_played_tile)
                    print("Computer played:", computer_played_tile)
                    if len(computer_hand) == 0:
                        print("Computer wins!")
                        break
            else:
                continue
            print()

play_game()
