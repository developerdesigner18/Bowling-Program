knock_down,score,shot = 0,0,1
step = 0
pin = 10
bal_pin = 10

# Function to take a valid input
def Input():
    global knock_down,bal_pin, chance
    knock_down = int(input("Total no of pins down in the shot : "))
    if knock_down > bal_pin:
        print(f"Input should be lower than or equal to {bal_pin}")
        Input()
    else:
        bal_pin = bal_pin - knock_down
        
         
    return knock_down


def Bowling():
    global shot, knock_down, chance, step, chance_score, bal_pin, score
    while (shot > 0):
        shot -= 1
        print("Remaining shots = ",shot+1)
        knock_down = Input()
            
        # Condition to integrate the spare logic
        try:
            if chance <= 2:
                chance -= 1

                if bal_pin == 0:
                    shot += 1            
                
        except:
            pass
             
        if knock_down == 10:
            chance = 2
                   
        if bal_pin == 0:
            bal_pin = 10
        
        print("Remaining pin - ",bal_pin)
        
        # Check strike logic
        if (knock_down == 10):
            shot += 2   
            score += knock_down
            print("Total score = ",score)
            return Bowling()           
            
        else:             
            score += knock_down
            print("Total score = ",score)
            return Bowling()
        
    else:
        print("Game Over")
                   
            

Bowling()     
     
    