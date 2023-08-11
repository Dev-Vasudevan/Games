players=[]
global current_round
current_round = []
global prev_round
prev_round=[]
money={}
index=1
t=0
n=int(input("Enter Number of players"))
for t in range (n):
    players.append(input("Enter name of player {}".format(t+1)))

i = 0
money = {}
cash = int(input("Enter purse amount"))
for i in range(n):
    money[players[i]] = cash
buy_in =(int(input("Enter buy in amount")))

player1 = 1

k=0
while True:


    match_bet = buy_in
    pot=0
    bet = 0
    current_round=[]
    prev_round=[]
    loan=input("Number of loans")
    if (loan!=""):
        loan=int(loan)

        for ln in range (loan):
            r=input("Richer player")
            g=input("Gareeb")
            amt=int(input("Amount"))
            money[r]=money[r]-amt
            money[g] = money[g] + amt
            print(money)

    for i in range(player1, n):
        current_round.append(players[i])
        prev_round.append(players[i])
    for i in range(0, player1):
        current_round.append(players[i])
        prev_round.append(players[i])
    print(current_round)

    buy_in = int(buy_in)

    for p in current_round:
        money[p] = money[p] - buy_in

    turns = 0


    pot = buy_in * len(current_round)


    for turns in range(6):


        print("To fold type 'fold' or 'f' to raise enter the amount or to check type 'check' or 'c' ")
        for p in current_round:

            action = input("{}:".format(p))

            if (action == "fold" or action == "f"):
                prev_round.remove(p)

                continue
            if (action == "check" or action == "c"):
                continue

            elif (action.isdigit() == True):
                bet = bet + int(action)

        current_round = prev_round.copy()

        for p in current_round:
            money[p] = money[p] - bet
        pot = pot + len(current_round) * bet

        match_bet = match_bet + bet
        bet = 0
        print("Bet is at {} and pot is at {}".format(match_bet, pot))
        if len(current_round) == 1:
            money[current_round[0]] = money[current_round[0]] + pot
            print(money)
            k=1
            break


    current_round=[]
    player1 = (player1 + 1) % n

    if k==1:
        k=0
        continue
    win = input("Enter name of winner")
    money[win]=money[win]+pot
    print(money)


























