#FIVE_IN_A_ROW.py
import time;
import math;
import random;
import tkinter;

def AI(MODE):
    #When AI is in COMPUTER mode, it focus on offense;
    #When AI is in PLAYER mode, it focus on defense;
    if MODE == COMPUTER:
        SELF = COMPUTER;
        OPPONENT = PLAYER;
    elif MODE == PLAYER:
        SELF = PLAYER;
        OPPONENT = COMPUTER;
    global TURN;
    
    #A boring part
    TIME = random.randint(2,4);
    canvas.itemconfig(INFO, text="Computer is thinking...", font=("Comic Sans MS", 20), fill="black");
    canvas.update();
    time.sleep(TIME/10.0);

    #Reset score object
    L5 = 0; L4 = 0; D4 = 0; L3 = 0; JL3 = 0; D3 = 0; L2 = 0; JL2 = 0; D2 = 0;
    for i in range(15):
        for j in range(15):
            if field[i][j] == 0:
                field[i][j] = MODE;
                #L5, HORIZONTAL
                if j<=len(field)-1 and j-4>=0:
                    if field[i][j-4] ==  SELF and field[i][j-3] == SELF and field[i][j-2] == SELF and field[i][j-1] == SELF and field[i][j] == SELF:
                        L5 += 1;
                if j+1<=len(field)-1 and j-3>=0:
                    if field[i][j-3] ==  SELF and field[i][j-2] == SELF and field[i][j-1] == SELF and field[i][j] == SELF and field[i][j+1] == SELF:
                        L5 += 1;
                if j+2<=len(field)-1 and j-2>=0:
                    if field[i][j-2] ==  SELF and field[i][j-1] == SELF and field[i][j] == SELF and field[i][j+1] == SELF and field[i][j+2] == SELF:
                        L5 += 1;
                if j+3<=len(field)-1 and j-1>=0:
                    if field[i][j-1] ==  SELF and field[i][j] == SELF and field[i][j+1] == SELF and field[i][j+2] == SELF and field[i][j+3] == SELF:
                        L5 += 1;
                if j+4<=len(field)-1 and j>=0:
                    if field[i][j] ==  SELF and field[i][j+1] == SELF and field[i][j+2] == SELF and field[i][j+3] == SELF and field[i][j+4] == SELF:
                        L5 += 1;
                #L5, PERPENDICULAR
                if i<=len(field)-1 and i-4>=0:
                    if field[i-4][j] ==  SELF and field[i-3][j] == SELF and field[i-2][j] == SELF and field[i-1][j] == SELF and field[i][j] == SELF:
                        L5 += 1;
                if i+1<=len(field)-1 and i-3>=0:
                    if field[i-3][j] ==  SELF and field[i-2][j] == SELF and field[i-1][j] == SELF and field[i][j] == SELF and field[i+1][j] == SELF:
                        L5 += 1;
                if i+2<=len(field)-1 and i-2>=0:
                    if field[i-2][j] ==  SELF and field[i-1][j] == SELF and field[i][j] == SELF and field[i+1][j] == SELF and field[i+2][j] == SELF:
                        L5 += 1;
                if i+3<=len(field)-1 and i-1>=0:
                    if field[i-1][j] ==  SELF and field[i][j] == SELF and field[i+1][j] == SELF and field[i+2][j] == SELF and field[i+3][j] == SELF:
                        L5 += 1;
                if i+4<=len(field)-1 and i>=0:
                    if field[i][j] ==  SELF and field[i+1][j] == SELF and field[i+2][j] == SELF and field[i+3][j] == SELF and field[i+4][j] == SELF:
                        L5 += 1;
                #L5, DECLINE
                if i+4<=len(field)-1 and i>=0 and j+4<=len(field)-1 and j>=0:
                    if field[i][j] == SELF and field[i+1][j+1] == SELF and field[i+2][j+2] == SELF and field[i+3][j+3] == SELF and field[i+4][j+4] == SELF:
                        L5 += 1;
                if i+3<=len(field)-1 and i-1>=0 and j+3<=len(field)-1 and j-1>=0:
                    if field[i-1][j-1] == SELF and field[i][j] == SELF and field[i+1][j+1] == SELF and field[i+2][j+2] == SELF and field[i+3][j+3] == SELF:
                        L5 += 1;
                if i+2<=len(field)-1 and i-2>=0 and j+2<=len(field)-1 and j-2>=0:
                    if field[i-2][j-2] == SELF and field[i-1][j-1] == SELF and field[i][j] == SELF and field[i+1][j+1] == SELF and field[i+2][j+2] == SELF:
                        L5 += 1;
                if i+1<=len(field)-1 and i-3>=0 and j+1<=len(field)-1 and j-3>=0:
                    if field[i-3][j-3] == SELF and field[i-2][j-2] == SELF and field[i-1][j-1] == SELF and field[i][j] == SELF and field[i+1][j+1] == SELF:
                        L5 += 1;
                if i<=len(field)-1 and i-4>=0 and j<=len(field)-1 and j-4>=0:
                    if field[i-4][j-4] == SELF and field[i-3][j-3] == SELF and field[i-2][j-2] == SELF and field[i-1][j-1] == SELF and field[i][j] == SELF:
                        L5 += 1;
                #L5, RISE
                if i+4<=len(field)-1 and i>=0 and j<=len(field)-1 and j-4>=0:
                    if field[i][j] == SELF and field[i+1][j-1] == SELF and field[i+2][j-2] == SELF and field[i+3][j-3] == SELF and field[i+4][j-4] == SELF:
                        L5 += 1;
                if i+3<=len(field)-1 and i-1>=0 and j+1<=len(field)-1 and j-3>=0:
                    if field[i-1][j+1] == SELF and field[i][j] == SELF and field[i+1][j-1] == SELF and field[i+2][j-2] == SELF and field[i+3][j-3] == SELF:
                        L5 += 1;
                if i+2<=len(field)-1 and i-2>=0 and j+2<=len(field)-1 and j-2>=0:
                    if field[i-2][j+2] == SELF and field[i-1][j-1] == SELF and field[i][j] == SELF and field[i+1][j-1] == SELF and field[i+2][j-2] == SELF:
                        L5 += 1;
                if i+1<=len(field)-1 and i-3>=0 and j+3<=len(field)-1 and j-1>=0:
                    if field[i-3][j+3] == SELF and field[i-2][j+2] == SELF and field[i-1][j+1] == SELF and field[i][j] == SELF and field[i+1][j-1] == SELF:
                        L5 += 1;
                if i<=len(field)-1 and i-4>=0 and j+4<=len(field)-1 and j>=0:
                    if field[i-4][j+4] == SELF and field[i-3][j+3] == SELF and field[i-2][j+2] == SELF and field[i-1][j+1] == SELF and field[i][j] == SELF:
                        L5 += 1;

                if L5 == 0:     
                    #L4, HORIZONTAL
                    if j+1<=len(field)-1 and j-4>=0:
                        if field[i][j-4] == 0 and field[i][j-3] == SELF and field[i][j-2] == SELF and field[i][j-1] == SELF and field[i][j] == SELF and field[i][j+1] == 0:
                            L4 += 1;
                    if j+2<=len(field)-1 and j-3>=0:
                        if field[i][j-3] == 0 and field[i][j-2] == SELF and field[i][j-1] == SELF and field[i][j] == SELF and field[i][j+1] == SELF and field[i][j+2] == 0:
                            L4 += 1;
                    if j+3<=len(field)-1 and j-2>=0:
                        if field[i][j-2] == 0 and field[i][j-1] == SELF and field[i][j] == SELF and field[i][j+1] == SELF and field[i][j+2] == SELF and field[i][j+3] == 0:
                            L4 += 1;
                    if j+4<=len(field)-1 and j-1>=0:
                        if field[i][j-1] == 0 and field[i][j] == SELF and field[i][j+1] == SELF and field[i][j+2] == SELF and field[i][j+3] == SELF and field[i][j+4] == 0:
                            L4 += 1;
                    #L4, PERPENDICULAR
                    if i+1<=len(field)-1 and i-4>=0:
                        if field[i-4][j] == 0 and field[i-3][j] == SELF and field[i-2][j] == SELF and field[i-1][j] == SELF and field[i][j] == SELF and field[i+1][j] == 0:
                            L4 += 1;
                    if i+2<=len(field)-1 and i-3>=0:
                        if field[i-3][j] == 0 and field[i-2][j] == SELF and field[i-1][j] == SELF and field[i][j] == SELF and field[i+1][j] == SELF and field[i+2][j] == 0:
                            L4 += 1;
                    if i+3<=len(field)-1 and i-2>=0:
                        if field[i-2][j] == 0 and field[i-1][j] == SELF and field[i][j] == SELF and field[i+1][j] == SELF and field[i+2][j] == SELF and field[i+3][j] == 0:
                            L4 += 1;
                    if i+4<=len(field)-1 and i-1>=0:
                        if field[i-1][j] == 0 and field[i][j] == SELF and field[i+1][j] == SELF and field[i+2][j] == SELF and field[i+3][j] == SELF and field[i+4][j] == 0:
                            L4 += 1;
                    #L4, DECLINE
                    if i+4<=len(field)-1 and i-1>=0 and j+4<=len(field)-1 and j-1>=0:
                        if field[i-1][j-1] == 0 and field[i][j] ==  SELF and field[i+1][j+1] == SELF and field[i+2][j+2] == SELF and field[i+3][j+3] == SELF and field[i+4][j+4] == 0:
                            L4 += 1;
                    if i+3<=len(field)-1 and i-2>=0 and j+3<=len(field)-1 and j-2>=0:
                        if field[i-2][j-2] == 0 and field[i-1][j-1] == SELF and field[i][j] == SELF and field[i+1][j+1] == SELF and field[i+2][j+2] == SELF and field[i+3][j+3] == 0:
                            L4 += 1;
                    if i+2<=len(field)-1 and i-3>=0 and j+2<=len(field)-1 and j-3>=0:
                        if field[i-3][j-3] == 0 and field[i-2][j-2] == SELF and field[i-1][j-1] == SELF and field[i][j] == SELF and field[i+1][j+1] == SELF and field[i+2][j+2] == 0:
                            L4 += 1;
                    if i+1<=len(field)-1 and i-4>=0 and j+1<=len(field)-1 and j-4>=0:
                        if field[i-4][j-4] == 0 and field[i-3][j-3] == SELF and field[i-2][j-2] == SELF and field[i-1][j-1] == SELF and field[i][j] == SELF and field[i+1][j+1] == 0:
                            L4 += 1;
                    #L4, RISE
                    if i+4<=len(field)-1 and i-1>=0 and j+1<=len(field)-1 and j-4>=0:
                        if field[i-1][j+1] == 0 and field[i][j] ==  SELF and field[i+1][j-1] == SELF and field[i+2][j-2] == SELF and field[i+3][j-3] == SELF and field[i+4][j-4] == 0:
                            L4 += 1;
                    if i+3<=len(field)-1 and i-2>=0 and j+2<=len(field)-1 and j-3>=0:
                        if field[i-2][j+2] == 0 and field[i-1][j+1] ==  SELF and field[i][j] == SELF and field[i+1][j-1] == SELF and field[i+2][j-2] == SELF and field[i+3][j-3] == 0:
                            L4 += 1;
                    if i+2<=len(field)-1 and i-3>=0 and j+3<=len(field)-1 and j-2>=0:
                        if field[i-3][j+3] == 0 and field[i-2][j+2] ==  SELF and field[i-1][j+1] == SELF and field[i][j] == SELF and field[i+1][j-1] == SELF and field[i+2][j-2] == 0:
                            L4 += 1;
                    if i+1<=len(field)-1 and i-4>=0 and j+4<=len(field)-1 and j-1>=0:
                        if field[i-4][j+4] == 0 and field[i-3][j+3] ==  SELF and field[i-2][j+2] == SELF and field[i-1][j+1] == SELF and field[i][j] == SELF and field[i+1][j-1] == 0:
                            L4 += 1;
                    
                    #D4, HORIZONTAL
                    if j<=len(field)-1 and j-5>=0:
                        if (field[i][j-4] ==  SELF and field[i][j-3] == SELF and field[i][j-2] == SELF and field[i][j-1] == SELF and field[i][j] == OPPONENT) != \
                           (field[i][j-4] ==  SELF and field[i][j-3] == SELF and field[i][j-2] == SELF and field[i][j-1] == SELF and field[i][j-5] == OPPONENT):
                            D4 += 1;
                    if j+1<=len(field)-1 and j-4>=0:
                        if (field[i][j-3] ==  SELF and field[i][j-2] == SELF and field[i][j-1] == SELF and field[i][j] == SELF and field[i][j+1] == OPPONENT) != \
                           (field[i][j-3] ==  SELF and field[i][j-2] == SELF and field[i][j-1] == SELF and field[i][j] == SELF and field[i][j-4] == OPPONENT):
                            D4 += 1;
                    if j+2<=len(field)-1 and j-3>=0:
                        if (field[i][j-2] ==  SELF and field[i][j-1] == SELF and field[i][j] == SELF and field[i][j+1] == SELF and field[i][j+2] == OPPONENT) != \
                           (field[i][j-2] ==  SELF and field[i][j-1] == SELF and field[i][j] == SELF and field[i][j+1] == SELF and field[i][j-3] == OPPONENT):
                            D4 += 1;
                    if j+3<=len(field)-1 and j-2>=0:
                        if (field[i][j-1] ==  SELF and field[i][j] == SELF and field[i][j+1] == SELF and field[i][j+2] == SELF and field[i][j+3] == OPPONENT) != \
                           (field[i][j-1] ==  SELF and field[i][j] == SELF and field[i][j+1] == SELF and field[i][j+2] == SELF and field[i][j-2] == OPPONENT):
                            D4 += 1;
                    if j+4<=len(field)-1 and j-1>=0:
                        if (field[i][j] ==  SELF and field[i][j+1] == SELF and field[i][j+2] == SELF and field[i][j+3] == SELF and field[i][j+4] == OPPONENT) != \
                           (field[i][j] ==  SELF and field[i][j+1] == SELF and field[i][j+2] == SELF and field[i][j+3] == SELF and field[i][j-1] == OPPONENT):
                            D4 += 1;
                    if j+5<=len(field)-1 and j>=0:
                        if (field[i][j+1] ==  SELF and field[i][j+2] == SELF and field[i][j+3] == SELF and field[i][j+4] == SELF and field[i][j+5] == OPPONENT) != \
                           (field[i][j+1] ==  SELF and field[i][j+2] == SELF and field[i][j+3] == SELF and field[i][j+4] == SELF and field[i][j] == OPPONENT):
                            D4 += 1;
                    #D4, PERPENDICULAR
                    if i<=len(field)-1 and i-5>=0:
                        if (field[i-4][j] == SELF and field[i-3][j] == SELF and field[i-2][j] == SELF and field[i-1][j] == SELF and field[i][j] == OPPONENT) != \
                           (field[i-4][j] == SELF and field[i-3][j] == SELF and field[i-2][j] == SELF and field[i-1][j] == SELF and field[i-5][j] == OPPONENT):
                            D4 += 1;
                    if i+1<=len(field)-1 and i-4>=0:
                        if (field[i-3][j] ==  SELF and field[i-2][j] == SELF and field[i-1][j] == SELF and field[i][j] == SELF and field[i+1][j] == OPPONENT) != \
                           (field[i-3][j] ==  SELF and field[i-2][j] == SELF and field[i-1][j] == SELF and field[i][j] == SELF and field[i-4][j] == OPPONENT):
                            D4 += 1;
                    if i+2<=len(field)-1 and i-3>=0:
                        if (field[i-2][j] ==  SELF and field[i-1][j] == SELF and field[i][j] == SELF and field[i+1][j] == SELF and field[i+2][j] == OPPONENT) != \
                           (field[i-2][j] ==  SELF and field[i-1][j] == SELF and field[i][j] == SELF and field[i+1][j] == SELF and field[i-3][j] == OPPONENT):
                            D4 += 1;
                    if i+3<=len(field)-1 and i-2>=0:
                        if (field[i-1][j] ==  SELF and field[i][j] == SELF and field[i+1][j] == SELF and field[i+2][j] == SELF and field[i+3][j] == OPPONENT) != \
                           (field[i-1][j] ==  SELF and field[i][j] == SELF and field[i+1][j] == SELF and field[i+2][j] == SELF and field[i-2][j] == OPPONENT):
                            D4 += 1;
                    if i+4<=len(field)-1 and i-1>=0:
                        if (field[i][j] ==  SELF and field[i+1][j] == SELF and field[i+2][j] == SELF and field[i+3][j] == SELF and field[i+4][j] == OPPONENT) != \
                           (field[i][j] ==  SELF and field[i+1][j] == SELF and field[i+2][j] == SELF and field[i+3][j] == SELF and field[i-1][j] == OPPONENT):
                            D4 += 1;
                    if i+5<=len(field)-1 and i>=0:
                        if (field[i+1][j] ==  SELF and field[i+2][j] == SELF and field[i+3][j] == SELF and field[i+4][j] == SELF and field[i+5][j] == OPPONENT) != \
                           (field[i+1][j] ==  SELF and field[i+2][j] == SELF and field[i+3][j] == SELF and field[i+4][j] == SELF and field[i][j] == OPPONENT):
                            D4 += 1;
                    #D4, DECLINE
                    if i+5<=len(field)-1 and i>=0 and j+5<=len(field)-1 and j>=0:
                        if (field[i+1][j+1] ==  SELF and field[i+2][j+2] == SELF and field[i+3][j+3] == SELF and field[i+4][j+4] == SELF and field[i+5][j+5] == OPPONENT) != \
                           (field[i+1][j+1] ==  SELF and field[i+2][j+2] == SELF and field[i+3][j+3] == SELF and field[i+4][j+4] == SELF and field[i][j] == OPPONENT):
                            D4 += 1;
                    if i+4<=len(field)-1 and i-1>=0 and j+4<=len(field)-1 and j-1>=0:
                        if (field[i][j] ==  SELF and field[i+1][j+1] == SELF and field[i+2][j+2] == SELF and field[i+3][j+3] == SELF and field[i+4][j+4] == OPPONENT) != \
                           (field[i][j] ==  SELF and field[i+1][j+1] == SELF and field[i+2][j+2] == SELF and field[i+3][j+3] == SELF and field[i-1][j-1] == OPPONENT):
                            D4 += 1;
                    if i+3<=len(field)-1 and i-2>=0 and j+3<=len(field)-1 and j-2>=0:
                        if (field[i-1][j-1] == SELF and field[i][j] == SELF and field[i+1][j+1] == SELF and field[i+2][j+2] == SELF and field[i+3][j+3] == OPPONENT) != \
                           (field[i-1][j-1] == SELF and field[i][j] == SELF and field[i+1][j+1] == SELF and field[i+2][j+2] == SELF and field[i-2][j-2] == OPPONENT):
                            D4 += 1;
                    if i+2<=len(field)-1 and i-3>=0 and j+2<=len(field)-1 and j-3>=0:
                        if (field[i-2][j-2] == SELF and field[i-1][j-1] == SELF and field[i][j] == SELF and field[i+1][j+1] == SELF and field[i+2][j+2] == OPPONENT) != \
                           (field[i-2][j-2] == SELF and field[i-1][j-1] == SELF and field[i][j] == SELF and field[i+1][j+1] == SELF and field[i-3][j-3] == OPPONENT):
                            D4 += 1;
                    if i+1<=len(field)-1 and i-4>=0 and j+1<=len(field)-1 and j-4>=0:
                        if (field[i-3][j-3] == SELF and field[i-2][j-2] == SELF and field[i-1][j-1] == SELF and field[i][j] == SELF and field[i+1][j+1] == OPPONENT) != \
                           (field[i-3][j-3] == SELF and field[i-2][j-2] == SELF and field[i-1][j-1] == SELF and field[i][j] == SELF and field[i-4][j-4] == OPPONENT):
                            D4 += 1;
                    if i<=len(field)-1 and i-5>=0 and j<=len(field)-1 and j-5>=0:
                        if (field[i-4][j-4] == SELF and field[i-3][j-3] == SELF and field[i-2][j-2] == SELF and field[i-1][j-1] == SELF and field[i][j] == OPPONENT) != \
                           (field[i-4][j-4] == SELF and field[i-3][j-3] == SELF and field[i-2][j-2] == SELF and field[i-1][j-1] == SELF and field[i-5][j-5] == OPPONENT):
                            D4 += 1;
                    #D4, RISE
                    if i+5<=len(field)-1 and i>=0 and j<=len(field)-1 and j-5>=0:
                        if (field[i+1][j-1] ==  SELF and field[i+2][j-2] == SELF and field[i+3][j-3] == SELF and field[i+4][j-4] == SELF and field[i+5][j-5] == OPPONENT) != \
                           (field[i+1][j-1] ==  SELF and field[i+2][j-2] == SELF and field[i+3][j-3] == SELF and field[i+4][j-4] == SELF and field[i][j] == OPPONENT):
                            D4 += 1;
                    if i+4<=len(field)-1 and i-1>=0 and j+1<=len(field)-1 and j-4>=0:
                        if (field[i][j] ==  SELF and field[i+1][j-1] == SELF and field[i+2][j-2] == SELF and field[i+3][j-3] == SELF and field[i+4][j-4] == OPPONENT) != \
                           (field[i][j] ==  SELF and field[i+1][j-1] == SELF and field[i+2][j-2] == SELF and field[i+3][j-3] == SELF and field[i-1][j+1] == OPPONENT):
                            D4 += 1;
                    if i+3<=len(field)-1 and i-2>=0 and j+2<=len(field)-1 and j-3>=0:
                        if (field[i-1][j+1] ==  SELF and field[i][j] == SELF and field[i+1][j-1] == SELF and field[i+2][j-2] == SELF and field[i+3][j-3] == OPPONENT) != \
                           (field[i-1][j+1] ==  SELF and field[i][j] == SELF and field[i+1][j-1] == SELF and field[i+2][j-2] == SELF and field[i-2][j+2] == OPPONENT):
                            D4 += 1;
                    if i+2<=len(field)-1 and i-3>=0 and j+3<=len(field)-1 and j-2>=0:
                        if (field[i-2][j+2] ==  SELF and field[i-1][j+1] == SELF and field[i][j] == SELF and field[i+1][j-1] == SELF and field[i+2][j-2] == OPPONENT) != \
                           (field[i-2][j+2] ==  SELF and field[i-1][j+1] == SELF and field[i][j] == SELF and field[i+1][j-1] == SELF and field[i-3][j+3] == OPPONENT):
                            D4 += 1;
                    if i+1<=len(field)-1 and i-4>=0 and j+4<=len(field)-1 and j-1>=0:
                        if (field[i-3][j+3] ==  SELF and field[i-2][j+2] == SELF and field[i-1][j+1] == SELF and field[i][j] == SELF and field[i+1][j-1] == OPPONENT) != \
                           (field[i-3][j+3] ==  SELF and field[i-2][j+2] == SELF and field[i-1][j+1] == SELF and field[i][j] == SELF and field[i-4][j+4] == OPPONENT):
                            D4 += 1;
                    if i<=len(field)-1 and i-5>=0 and j+5<=len(field)-1 and j>=0:
                        if (field[i-4][j+4] ==  SELF and field[i-3][j+3] == SELF and field[i-2][j+2] == SELF and field[i-1][j+1] == SELF and field[i][j] == OPPONENT) != \
                           (field[i-4][j+4] ==  SELF and field[i-3][j+3] == SELF and field[i-2][j+2] == SELF and field[i-1][j+1] == SELF and field[i-5][j+5] == OPPONENT):
                            D4 += 1;

                    #L3, HORIZONTAL
                    if j+1<=len(field)-1 and j-3>=0:
                        if field[i][j-3] == 0 and field[i][j-2] == SELF and field[i][j-1] == SELF and field[i][j] == SELF and field[i][j+1] == 0:
                            L3 += 1;
                    if j+2<=len(field)-1 and j-2>=0:
                        if field[i][j-2] == 0 and field[i][j-1] == SELF and field[i][j] == SELF and field[i][j+1] == SELF and field[i][j+2] == 0:
                            L3 += 1;
                    if j+3<=len(field)-1 and j-1>=0:
                        if field[i][j-1] == 0 and field[i][j] == SELF and field[i][j+1] == SELF and field[i][j+2] == SELF and field[i][j+3] == 0:
                            L3 += 1;
                    #L3, PERPENDICULAR
                    if i+1<=len(field)-1 and i-3>=0:
                        if field[i-3][j] == 0 and field[i-2][j] == SELF and field[i-1][j] == SELF and field[i][j] == SELF and field[i+1][j] == 0:
                            L3 += 1;
                    if i+2<=len(field)-1 and i-2>=0:
                        if field[i-2][j] == 0 and field[i-1][j] == SELF and field[i][j] == SELF and field[i+1][j] == SELF and field[i+2][j] == 0:
                            L3 += 1;
                    if i+3<=len(field)-1 and i-1>=0:
                        if field[i-1][j] == 0 and field[i][j] == SELF and field[i+1][j] == SELF and field[i+2][j] == SELF and field[i+3][j] == 0:
                            L3 += 1;
                    #L3, DECLINE
                    if i+3<=len(field)-1 and i-1>=0 and j+3<=len(field)-1 and j-1>=0:
                        if field[i-1][j-1] == 0 and field[i][j] == SELF and field[i+1][j+1] == SELF and field[i+2][j+2] == SELF and field[i+3][j+3] == 0:
                            L3 += 1;
                    if i+2<=len(field)-1 and i-2>=0 and j+2<=len(field)-1 and j-2>=0:
                        if field[i-2][j-2] == 0 and field[i-1][j-1] == SELF and field[i][j] == SELF and field[i+1][j+1] == SELF and field[i+2][j+2] == 0:
                            L3 += 1;
                    if i+1<=len(field)-1 and i-3>=0 and j+1<=len(field)-1 and j-3>=0:
                        if field[i-3][j-3] == 0 and field[i-2][j-2] == SELF and field[i-1][j-1] == SELF and field[i][j] == SELF and field[i+1][j+1] == 0:
                            L3 += 1;
                    #L3, RISE
                    if i+4<=len(field)-1 and i-1>=0 and j+1<=len(field)-1 and j-4>=0:
                        if field[i-1][j+1] == 0 and field[i][j] ==  SELF and field[i+1][j-1] == SELF and field[i+2][j-2] == SELF and field[i+3][j-3] == 0:
                            L3 += 1;
                    if i+3<=len(field)-1 and i-2>=0 and j+2<=len(field)-1 and j-3>=0:
                        if field[i-2][j+2] == 0 and field[i-1][j+1] ==  SELF and field[i][j] == SELF and field[i+1][j-1] == SELF and field[i+2][j-2] == 0:
                            L3 += 1;
                    if i+2<=len(field)-1 and i-3>=0 and j+3<=len(field)-1 and j-2>=0:
                        if field[i-3][j+3] == 0 and field[i-2][j+2] ==  SELF and field[i-1][j+1] == SELF and field[i][j] == SELF and field[i+1][j-1] == 0:
                            L3 += 1;
                            
                    #L3, HORIZONTAL, JUMPING
                    if j+1<=len(field)-1 and j-4>=0:
                        if field[i][j-4] == 0 and field[i][j-3] == SELF and field[i][j-2] == 0 and field[i][j-1] == SELF and field[i][j] == SELF and field[i][j+1] == 0:
                            JL3 += 1;
                    if j+1<=len(field)-1 and j-4>=0:
                        if field[i][j-4] == 0 and field[i][j-3] == SELF and field[i][j-2] == SELF and field[i][j-1] == 0 and field[i][j] == SELF and field[i][j+1] == 0:
                            JL3 += 1;
                    if j+4<=len(field)-1 and j-1>=0:
                        if field[i][j-1] == 0 and field[i][j] == SELF and field[i][j+1] == 0 and field[i][j+2] == SELF and field[i][j+3] == SELF and field[i][j+4] == 0:
                            JL3 += 1;
                    if j+4<=len(field)-1 and j-1>=0:
                        if field[i][j-1] == 0 and field[i][j] == SELF and field[i][j+1] == SELF and field[i][j+2] == 0 and field[i][j+3] == SELF and field[i][j+4] == 0:
                            JL3 += 1;
                    if j+2<=len(field)-1 and j-3>=0:
                        if field[i][j-3] == 0 and field[i][j-2] == SELF and field[i][j-1] == 0 and field[i][j] == SELF and field[i][j+1] == SELF and field[i][j+2] == 0:
                            JL3 += 1;
                    if j+3<=len(field)-1 and j-2>=0:
                        if field[i][j-2] == 0 and field[i][j-1] == SELF and field[i][j] == SELF and field[i][j+1] == 0 and field[i][j+2] == SELF and field[i][j+3] == 0:
                            JL3 += 1;
                    #L3, PERPENDICULAR, JUMPING
                    if i+1<=len(field)-1 and i-4>=0:
                        if field[i-4][j] == 0 and field[i-3][j] == SELF and field[i-2][j] == 0 and field[i-1][j] == SELF and field[i][j] == SELF and field[i+1][j] == 0:
                            JL3 += 1;
                    if i+1<=len(field)-1 and i-4>=0:
                        if field[i-4][j] == 0 and field[i-3][j] == SELF and field[i-2][j] == SELF and field[i-1][j] == 0 and field[i][j] == SELF and field[i+1][j] == 0:
                            JL3 += 1;
                    if i+4<=len(field)-1 and i-1>=0:
                        if field[i-1][j] == 0 and field[i][j] == SELF and field[i+1][j] == 0 and field[i+2][j] == SELF and field[i+3][j] == SELF and field[i+4][j] == 0:
                            JL3 += 1;
                    if i+4<=len(field)-1 and i-1>=0:
                        if field[i-1][j] == 0 and field[i][j] == SELF and field[i+1][j] == SELF and field[i+2][j] == 0 and field[i+3][j] == SELF and field[i+4][j] == 0:
                            JL3 += 1;
                    if i+2<=len(field)-1 and i-3>=0:
                        if field[i-3][j] == 0 and field[i-2][j] == SELF and field[i-1][j] == 0 and field[i][j] == SELF and field[i+1][j] == SELF and field[i+2][j] == 0:
                            JL3 += 1;
                    if i+3<=len(field)-1 and i-2>=0:
                        if field[i-2][j] == 0 and field[i-1][j] == SELF and field[i][j] == SELF and field[i+1][j] == 0 and field[i+2][j] == SELF and field[i+3][j] == 0:
                            JL3 += 1;
                    #L3, DECLINE, JUMPING
                    if i+4<=len(field)-1 and i-1>=0 and j+4<=len(field)-1 and j-1>=0:
                        if field[i-1][j-1] == 0 and field[i][j] == SELF and field[i+1][j+1] == 0 and field[i+2][j+2] == SELF and field[i+3][j+3] == SELF and field[i+4][j+4] == 0:
                            JL3 += 1;
                    if i+4<=len(field)-1 and i-1>=0 and j+4<=len(field)-1 and j-1>=0:
                        if field[i-1][j-1] == 0 and field[i][j] == SELF and field[i+1][j+1] == SELF and field[i+2][j+2] == 0 and field[i+3][j+3] == SELF and field[i+4][j+4] == 0:
                            JL3 += 1;
                    if i+1<=len(field)-1 and i-4>=0 and j+1<=len(field)-1 and j-4>=0:
                        if field[i-4][j-4] == 0 and field[i-3][j-3] == SELF and field[i-2][j-2] == 0 and field[i-1][j-1] == SELF and field[i][j] == SELF and field[i+1][j+1] == 0:
                            JL3 += 1;
                    if i+1<=len(field)-1 and i-4>=0 and j+1<=len(field)-1 and j-4>=0:
                        if field[i-4][j-4] == 0 and field[i-3][j-3] == SELF and field[i-2][j-2] == SELF and field[i-1][j-1] == 0 and field[i][j] == SELF and field[i+1][j+1] == 0:
                            JL3 += 1;
                    if i+2<=len(field)-1 and i-3>=0 and j+2<=len(field)-1 and j-3>=0:
                        if field[i-3][j-3] == 0 and field[i-2][j-2] == SELF and field[i-1][j-1] == 0 and field[i][j] == SELF and field[i+1][j+1] == SELF and field[i+2][j+2] == 0:
                            JL3 += 1;
                    if i+3<=len(field)-1 and i-2>=0 and j+3<=len(field)-1 and j-2>=0:
                        if field[i-2][j-2] == 0 and field[i-1][j-1] == SELF and field[i][j] == SELF and field[i+1][j+1] == 0 and field[i+2][j+2] == SELF and field[i+3][j+3] == 0:
                            JL3 += 1;
                    #L3, RISE, JUMPING
                    if i+4<=len(field)-1 and i-1>=0 and j+1<=len(field)-1 and j-4>=0:
                        if field[i-1][j+1] == 0 and field[i][j] ==  SELF and field[i+1][j-1] == 0 and field[i+2][j-2] == SELF and field[i+3][j-3] == SELF and field[i+4][j-4] == 0:
                            JL3 += 1;
                    if i+4<=len(field)-1 and i-1>=0 and j+1<=len(field)-1 and j-4>=0:
                        if field[i-1][j+1] == 0 and field[i][j] ==  SELF and field[i+1][j-1] == SELF and field[i+2][j-2] == 0 and field[i+3][j-3] == SELF and field[i+4][j-4] == 0:
                            JL3 += 1;
                    if i+1<=len(field)-1 and i-4>=0 and j+4<=len(field)-1 and j-1>=0:
                        if field[i-4][j+4] == 0 and field[i-3][j+3] ==  SELF and field[i-2][j+2] == 0 and field[i-1][j+1] == SELF and field[i][j] == SELF and field[i+1][j-1] == 0:
                            JL3 += 1;
                    if i+1<=len(field)-1 and i-4>=0 and j+4<=len(field)-1 and j-1>=0:
                        if field[i-4][j+4] == 0 and field[i-3][j+3] ==  SELF and field[i-2][j+2] == SELF and field[i-1][j+1] == 0 and field[i][j] == SELF and field[i+1][j-1] == 0:
                            JL3 += 1;
                    if i+2<=len(field)-1 and i-3>=0 and j+3<=len(field)-1 and j-2>=0:
                        if field[i-3][j+3] == 0 and field[i-2][j+2] ==  SELF and field[i-1][j+1] == 0 and field[i][j] == SELF and field[i+1][j-1] == SELF and field[i+2][j-2] == 0:
                            JL3 += 1;
                    if i+3<=len(field)-1 and i-2>=0 and j+2<=len(field)-1 and j-3>=0:
                        if field[i-2][j+2] == 0 and field[i-1][j+1] ==  SELF and field[i][j] == SELF and field[i+1][j-1] == 0 and field[i+2][j-2] == SELF and field[i+3][j-3] == 0:
                            JL3 += 1;
                    
                    #D3, HORIZONTAL
                    if j<=len(field)-1 and j-4>=0:
                        if (field[i][j-3] == SELF and field[i][j-2] == SELF and field[i][j-1] == SELF and field[i][j] == OPPONENT) != \
                           (field[i][j-3] == SELF and field[i][j-2] == SELF and field[i][j-1] == SELF and field[i][j-4] == OPPONENT):
                            D3 += 1;
                    if j+1<=len(field)-1 and j-3>=0:
                        if (field[i][j-2] == SELF and field[i][j-1] == SELF and field[i][j] == SELF and field[i][j+1] == OPPONENT) != \
                           (field[i][j-2] == SELF and field[i][j-1] == SELF and field[i][j] == SELF and field[i][j-3] == OPPONENT):
                            D3 += 1;
                    if j+2<=len(field)-1 and j-2>=0:
                        if (field[i][j-1] == SELF and field[i][j] == SELF and field[i][j+1] == SELF and field[i][j+2] == OPPONENT) != \
                           (field[i][j-1] == SELF and field[i][j] == SELF and field[i][j+1] == SELF and field[i][j-2] == OPPONENT):
                            D3 += 1;
                    if j+3<=len(field)-1 and j-1>=0:
                        if (field[i][j] == SELF and field[i][j+1] == SELF and field[i][j+2] == SELF and field[i][j+3] == OPPONENT) != \
                           (field[i][j] == SELF and field[i][j+1] == SELF and field[i][j+2] == SELF and field[i][j-1] == OPPONENT):
                            D3 += 1;
                    if j+4<=len(field)-1 and j>=0:
                        if (field[i][j+1] == SELF and field[i][j+2] == SELF and field[i][j+3] == SELF and field[i][j+4] == OPPONENT) != \
                           (field[i][j+1] == SELF and field[i][j+2] == SELF and field[i][j+3] == SELF and field[i][j] == OPPONENT):
                            D3 += 1;
                    #D3, PERPENDICULAR
                    if i<=len(field)-1 and i-4>=0:
                        if (field[i-3][j] == SELF and field[i-2][j] == SELF and field[i-1][j] == SELF and field[i][j] == OPPONENT) != \
                           (field[i-3][j] == SELF and field[i-2][j] == SELF and field[i-1][j] == SELF and field[i-4][j] == OPPONENT):
                            D3 += 1;
                    if i+1<=len(field)-1 and i-3>=0:
                        if (field[i-2][j] == SELF and field[i-1][j] == SELF and field[i][j] == SELF and field[i+1][j] == OPPONENT) != \
                           (field[i-2][j] == SELF and field[i-1][j] == SELF and field[i][j] == SELF and field[i-3][j] == OPPONENT):
                            D3 += 1;
                    if i+2<=len(field)-1 and i-2>=0:
                        if (field[i-1][j] == SELF and field[i][j] == SELF and field[i+1][j] == SELF and field[i+2][j] == OPPONENT) != \
                           (field[i-1][j] == SELF and field[i][j] == SELF and field[i+1][j] == SELF and field[i-2][j] == OPPONENT):
                            D3 += 1;
                    if i+3<=len(field)-1 and i-1>=0:
                        if (field[i][j] == SELF and field[i+1][j] == SELF and field[i+2][j] == SELF and field[i+3][j] == OPPONENT) != \
                           (field[i][j] == SELF and field[i+1][j] == SELF and field[i+2][j] == SELF and field[i-1][j] == OPPONENT):
                            D3 += 1;
                    if i+4<=len(field)-1 and i>=0:
                        if (field[i+1][j] == SELF and field[i+2][j] == SELF and field[i+3][j] == SELF and field[i+4][j] == OPPONENT) != \
                           (field[i+1][j] == SELF and field[i+2][j] == SELF and field[i+3][j] == SELF and field[i][j] == OPPONENT):
                            D3 += 1;
                    #D3, DECLINE
                    if i+4<=len(field)-1 and i>=0 and j+4<=len(field)-1 and j>=0:
                        if (field[i+1][j+1] ==  SELF and field[i+2][j+2] == SELF and field[i+3][j+3] == SELF and field[i+4][j+4] == OPPONENT) != \
                           (field[i+1][j+1] ==  SELF and field[i+2][j+2] == SELF and field[i+3][j+3] == SELF and field[i][j] == OPPONENT):
                            D3 += 1;
                    if i+3<=len(field)-1 and i-1>=0 and j+3<=len(field)-1 and j-1>=0:
                        if (field[i][j] ==  SELF and field[i+1][j+1] == SELF and field[i+2][j+2] == SELF and field[i+3][j+3] == OPPONENT) != \
                           (field[i][j] ==  SELF and field[i+1][j+1] == SELF and field[i+2][j+2] == SELF and field[i-1][j-1] == OPPONENT):
                            D3 += 1;
                    if i+2<=len(field)-1 and i-2>=0 and j+2<=len(field)-1 and j-2>=0:
                        if (field[i-1][j-1] == SELF and field[i][j] == SELF and field[i+1][j+1] == SELF and field[i+2][j+2] == OPPONENT) != \
                           (field[i-1][j-1] == SELF and field[i][j] == SELF and field[i+1][j+1] == SELF and field[i-2][j-2] == OPPONENT):
                            D3 += 1;
                    if i+1<=len(field)-1 and i-3>=0 and j+1<=len(field)-1 and j-3>=0:
                        if (field[i-2][j-2] == SELF and field[i-1][j-1] == SELF and field[i][j] == SELF and field[i+1][j+1] == OPPONENT) != \
                           (field[i-2][j-2] == SELF and field[i-1][j-1] == SELF and field[i][j] == SELF and field[i-3][j-3] == OPPONENT):
                            D3 += 1;
                    if i<=len(field)-1 and i-4>=0 and j<=len(field)-1 and j-4>=0:
                        if (field[i-3][j-3] == SELF and field[i-2][j-2] == SELF and field[i-1][j-1] == SELF and field[i][j] == OPPONENT) != \
                           (field[i-3][j-3] == SELF and field[i-2][j-2] == SELF and field[i-1][j-1] == SELF and field[i-4][j-4] == OPPONENT):
                            D3 += 1;
                    #D3, RISE
                    if i+4<=len(field)-1 and i>=0 and j<=len(field)-1 and j-4>=0:
                        if (field[i+1][j-1] ==  SELF and field[i+2][j-2] == SELF and field[i+3][j-3] == SELF and field[i+4][j-4] == OPPONENT) != \
                           (field[i+1][j-1] ==  SELF and field[i+2][j-2] == SELF and field[i+3][j-3] == SELF and field[i][j] == OPPONENT):
                            D3 += 1;
                    if i+3<=len(field)-1 and i-1>=0 and j+1<=len(field)-1 and j-3>=0:
                        if (field[i][j] ==  SELF and field[i+1][j-1] == SELF and field[i+2][j-2] == SELF and field[i+3][j-3] == OPPONENT) != \
                           (field[i][j] ==  SELF and field[i+1][j-1] == SELF and field[i+2][j-2] == SELF and field[i-1][j+1] == OPPONENT):
                            D3 += 1;
                    if i+2<=len(field)-1 and i-2>=0 and j+2<=len(field)-1 and j-2>=0:
                        if (field[i-1][j+1] ==  SELF and field[i][j] == SELF and field[i+1][j-1] == SELF and field[i+2][j-2] == OPPONENT) != \
                           (field[i-1][j+1] ==  SELF and field[i][j] == SELF and field[i+1][j-1] == SELF and field[i-2][j+2] == OPPONENT):
                            D3 += 1;
                    if i+1<=len(field)-1 and i-3>=0 and j+3<=len(field)-1 and j-1>=0:
                        if (field[i-2][j+2] ==  SELF and field[i-1][j+1] == SELF and field[i][j] == SELF and field[i+1][j-1] == OPPONENT) != \
                           (field[i-2][j+2] ==  SELF and field[i-1][j+1] == SELF and field[i][j] == SELF and field[i-3][j+3] == OPPONENT):
                            D3 += 1;
                    if i<=len(field)-1 and i-4>=0 and j+4<=len(field)-1 and j>=0:
                        if (field[i-3][j+3] ==  SELF and field[i-2][j+2] == SELF and field[i-1][j+1] == SELF and field[i][j] == OPPONENT) != \
                           (field[i-3][j+3] ==  SELF and field[i-2][j+2] == SELF and field[i-1][j+1] == SELF and field[i-4][j+4] == OPPONENT):
                            D3 += 1;

                    #L2, HORIZONTAL
                    if j<=len(field)-1 and j-3>=0:
                        if field[i][j-3] == 0 and field[i][j-2] == SELF and field[i][j-1] == SELF and field[i][j] == 0:
                            L2 += 1;
                    if j+1<=len(field)-1 and j-2>=0:
                        if field[i][j-2] == 0 and field[i][j-1] == SELF and field[i][j] == SELF and field[i][j+1] == 0:
                            L2 += 1;
                    if j+2<=len(field)-1 and j-1>=0:
                        if field[i][j-1] == 0 and field[i][j] == SELF and field[i][j+1] == SELF and field[i][j+2] == 0:
                            L2 += 1;
                    if j+3<=len(field)-1 and j>=0:
                        if field[i][j] == 0 and field[i][j+1] == SELF and field[i][j+2] == SELF and field[i][j+3] == 0:
                            L2 += 1;
                    #L2, PERPENDICULAR
                    if i<=len(field)-1 and i-3>=0:
                        if field[i-3][j] == 0 and field[i-2][j] ==  SELF and field[i-1][j] == SELF and field[i][j] == 0:
                            L2 += 1;
                    if i+1<=len(field)-1 and i-2>=0:
                        if field[i-2][j] == 0 and field[i-1][j] == SELF and field[i][j] == SELF and field[i+1][j] == 0:
                            L2 += 1;
                    if i+2<=len(field)-1 and i-1>=0:
                        if field[i-1][j] == 0 and field[i][j] == SELF and field[i+1][j] == SELF and field[i+2][j] == 0:
                            L2 += 1;
                    if i+3<=len(field)-1 and i>=0:
                        if field[i][j] == 0 and field[i+1][j] == SELF and field[i+2][j] == SELF and field[i+3][j] == 0:
                            L2 += 1;
                    #L2, DECLINE
                    if i+3<=len(field)-1 and i>=0 and j+3<=len(field)-1 and j>=0:
                        if field[i][j] == 0 and field[i+1][j+1] == SELF and field[i+2][j+2] == SELF and field[i+3][j+1] == 0:
                            L2 += 1;
                    if i+2<=len(field)-1 and i-1>=0 and j+2<=len(field)-1 and j-1>=0:
                        if field[i-1][j-1] == 0 and field[i][j] == SELF and field[i+1][j+1] == SELF and field[i+2][j+2] == 0:
                            L2 += 1;
                    if i+1<=len(field)-1 and i-2>=0 and j+1<=len(field)-1 and j-2>=0:
                        if field[i-2][j-2] == 0 and field[i-1][j-1] == SELF and field[i][j] == SELF and field[i+1][j+1] == 0:
                            L2 += 1;
                    if i<=len(field)-1 and i-3>=0 and j<=len(field)-1 and j-3>=0:
                        if field[i-3][j-3] == 0 and field[i-2][j-2] == SELF and field[i-1][j-1] == SELF and field[i][j] == 0:
                            L2 += 1;
                    #L2, RISE
                    if i+3<=len(field)-1 and i>=0 and j<=len(field)-1 and j-3>=0:
                        if field[i][j] == 0 and field[i+1][j-1] ==  SELF and field[i+2][j-2] == SELF and field[i+3][j-3] == 0:
                            L2 += 1;
                    if i+2<=len(field)-1 and i-1>=0 and j+1<=len(field)-1 and j-2>=0:
                        if field[i-1][j+1] == 0 and field[i][j] ==  SELF and field[i+1][j-1] == SELF and field[i+2][j-2] == 0:
                            L2 += 1;
                    if i+1<=len(field)-1 and i-2>=0 and j+2<=len(field)-1 and j-1>=0:
                        if field[i-2][j+2] == 0 and field[i-1][j+1] ==  SELF and field[i][j] == SELF and field[i+1][j-1] == 0:
                            L2 += 1;
                    if i<=len(field)-1 and i-3>=0 and j+3<=len(field)-1 and j>=0:
                        if field[i-3][j+3] == 0 and field[i-2][j+2] ==  SELF and field[i-1][j+1] == SELF and field[i][j] == 0:
                            L2 += 1;
                    #L2, RISE
                    if i+3<=len(field)-1 and i>=0 and j<=len(field)-1 and j-3>=0:
                        if field[i][j] == 0 and field[i+1][j-1] ==  SELF and field[i+2][j-2] == SELF and field[i+3][j-3] == 0:
                            L2 += 1;
                    if i+2<=len(field)-1 and i-1>=0 and j+1<=len(field)-1 and j-2>=0:
                        if field[i-1][j+1] == 0 and field[i][j] ==  SELF and field[i+1][j-1] == SELF and field[i+2][j-2] == 0:
                            L2 += 1;
                    if i+1<=len(field)-1 and i-2>=0 and j+2<=len(field)-1 and j-1>=0:
                        if field[i-2][j+2] == 0 and field[i-1][j+1] ==  SELF and field[i][j] == SELF and field[i+1][j-1] == 0:
                            L2 += 1;
                    if i<=len(field)-1 and i-3>=0 and j+3<=len(field)-1 and j>=0:
                        if field[i-3][j+3] == 0 and field[i-2][j+2] ==  SELF and field[i-1][j+1] == SELF and field[i][j] == 0:
                            L2 += 1;

                    #L2, HORIZONTAL, JUMPING
                    if j+1<=len(field)-1 and j-4>=0:
                        if field[i][j-4] == 0 and field[i][j-3] == SELF and field[i][j-2] == 0 and field[i][j-1] == 0 and field[i][j] == SELF and field[i][j+1] == 0:
                            JL2 += 1;
                    if j+1<=len(field)-1 and j-4>=0:
                        if field[i][j-4] == 0 and field[i][j-3] == 0 and field[i][j-2] == SELF and field[i][j-1] == 0 and field[i][j] == SELF and field[i][j+1] == 0:
                            JL2 += 1;
                    if j+4<=len(field)-1 and j-1>=0:
                        if field[i][j-1] == 0 and field[i][j] == SELF and field[i][j+1] == 0 and field[i][j+2] == SELF and field[i][j+3] == 0 and field[i][j+4] == 0:
                            JL2 += 1;
                    if j+4<=len(field)-1 and j-1>=0:
                        if field[i][j-1] == 0 and field[i][j] == SELF and field[i][j+1] == 0 and field[i][j+2] == 0 and field[i][j+3] == SELF and field[i][j+4] == 0:
                            JL2 += 1;
                    #L2, PERPENDICULAR, JUMPING
                    if i+1<=len(field)-1 and i-4>=0:
                        if field[i-4][j] == 0 and field[i-3][j] == SELF and field[i-2][j] == 0 and field[i-1][j] == 0 and field[i][j] == SELF and field[i+1][j] == 0:
                            JL2 += 1;
                    if i+1<=len(field)-1 and i-4>=0:
                        if field[i-4][j] == 0 and field[i-3][j] == 0 and field[i-2][j] == SELF and field[i-1][j] == 0 and field[i][j] == SELF and field[i+1][j] == 0:
                            JL2 += 1;
                    if i+4<=len(field)-1 and i-1>=0:
                        if field[i-1][j] == 0 and field[i][j] == SELF and field[i+1][j] == 0 and field[i+2][j] == SELF and field[i+3][j] == 0 and field[i+4][j] == 0:
                            JL2 += 1;
                    if i+4<=len(field)-1 and i-1>=0:
                        if field[i-1][j] == 0 and field[i][j] == SELF and field[i+1][j] == 0 and field[i+2][j] == 0 and field[i+3][j] == SELF and field[i+4][j] == 0:
                            JL2 += 1;
                    #L2, DECLINE, JUMPING
                    if i+4<=len(field)-1 and i-1>=0 and j+4<=len(field)-1 and j-1>=0:
                        if field[i-1][j-1] == 0 and field[i][j] == SELF and field[i+1][j+1] == 0 and field[i+2][j+2] == SELF and field[i+3][j+3] == 0 and field[i+4][j+4] == 0:
                            JL2 += 1;
                    if i+4<=len(field)-1 and i-1>=0 and j+4<=len(field)-1 and j-1>=0:
                        if field[i-1][j-1] == 0 and field[i][j] == SELF and field[i+1][j+1] == 0 and field[i+2][j+2] == 0 and field[i+3][j+3] == SELF and field[i+4][j+4] == 0:
                            JL2 += 1;
                    if i+1<=len(field)-1 and i-4>=0 and j+1<=len(field)-1 and j-4>=0:
                        if field[i-4][j-4] == 0 and field[i-3][j-3] == SELF and field[i-2][j-2] == 0 and field[i-1][j-1] == 0 and field[i][j] == SELF and field[i+1][j+1] == 0:
                            JL2 += 1;
                    if i+1<=len(field)-1 and i-4>=0 and j+1<=len(field)-1 and j-4>=0:
                        if field[i-4][j-4] == 0 and field[i-3][j-3] == 0 and field[i-2][j-2] == SELF and field[i-1][j-1] == 0 and field[i][j] == SELF and field[i+1][j+1] == 0:
                            JL2 += 1;
                    #L2, RISE, JUMPING
                    if i+4<=len(field)-1 and i-1>=0 and j+1<=len(field)-1 and j-4>=0:
                        if field[i-1][j+1] == 0 and field[i][j] ==  SELF and field[i+1][j-1] == 0 and field[i+2][j-2] == SELF and field[i+3][j-3] == 0 and field[i+4][j-4] == 0:
                            JL2 += 1;
                    if i+4<=len(field)-1 and i-1>=0 and j+1<=len(field)-1 and j-4>=0:
                        if field[i-1][j+1] == 0 and field[i][j] ==  SELF and field[i+1][j-1] == 0 and field[i+2][j-2] == 0 and field[i+3][j-3] == SELF and field[i+4][j-4] == 0:
                            JL2 += 1;
                    if i+1<=len(field)-1 and i-4>=0 and j+4<=len(field)-1 and j-1>=0:
                        if field[i-4][j+4] == 0 and field[i-3][j+3] ==  SELF and field[i-2][j+2] == 0 and field[i-1][j+1] == 0 and field[i][j] == SELF and field[i+1][j-1] == 0:
                            JL2 += 1;
                    if i+1<=len(field)-1 and i-4>=0 and j+4<=len(field)-1 and j-1>=0:
                        if field[i-4][j+4] == 0 and field[i-3][j+3] ==  0 and field[i-2][j+2] == SELF and field[i-1][j+1] == 0 and field[i][j] == SELF and field[i+1][j-1] == 0:
                            JL2 += 1;

                    #D2, HORIZONTAL
                    if j<=len(field)-1 and j-3>=0:
                        if (field[i][j-2] == SELF and field[i][j-1] == SELF and field[i][j] == OPPONENT) != \
                           (field[i][j-2] == SELF and field[i][j-1] == SELF and field[i][j-3] == OPPONENT):
                            D2 += 1;
                    if j+1<=len(field)-1 and j-2>=0:
                        if (field[i][j-1] == SELF and field[i][j] == SELF and field[i][j+1] == OPPONENT) != \
                           (field[i][j-1] == SELF and field[i][j] == SELF and field[i][j-2] == OPPONENT):
                            D2 += 1;
                    if j+2<=len(field)-1 and j-1>=0:
                        if (field[i][j] == SELF and field[i][j+1] == SELF and field[i][j+2] == OPPONENT) != \
                           (field[i][j] == SELF and field[i][j+1] == SELF and field[i][j-1] == OPPONENT):
                            D2 += 1;
                    if j+3<=len(field)-1 and j>=0:
                        if (field[i][j+1] == SELF and field[i][j+2] == SELF and field[i][j+3] == OPPONENT) != \
                           (field[i][j+1] == SELF and field[i][j+2] == SELF and field[i][j] == OPPONENT):
                            D2 += 1;
                    #D2, PERPENDICULAR
                    if i<=len(field)-1 and i-3>=0:
                        if (field[i-2][j] == SELF and field[i-1][j] == SELF and field[i][j] == OPPONENT) != \
                           (field[i-2][j] == SELF and field[i-1][j] == SELF and field[i-3][j] == OPPONENT):
                            D2 += 1;
                    if i+1<=len(field)-1 and i-2>=0:
                        if (field[i-1][j] == SELF and field[i][j] == SELF and field[i+1][j] == OPPONENT) != \
                           (field[i-1][j] == SELF and field[i][j] == SELF and field[i-2][j] == OPPONENT):
                            D2 += 1;
                    if i+2<=len(field)-1 and i-1>=0:
                        if (field[i][j] == SELF and field[i+1][j] == SELF and field[i+2][j] == OPPONENT) != \
                           (field[i][j] == SELF and field[i+1][j] == SELF and field[i-1][j] == OPPONENT):
                            D2 += 1;
                    if i+3<=len(field)-1 and i>=0:
                        if (field[i+1][j] == SELF and field[i+2][j] == SELF and field[i+3][j] == OPPONENT) != \
                           (field[i+1][j] == SELF and field[i+2][j] == SELF and field[i][j] == OPPONENT):
                            D2 += 1;
                    #D2, DECLINE
                    if i+3<=len(field)-1 and i>=0 and j+3<=len(field)-1 and j>=0:
                        if (field[i+1][j+1] ==  SELF and field[i+2][j+2] == SELF and field[i+3][j+3] == OPPONENT) != \
                           (field[i+1][j+1] ==  SELF and field[i+2][j+2] == SELF and field[i][j] == OPPONENT):
                            D2 += 1;
                    if i+2<=len(field)-1 and i-1>=0 and j+2<=len(field)-1 and j-1>=0:
                        if (field[i][j] ==  SELF and field[i+1][j+1] == SELF and field[i+2][j+2] == OPPONENT) != \
                           (field[i][j] ==  SELF and field[i+1][j+1] == SELF and field[i-1][j-1] == OPPONENT):
                            D2 += 1;
                    if i+1<=len(field)-1 and i-2>=0 and j+1<=len(field)-1 and j-2>=0:
                        if (field[i-1][j-1] == SELF and field[i][j] == SELF and field[i+1][j+1] == OPPONENT) != \
                           (field[i-1][j-1] == SELF and field[i][j] == SELF and field[i-2][j-2] == OPPONENT):
                            D2 += 1;
                    if i<=len(field)-1 and i-3>=0 and j<=len(field)-1 and j-3>=0:
                        if (field[i-2][j-2] == SELF and field[i-1][j-1] == SELF and field[i][j] == OPPONENT) != \
                           (field[i-2][j-2] == SELF and field[i-1][j-1] == SELF and field[i-3][j-3] == OPPONENT):
                            D2 += 1;
                    #D2, RISE
                    if i+3<=len(field)-1 and i>=0 and j<=len(field)-1 and j-3>=0:
                        if (field[i+1][j-1] ==  SELF and field[i+2][j-2] == SELF and field[i+3][j-3] == OPPONENT) != \
                           (field[i+1][j-1] ==  SELF and field[i+2][j-2] == SELF and field[i][j] == OPPONENT):
                            D2 += 1;
                    if i+2<=len(field)-1 and i-1>=0 and j+1<=len(field)-1 and j-2>=0:
                        if (field[i][j] ==  SELF and field[i+1][j-1] == SELF and field[i+2][j-2] == OPPONENT) != \
                           (field[i][j] ==  SELF and field[i+1][j-1] == SELF and field[i-1][j+1] == OPPONENT):
                            D2 += 1;
                    if i+1<=len(field)-1 and i-2>=0 and j+2<=len(field)-1 and j-1>=0:
                        if (field[i-1][j+1] ==  SELF and field[i][j] == SELF and field[i+1][j-1] == OPPONENT) != \
                           (field[i-1][j+1] ==  SELF and field[i][j] == SELF and field[i-2][j+2] == OPPONENT):
                            D2 += 1;
                    if i<=len(field)-1 and i-3>=0 and j+3<=len(field)-1 and j>=0:
                        if (field[i-2][j+2] ==  SELF and field[i-1][j+1] == SELF and field[i][j] == OPPONENT) != \
                           (field[i-2][j+2] ==  SELF and field[i-1][j+1] == SELF and field[i-3][j+3] == OPPONENT):
                            D2 += 1;
                        
                field[i][j] = 0;
                SPOTSCORE = 0;

                #Add score according to score object
                while L5 >= 1:
                    SPOTSCORE += 100000;
                    if MODE == COMPUTER:
                        SPOTSCORE += 100000;
                    L5 -= 1;
                while L4 >= 1:
                    SPOTSCORE += 10000;
                    L4 -= 1;
                while D4 >= 2:
                    SPOTSCORE += 10000;
                    D4 -= 2;
                while D4 >= 1 and L3 >= 1:
                    SPOTSCORE += 10000;
                    D4 -= 1; L3 -= 1;
                while L3 >= 2:
                    SPOTSCORE += 5000;
                    L3 -= 2;
                while L3 >= 1 and JL3 >= 1:
                    SPOTSCORE += 5000;
                    L3 -= 1; JL3 -= 1;
                while JL3 >= 2:
                    SPOTSCORE += 5000;
                    JL3 -= 2;
                while L3 >= 1 and D3 >= 1:
                    SPOTSCORE += 1000;
                    L3 -= 1; D3 -= 1;
                while D4 >= 1:
                    SPOTSCORE += 500;
                    D4 -= 1;
                while L3 >= 1:
                    SPOTSCORE += 100;
                    L3 -= 1;
                while JL3 >= 1:
                    SPOTSCORE += 90;
                    JL3 -= 1;
                while L2 >= 2:
                    SPOTSCORE += 50;
                    L2 -= 2;
                while L2 >= 1:
                    SPOTSCORE += 10;
                    L2 -= 1;
                while JL2 >= 1:
                    SPOTSCORE += 9;
                    JL2 -= 1;
                while D3 >= 1:
                    SPOTSCORE += 5;
                    D3 -= 1;
                while D2 >= 1:
                    SPOTSCORE += 2;
                    D2 -= 1;

                #AI gets one extra offensive score
                if MODE == COMPUTER:
                    SPOTSCORE += 5;
                COE[i][j] += SPOTSCORE;


def DECIDE():
    CURRENT_MAX = 0;
    for i in range(15):
        for j in range(15):
            CURRENT_MAX = max(CURRENT_MAX, COE[i][j]);

    #List all max scores
    POSSIBLE_X = [];
    POSSIBLE_Y = [];
    for i in range(15):
        for j in range(15):
            if COE[i][j] == CURRENT_MAX:
                    POSSIBLE_X.append(i+1);
                    POSSIBLE_Y.append(j+1);

    #Randomly choose one from max scores
    R = random.randint(0,len(POSSIBLE_X)-1);
    x = POSSIBLE_X[R];
    y = POSSIBLE_Y[R];
    canvas.create_oval( y*40-5, x*40-5, y*40+25, x*40+25, fill=COMPUTER);
    
    canvas.itemconfig(INFO, text=("Latest Computer Position: %s %s"%(x,y)), font=("Comic Sans MS", 20), fill="black");
    #SIGN = canvas.create_text( y*40+10, x*40+10, text="+", fill="red", font=("Comic Sans MS", 25));
    canvas.coords(SIGN,(y*40+10, x*40+10));
    canvas.itemconfig(SIGN, text="+", fill="red", font=("Comic Sans MS", 25));
    canvas.coords(SIGN,(y*40+10, x*40+10));
    #SIGN = canvas.create_text( y*40+10, x*40+10, text="+", fill="red", font=("Comic Sans MS", 25));
    field[x-1][y-1] = COMPUTER;
    win();

    #Clear score list
    global TURN;
    TURN = True;
    for i in range(15):
        for j in range(15):
            COE[i][j] = 0;
    

def win():
    global playerWin;
    playerWin = False;
    global computerWin;
    computerWin = False;

    #Judge if win
    for i in range(0,15):
        for j in range(0,15):
            if i+2<=len(field)-1 and i-2>=0:
                if field[i-2][j] ==  PLAYER and field[i-1][j] == PLAYER and field[i][j] == PLAYER and field[i+1][j] == PLAYER and field[i+2][j] == PLAYER:
                    playerWin = True;
                if field[i-2][j] ==  COMPUTER and field[i-1][j] == COMPUTER and field[i][j] == COMPUTER and field[i+1][j] == COMPUTER and field[i+2][j] == COMPUTER:
                    computerWin = True;
            if j+2<=len(field)-1 and j-2>=0:
                if field[i][j-2] ==  PLAYER and field[i][j-1] == PLAYER and field[i][j] == PLAYER and field[i][j+1] == PLAYER and field[i][j+2] == PLAYER:
                    playerWin = True;
                if field[i][j-2] ==  COMPUTER and field[i][j-1] == COMPUTER and field[i][j] == COMPUTER and field[i][j+1] == COMPUTER and field[i][j+2] == COMPUTER:
                    computerWin = True;
                    
                if i+2<=len(field)-1 and i-2>=0:
                    if field[i-2][j-2] ==  PLAYER and field[i-1][j-1] == PLAYER and field[i][j] == PLAYER and field[i+1][j+1] == PLAYER and field[i+2][j+2] == PLAYER:
                        playerWin = True;
                    if field[i+2][j-2] ==  PLAYER and field[i+1][j-1] == PLAYER and field[i][j] == PLAYER and field[i-1][j+1] == PLAYER and field[i-2][j+2] == PLAYER:
                        playerWin = True;
                    if field[i-2][j-2] ==  COMPUTER and field[i-1][j-1] == COMPUTER and field[i][j] == COMPUTER and field[i+1][j+1] == COMPUTER and field[i+2][j+2] == COMPUTER:
                        computerWin = True;
                    if field[i+2][j-2] ==  COMPUTER and field[i+1][j-1] == COMPUTER and field[i][j] == COMPUTER and field[i-1][j+1] == COMPUTER and field[i-2][j+2] == COMPUTER:
                        computerWin = True;
    if playerWin == True:
        canvas.create_text(330, 330, text="You Win!", font=("Comic Sans MS", 50), fill="green");
        canvas.update();
        time.sleep(5);
    elif computerWin == True:
        canvas.create_text(330, 330, text="Game Over!", font=("Comic Sans MS", 50), fill="red");
        canvas.update();
        time.sleep(5);

def click(event):
    global TURN;
    if TURN == True:
        clickPos = [];
        clickPos.append(event.x);
        clickPos.append(event.y);
        x = round((clickPos[1]-10)/40);
        y = round((clickPos[0]-10)/40);
        if 0<x<16 and 0<y<16:
            if field[x-1][y-1] != COMPUTER and field[x-1][y-1] != PLAYER:
                field[x-1][y-1] = PLAYER;
                canvas.create_oval( y*40-5, x*40-5, y*40+25, x*40+25, fill=PLAYER);
                win();
                TURN = False;
                if playerWin == False:
                    AI(COMPUTER);
                    AI(PLAYER);
                    DECIDE();

field = [[0 for i in range(15)] for i in range(15)];
tk = tkinter.Tk();
tk.title("FIVE IN A ROW - version 0.2");
tk.resizable(0,0);
tk.bind("<Button-1>", click);
canvas = tkinter.Canvas(tk, width=660, height=700);
canvas.create_rectangle(0, 0, 660, 700, fill="silver");
INFO = canvas.create_text(330, 650, text="Latest Computer Position: - -", font=("Comic Sans MS", 20), fill="black");
SIGN = canvas.create_text(0, 0, text=" ", fill="red", font=("Comic Sans MS", 25));
canvas.pack();
COE = [[0 for i in range(15)] for i in range(15)];
TURN = True;

FIRST_TURN = random.randint(0,1);
if FIRST_TURN == 0:
    COMPUTER = "black";
    PLAYER = "white";
    FIRST_X = random.randint(6,8);
    FIRST_Y = random.randint(6,8);
    field[FIRST_X][FIRST_Y] = COMPUTER;
    canvas.create_oval(FIRST_Y*40+35, FIRST_X*40+35, FIRST_Y*40+65, FIRST_X*40+65, fill=COMPUTER);
    canvas.itemconfig(INFO, text=("Latest Computer Position: %s %s"%(FIRST_X+1,FIRST_Y+1)), font=("Comic Sans MS", 20), fill="black");
else:
    COMPUTER = "white";
    PLAYER = "black";
    canvas.itemconfig(INFO, text="Now it's your turn!", font=("Comic Sans MS", 20), fill="black");

playerWin = False;
computerWin = False;
    
for i in range(0, 15):
    canvas.create_line(50, 50+40*i, 610, 50+40*i);
    canvas.create_line(50+40*i, 50, 50+40*i, 610);

while playerWin == False and computerWin == False:
    canvas.update();




