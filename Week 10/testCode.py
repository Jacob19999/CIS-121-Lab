# ...existing code...
import random
import sys

# Simple terminal Blackjack
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['♠', '♥', '♦', '♣']

def create_deck():
    return [r + s for r in RANKS for s in SUITS]

def shuffle_deck():
    deck = create_deck()
    random.shuffle(deck)
    return deck

def card_value(card):
    rank = card[:-1]  # drop suit
    if rank in ['J', 'Q', 'K']:
        return 10
    if rank == 'A':
        return 11
    return int(rank)

def hand_value(hand):
    total = sum(card_value(c) for c in hand)
    # Adjust Aces from 11 to 1 as needed
    aces = sum(1 for c in hand if c[:-1] == 'A')
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def is_blackjack(hand):
    return len(hand) == 2 and hand_value(hand) == 21

def show_hand(hand, hide_first=False):
    if hide_first:
        return "[hidden], " + ", ".join(hand[1:])
    return ", ".join(hand)

def prompt_yes_no(prompt):
    while True:
        ans = input(prompt + " (y/n): ").strip().lower()
        if ans in ('y', 'yes'):
            return True
        if ans in ('n', 'no'):
            return False

def get_bet(bank):
    while True:
        try:
            bet = float(input(f"Place your bet (bank: {bank:.2f}): ").strip())
            if bet <= 0:
                print("Bet must be positive.")
            elif bet > bank:
                print("You don't have enough for that bet.")
            else:
                return round(bet, 2)
        except ValueError:
            print("Invalid bet. Enter a number.")

def player_turn(deck, hand):
    while True:
        val = hand_value(hand)
        print(f"Your hand: {show_hand(hand)} (value: {val})")
        if val >= 21:
            return val
        action = input("Hit or stand? (h/s): ").strip().lower()
        if action in ('h', 'hit'):
            card = deck.pop()
            hand.append(card)
            print("You drew:", card)
            continue
        if action in ('s', 'stand'):
            return hand_value(hand)
        print("Please enter 'h' or 's'.")

def dealer_turn(deck, hand):
    print("Dealer reveals:", show_hand(hand), "(value:", hand_value(hand), ")")
    while hand_value(hand) < 17:
        card = deck.pop()
        hand.append(card)
        print("Dealer draws:", card, "->", show_hand(hand), "(value:", hand_value(hand), ")")
    return hand_value(hand)

def resolve_round(player_hand, dealer_hand, bet, bank):
    player_val = hand_value(player_hand)
    dealer_val = hand_value(dealer_hand)
    player_blackjack = is_blackjack(player_hand)
    dealer_blackjack = is_blackjack(dealer_hand)

    if player_blackjack and not dealer_blackjack:
        winnings = bet * 1.5
        bank += bet + winnings
        print("Blackjack! You win 3:2 -> +{:.2f}".format(winnings))
    elif dealer_blackjack and not player_blackjack:
        bank -= bet
        print("Dealer has Blackjack. You lose.")
    elif player_val > 21:
        bank -= bet
        print("You busted. You lose.")
    elif dealer_val > 21:
        bank += bet
        print("Dealer busted. You win!")
    elif player_val > dealer_val:
        bank += bet
        print("You win!")
    elif player_val < dealer_val:
        bank -= bet
        print("You lose.")
    else:
        print("Push. Bet returned.")
    return bank

def run_blackjack():
    print("Welcome to Terminal Blackjack")
    bank = 100.0
    while bank > 0:
        print("\n--- New Round ---")
        print(f"Bank: {bank:.2f}")
        deck = shuffle_deck()
        bet = get_bet(bank)

        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        print("Dealer showing:", show_hand(dealer_hand, hide_first=True))
        print("Your hand:", show_hand(player_hand), "(value:", hand_value(player_hand), ")")

        # Check natural blackjacks
        if is_blackjack(player_hand) or is_blackjack(dealer_hand):
            print("Dealer reveals:", show_hand(dealer_hand), "(value:", hand_value(dealer_hand), ")")
            bank = resolve_round(player_hand, dealer_hand, bet, bank)
        else:
            # Player turn
            p_val = player_turn(deck, player_hand)
            if p_val <= 21:
                # Dealer turn
                d_val = dealer_turn(deck, dealer_hand)
            else:
                d_val = hand_value(dealer_hand)  # dealer didn't need to draw
            bank = resolve_round(player_hand, dealer_hand, bet, bank)

        print(f"End of round. Bank: {bank:.2f}")
        if bank <= 0:
            print("You're out of money. Game over.")
            break
        if not prompt_yes_no("Play another hand?"):
            break
    print("Thanks for playing. Final bank:", f"{bank:.2f}")

if __name__ == "__main__":
    try:
        run_blackjack()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting game.")
        sys.exit(0)
# ...existing code...