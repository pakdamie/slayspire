import numpy as np

def initiate_cards(n_size):
    """
    Initiate a data.frame with n_size number of cards

    Parameters:
        n_size (integer): Total number of cards
    """
    
    #card_id with 0 being the update card and 
    #status with 0 being standard and 1 being upgraded
    matrix = np.column_stack((np.arange(n_size), np.array([1] + [0]*(n_size-1))))
    
    return matrix
def draw_cards(n_size):

    """
    Draw 5 cards and upgrade the cards if you have the special upgrade card. 
    Give me the number of turns it take

    Parameters:
        n_size (integer): Total number of cards
    """

    #Initiate a deck of n_size cards and have a draw pile that is initially
    #all of the card id 
    deck_cards = initiate_cards(n_size)
    draw_pile =  deck_cards[:, 0].copy()
    turns = 0 

    #All cards are updated when the sum of "status" column equals
    #n_size. Example a 3-card deck with (1,1,1) means that it's all updated
    
    while deck_cards[:,1].sum() != n_size: 
        
        #  If there's enough cards in the draw pile then draw 5 cards from the deck randomly  
        if len(draw_pile) >= 5:
            drawn_cards = np.random.choice(draw_pile, size=5, replace=False)   

        # If there's not enough cards in the draw pile, then pick up all the cards you can
        #from the the draw pile. The drawl will then "be reshuffled"
        else:
            remaining_cards = draw_pile
            draw_pile = deck_cards[~np.isin(deck_cards[:, 0], remaining_cards), 0]
            supplement_card = np.random.choice(draw_pile, size=5 - len(remaining_cards), replace=False)           
            
            #This now has the cards that you picked up before you shuffled
            #And the cards after you shuffled.
            drawn_cards =  np.concatenate((remaining_cards, supplement_card))

        #If any of the drawn cards has the upgrade card (0),
        #then make it so that the entire cards in this HAND is upgraded.
        if (drawn_cards == 0).any():
            deck_cards[np.isin(deck_cards[:,0], drawn_cards), 1] = 1
        
        #The new draw pile is the cards that aren't drawn.
        draw_pile = draw_pile[~np.isin(draw_pile, drawn_cards)]
        
        #Increment a turn
        turns += 1 
        
    return(turns)


def simulate_runs():

    """
    Given the total number of cards (total_cards), run 1000 trials and 
    tell me how many turns until all cards are updated!

    """


    total_cards = np.array([10,15,20,25,30,35])

    #Each column is the total number of cards
    #Each row is a run
    result_array = np.array([
    [draw_cards(tc) for tc in total_cards]   # one row = all settings for a run
    for _ in range(1000)])

    return(result_array)
