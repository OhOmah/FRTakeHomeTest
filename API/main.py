from fastapi import FastAPI

import checkSim

'''
    This will be the main page. 
'''

# Declaring the fast api object for deployment. 
app = FastAPI()

# including routers
app.include_router(checkSim.router)

