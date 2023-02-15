def rock_paper_scissor(hands: tuple) -> str:
    
    posible_hands = {
                    "scissors": ["paper", "lizard"],
                    "paper": ["rock", "spock"],
                    "rock": ["lizard", "scissors"],
                    "lizard": ["spock", "paper"],
                    "spock": ["scissors", "rock"],            
                    }
    
    player_1_points = 0
    player_2_points = 0
    
    player_1_hand = hands[0]
    player_2_hand = hands[1]
    print(f"Player 1: {player_1_hand}")
    print(f"Player 2: {player_2_hand}")
    print(f"posible_hands pos p2 {posible_hands[player_2_hand]}")
    
    if player_1_hand != player_2_hand:
        #   "rock"        "scissors"
        # "scisscors"     "paper"
        # "spock"         "lizard"
        if player_1_hand in posible_hands[player_2_hand]:
            player_2_points += 1
        else:
            player_1_points += 1
# print(f"{player_1_points} {player_2_points}")

    return "Tie" if player_1_points == player_2_points else "Ganador player 1" if player_1_points > player_2_points else "Ganador player 2"

def main():
    print(rock_paper_scissor(("rock", "scissors")))
    print(rock_paper_scissor(("scisscors", "paper")))
    print(rock_paper_scissor(("spock", "lizard")))
    print(rock_paper_scissor(("spock", "spock")))
    
if __name__ == "__main__":
    main()
    