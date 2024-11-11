import random



def random_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare_score(u_score, c_score):
    if u_score == c_score:
        return "Draw 🫥"
    elif c_score == 0:
        return "Lose, opponent has  Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack"
    elif u_score > 21:
        return "You went over. You lose! 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win! 😀"
    else:
        return "You lose 😤"


def game():
    player_cards = []
    computer_cards = []
    computer_score = -1
    is_game_over = False
    player_credit = 0

    if player_credit == 0:
        print("To start playing game you first need to deposit money! Minimum deposit is 100$")
        credit = int(input("Deposit money: "))
        player_credit += credit

    for _ in range(2):
        player_cards.append(random_card())
        computer_cards.append(random_card())

    while not is_game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Players current cards: {player_cards}, with score: {player_score}")
        print(f"Computer current cards: {computer_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            another_card = input("Do you want to get another card? 'y' / 'n': ")
            if another_card == 'y':
                player_cards.append(random_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(random_card())
        computer_score = calculate_score(computer_cards)

    print(f"Users final cards: {player_cards}, with final score: {player_score}")
    print(f"Computer final cards: {computer_cards}, with final score: {computer_score}")
    print(compare_score(player_score, computer_score))

    if player_score == 0:
        player_credit += 5
        print(f"Player win, and gain additional 5 credits, current credit balance is: {player_credit}")
    elif player_score > computer_score < 21:
        player_credit += 5
        print(f"Player win, and gain additional 5 credits, current credit balance is: {player_credit}")
    elif player_score > computer_score > 21:
        player_credit -= 5
        print(f"Computer wins, player lose 5 credits, current balance is: {player_credit}")
    elif computer_score == 0:
        player_credit -= 5
        print(f"Computer wins, player lose 5 credits, current balance is: {player_credit}")
    else:
        player_credit -= 5
        print(f"Computer wins, player lose 5 credits, current balance is: {player_credit}")


while input("Do you want to play a game of blackjack? 'y' or 'n' ") == 'y':
    print("\n" * 20)
    game()

