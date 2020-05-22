import os
import random
from tkinter import*


def calc_hand(hand):
    non_aces = [c for c in hand if c != '1']
    aces = [c for c in hand if c == '1']
    sum = 0
    for card in non_aces:
        if card in 'jqk':
            sum += 10
        else:
            sum += int(card)
    for card in aces:
        if sum <= 10:
            sum += 11
        else:
            sum += 1
    return sum

def Hit():

    
    global NumberOfCard
    global Playercardimage

    NumberOfCard = NumberOfCard + 1

    player.append(cards.pop())
    
    Playercardimage[NumberOfCard]= PhotoImage(file = "cards_gif/"'s'+player[NumberOfCard]+".gif")
    Card3_player=Label(image=Playercardimage[NumberOfCard],bg="green")
    Card3_player.grid(row=4,column=NumberOfCard)

    
    player_score = calc_hand(player)
    Display_pl_sco= Label(root, text=str(player_score),bg="green",fg="yellow")
    Display_pl_sco.grid(row=3,column=1)

    if calc_hand(player) > 21:

        
        YouBusted.grid(row=6,column=0,columnspan=3)
        Display_deal_sco= Label(root, text=str(dealer_score),bg="green",fg="yellow")
        Display_deal_sco.grid(row=1,column=1)
        
        
    elif calc_hand(player) == 21:
        BlackJack1.grid(row=6,column=0,columnspan=3)
        Display_deal_sco= Label(root, text=str(dealer_score),bg="green",fg="yellow")
        Display_deal_sco.grid(row=1,column=1)    


def Stand():
    
    
    global NumberOfCardDealer
    global Dealercardimage
    
    global Dealercard1
    Dealercard1 = PhotoImage(file = "cards_gif/"'c'+dealer[0]+".gif")
    Card1_dealer=Label(image=Dealercard1,bg="green")
    Card1_dealer.grid(row=2,column=0)

                       
    if calc_hand(dealer) <= 16:

        while calc_hand(dealer) <= 16:
            
            NumberOfCardDealer=NumberOfCardDealer+1
            dealer.append(cards.pop())
       
            Dealercardimage[NumberOfCardDealer] = PhotoImage(file = "cards_gif/"'s'+dealer[NumberOfCardDealer]+".gif")
            Card_dealer=Label(image=Dealercardimage[NumberOfCardDealer])
            Card_dealer.grid(row=2,column=NumberOfCardDealer)
        
        if  calc_hand(dealer) > 21:
            DealBusted.grid(row=6,column=0,columnspan=3)
            Display_deal_sco= Label(root, text=str(calc_hand(dealer)),bg="green",fg="white")
            Display_deal_sco.grid(row=1,column=1)   
        elif calc_hand(player) ==  calc_hand(dealer):
            Draw.grid(row=6,column=0,columnspan=3)
            Display_deal_sco= Label(root, text=str(calc_hand(dealer)),bg="green",fg="white")
            Display_deal_sco.grid(row=1,column=1)
        elif calc_hand(player) >  calc_hand(dealer):
            YouWin.grid(row=6,column=0,columnspan=3)
            Display_deal_sco= Label(root, text=str(calc_hand(dealer)),bg="green",fg="white")
            Display_deal_sco.grid(row=1,column=1)
        else:
            Youloss.grid(row=6,column=0,columnspan=3)
            Display_deal_sco= Label(root, text=str(calc_hand(dealer)),bg="green",fg="white")
            Display_deal_sco.grid(row=1,column=1)

            
    else:
                
        if  calc_hand(dealer) > 21:
            DealBusted.grid(row=6,column=0,columnspan=3)
            Display_deal_sco= Label(root, text=str(calc_hand(dealer)),bg="green")
            Display_deal_sco.grid(row=1,column=1)   
        elif calc_hand(player) ==  calc_hand(dealer):
            Draw.grid(row=6,column=0,columnspan=3)
            Display_deal_sco= Label(root, text=str(calc_hand(dealer)),bg="green")
            Display_deal_sco.grid(row=1,column=1)
        elif calc_hand(player) >  calc_hand(dealer):
            YouWin.grid(row=6,column=0,columnspan=3)
            Display_deal_sco= Label(root, text=str(calc_hand(dealer)),bg="green")
            Display_deal_sco.grid(row=1,column=1)
        else:
            Youloss.grid(row=6,column=0,columnspan=3)
            Display_deal_sco= Label(root, text=str(calc_hand(dealer)),bg="green")
            Display_deal_sco.grid(row=1,column=1)

root= Tk()


NumberOfCard=1
NumberOfCardDealer=1


root.title("Blackjack")
root.geometry("640x400")
root.configure(background="green")


#
Welcome = Label(root, text="BlackJack",bg="green",fg="white",font=("BlackJack", 15))
Dealer  = Label(root, text="Dealer",bg="green",fg="white")
Player = Label(root, text="Player",bg="green",fg="white")
#

#
YouBusted= Label(root, text="You busted!",bg="green",fg="yellow")
YouWin= Label(root, text="Awesome, you win",bg="green",fg="yellow")
Youloss= Label(root, text="You Loss",bg="green",fg="yellow")
DealBusted= Label(root, text="Dealer busted, you win!",bg="green",fg="yellow")
Draw= Label(root, text="Push, nobody wins",bg="green",fg="yellow")
BlackJack1= Label(root, text="Nice! BlackJack, you win!",bg="green",fg="yellow")
BlackJack2= Label(root, text="Dealer BlackJack, you loss!",bg="green",fg="yellow")
#

#
button_quit = Button(root, text="Quit", command=root.quit,bg="green",fg="white")
button_stand = Button(root, text="Stand",  command=Stand,bg="green",fg="white")
button_hit = Button(root, text="Hit",  command=Hit,bg="green",fg="white")
#

Copyright= Label(root, text="---Developed by Jack Zhening Huang---",bg="green",fg="white")

cards = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', '1',
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', '1',
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', '1',
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', '1',
]

random.shuffle(cards)

##shuffle##
dealer = []
player = []

##
Playercardimage=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]


Dealercardimage=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]


##pop out and remove##
player.append(cards.pop())
dealer.append(cards.pop())
player.append(cards.pop())
dealer.append(cards.pop())


player_score = calc_hand(player)
dealer_score = calc_hand(dealer)

Display_pl_sco= Label(root, text=str(player_score),bg="green",fg="white")
Display_deal_sco= Label(root, text="x",bg="green",fg="white")

# initial four cards display
Dealercard1 = PhotoImage(file = "cards_gif/b1fv.gif")
Dealercard2 = PhotoImage(file = "cards_gif/"'c'+dealer[1]+".gif")
Playercard1 = PhotoImage(file = "cards_gif/"'h'+player[0]+".gif")
Playercard2 = PhotoImage(file = "cards_gif/"'s'+player[1]+".gif")

Card1_dealer=Label(image=Dealercard1,bg="green")
Card2_dealer=Label(image=Dealercard2,bg="green")
Card1_player=Label(image=Playercard1,bg="green")
Card2_player=Label(image=Playercard2,bg="green")

#




Welcome.grid(row=0,column=0,columnspan=3)
Dealer.grid(row=1,column=0)
Display_deal_sco.grid(row=1,column=1)
Player.grid(row=3,column=0)
Display_pl_sco.grid(row=3,column=1)

Card1_dealer.grid(row=2,column=0)
Card2_dealer.grid(row=2,column=1)
Card1_player.grid(row=4,column=0)
Card2_player.grid(row=4,column=1)

button_stand.grid(row=5,column=1)
button_hit.grid(row=5,column=0)
button_quit.grid(row=5,column=2)
Copyright.grid(row=10,column=0,columnspan=3)
   
if calc_hand(player) == 21:
    
    BlackJack1.grid(row=6,column=0,columnspan=3) 

root.mainloop()  
