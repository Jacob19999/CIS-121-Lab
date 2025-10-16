# Try these questions below

# Question 4
#  def find_winner(player1, player2 ): -> Player 1 and 2 is mandatory !
def find_winner(player1 = "rock", player2 = "rock"):

    if player1 == player2:
        return "It is a Tie"
    
    if (player1 == "rock" and player2 == "scissors") or (player1 == "scissors" and player2 == "paper") or (player1 == "paper" and player2 == "rock"):
        return "Player 1 wins"
    else:
        return "player 2 Wins"


#print(find_winner("rock", "scissors"))
#print(find_winner())

# Question 8
def descending_order(num1, num2 = 15, num3 = 3):

    a, b, c = num1 , num2 , num3

   # a = num1
   # b = num2
   # c = num3

    if a < b:
        a , b = b , a
    if a < c:
        a , c = c , a
    if b < c:
        b , c = c , b

    return [a ,b, c]

#print(descending_order(1,2,3))
#print(descending_order(1))


# Question 15