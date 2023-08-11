
def check(a):
    checker=0
    for i in range (3):
        for t in range (3):

            if a[i][t]=="-":
               break
                #if nothing exists skip

            if i==t:
                #checking diagonals
                for q in range (3):
                    if a[q][q]==a[i][t]:
                        checker+=1
                    if checker==3:
                        return(a[i][t])
                if checker>0:
                    checker=0
            if (i==2-t) or (2-i==t):
                for q in range (3):
                    if a[2-q][q]==a[i][t]:
                        checker+=1
                    if checker==3:
                        return(a[i][t])
                if checker>0:
                    checker=0


            else:
                #checcking colums and rows
                checker_=0
                for q in range (3):
                    if a[i][q]==a[i][t] :
                        checker+=1


                    if a[q][t]==a[i][t]:
                        checker_+=1
                if checker==3 or checker_==3:
                    return(a[i][t])
                checker_=0
                checker = 0
    return("B")
def print_matrix(a):
    for i in range(3):
        for t in range(3):
            print(a[i][t],end=" ")
        print(" ")


#each element is a row
def game():
    a=[["-","-","-",],["-","-","-"],["-","-","-"]]
    z=0
    while z<=9:
        print("Player X")
        r,c=input("Enter square to occupy in form r c").split()
        r=int(r)-1
        c=int(c)-1
        a[r][c]="X"
        b=check(a)
        z+=1
        print_matrix(a)
        if b!="B":
            return(b+"WON!")
            
        if z==9:
            break
        print("Player O")
        r, c = input("Enter square to occupy in form r,c").split()
        r = int(r) - 1
        c = int(c) - 1
        a[r][c] = "O"
        b = check(a)
        print_matrix(a)
        if b != "B":
            return(b + " WON !")
            
            z+=1
    if z==9:
        return("Match is Drawn")
while True:
    b=game()
    print(b)
    a=input("Do you want to play again?(Yes/No)")
    if a=="No":
        break
    










