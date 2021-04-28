from fastapi import APIRouter
from pydantic import BaseModel, Field

from function import create_Stem, remove_Punctuation, remove_Stop_Words, jaccard_Similarity

'''
    This will be where the router takes place, will still be on the main page 
    This organizes the code for easy review. 
'''

# Declaring my router
router = APIRouter()

class Item(BaseModel):
    ''' 
        This class contains what the models takes in for consideration.
        The class will include example values in case the user does not 
        want to fill in the data. Will allow the function to run without user
        input.
    '''
    sample: str = Field(...,example="The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you.")
    sample1: str = Field(...,example="The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you.")

@router.post('/checkSim')
def check_Sim(user_input: Item):
    '''
        This function will take strings inside the dict, then compare the two 
        for text similarity using jaccard similarity
    '''

    # Now comparing the two and returning the results 
    return jaccard_Similarity(user_input.sample, user_input.sample1)
    