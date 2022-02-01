#elo-script by Zakarea Yoosuf
#Purpose: create an algorithm which takes into account differences in score and previous elo when calculating the results of a game match

#Input the elo of both players, maximum difference of 500, can be modified by editing eloFactor
elo1=int(input("Player 1's elo:"))
elo2=int(input("Player 2's elo:"))

#takes integer values between 1 and 5
score1 = int(input("Player 1 Score"))
score2 = int(input("Player 2 Score"))
deltaWins = score1-score2

#Takes score into account, exponentially increasing the factor from a minimum of 1 to a maximum of 2 as the difference in score increases.
WIN_SCALAR = 1.489896102405 #Found by solving 5^x * .1 + .9 = 2
winFactor = .9 + ((abs(deltaWins) ** WIN_SCALAR) * .1) 

#eloFactor takes into account if the person with higher or lower elo won
#If the person with a higher elo won, then the score should be affected less
if (elo1-elo2) * deltaWins > 0:
    eloFactor = abs((0-abs(elo2-elo1) + 500))  
else:
    #If the person with a lower elo won, then the score should be affected more
    eloFactor = (abs(elo2-elo1) + 500)
    
#Calculates the total change in elo
ELO_CHANGE_CONSTANT = .192 #Affects the volatility of elo shifting
eloChange = winFactor * max(0, eloFactor) * ELO_CHANGE_CONSTANT  + 1 

#To incentivize players to challenge others, the winning player receives extra points (15 with the current configuration, hence the 78.125)
INCENTIVE_ELO = ELO_CHANGE_CONSTANT/78.125
if score1==5:
    elo1 += INCENTIVE_ELO + eloChange
    elo2 -= eloChange
else:
    elo2 += INCENTIVE_ELO + eloChange
    elo1 -= eloChange

#Displays the resulting elos for each player, can be replaced with a return statement
print("Player 1's new elo is " + str(int(round(elo1*10)/10)))
print("Player 2's new elo is " + str(int(round(elo2*10)/10)))
