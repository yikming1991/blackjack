############### Our Blackjack House Rules #####################
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
game_ongoing = True
while game_ongoing:
    import random

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = []
    dealer_cards = []
    player_turn = True
    dealer_turn = True
    is_game_over = False


    def deal_cards():
        for _ in range(2):
            return random.choices(cards, k=2)


    def calculate_score(hand):
        score = sum(hand)
        if score == 21 and len(hand) == 2:
            score = "Blackjack"
        elif 11 in hand and score > 21:
            hand.remove(11)
            hand.append(1)
            score -= 10
        return score


    def blackjack(player_score, dealer_score):
        if player_score == 0:
            player_turn = False
            dealer_turn = False
            return "You got blackjack, you win!"
        if dealer_score == 0:
            return "The dealer got blackjack, you lose."


    def final_result(player_score, dealer_score):
        print(f"\nPlayer's final cards: {player_cards}, player's final score: {player_score}\n"
              f"Dealer's final cards: {dealer_cards}, dealer's final score: {dealer_score}")
        if player_score == "Blackjack":
            return "You got Blackjack, you win!"
        if dealer_score == "Blackjack":
            return "The dealer got Blackjack, you lose."
        elif player_score > 21:
            return "You went bust, you lose."
        elif player_score == dealer_score:
            return "You tied with the dealer."
        elif player_score < 22 and dealer_score < 22:
            if player_score > dealer_score:
                return "You win!"
            else:
                return "You lose."
        elif dealer_score > 21:
            return "The dealer went bust, you win!"


    player_cards = deal_cards()
    dealer_cards = deal_cards()
    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)
    if player_score == "Blackjack" or dealer_score == "Blackjack" or player_score > 21:
        is_game_over = True

    while not is_game_over:
        while player_turn:
            print(f"\nPlayer's cards: {player_cards}, player's score: {player_score}")
            print(f"Dealer's first card: {dealer_cards[0]}")
            if player_score == 21 and len(player_cards) == 2:
                player_turn = False
            elif player_score < 21:
                additional_card = input("Do you want an additional card? Type 'y' for yes, 'n' for no. ").lower()
                if additional_card == "y":
                    player_cards.append(random.choice(cards))
                    player_score = calculate_score(player_cards)
                elif additional_card == "n":
                    player_turn = False
            elif player_score >= 21:
                player_turn = False

        while dealer_turn:
            print(f"Dealer's cards: {dealer_cards}")
            if dealer_score < 17:
                dealer_cards.append(random.choice(cards))
                dealer_score = calculate_score(dealer_cards)
            elif dealer_score >= 17:
                dealer_turn = False

        is_game_over = True

    print(final_result(player_score, dealer_score))
    to_continue = input("\nDo you want to continue playing? Type 'y' for yes, 'n' for no. ").lower()
    if to_continue == "n":
        game_ongoing = False
